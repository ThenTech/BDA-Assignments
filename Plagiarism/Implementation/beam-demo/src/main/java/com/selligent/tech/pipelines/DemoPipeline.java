package com.selligent.tech.pipelines;

import com.selligent.tech.models.OptiExtEvent;
import com.selligent.tech.models.coders.OptiExtEventCoder;
import com.selligent.tech.pipelines.config.DemoPipelineOptions;
import com.selligent.tech.pipelines.operations.BigTableTenantWindowWriter;
import com.selligent.tech.pipelines.operations.AlertingCreator;
import org.apache.beam.runners.dataflow.DataflowRunner;
import org.apache.beam.sdk.Pipeline;
import org.apache.beam.sdk.coders.CoderRegistry;
import org.apache.beam.sdk.extensions.jackson.ParseJsons;
import org.apache.beam.sdk.io.gcp.pubsub.PubsubIO;
import org.apache.beam.sdk.options.PipelineOptionsFactory;
import org.apache.beam.sdk.transforms.*;
import org.apache.beam.sdk.transforms.windowing.*;
import org.apache.beam.sdk.values.KV;
import org.apache.beam.sdk.values.PCollection;
import org.jetbrains.annotations.NotNull;
import org.joda.time.Duration;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

/**
 *  Demo Pipeline
 *  -------------
 *
 *  Demonstration pipeline that operates on incoming {@link OptiExtEvent} objects. The pipeline produces a timeline
 *  representing the number of interactions received by each organization within the context of a window. The pipeline
 *  windows the events according to the settings specified in the {@link DemoPipelineOptions} options. Window results
 *  are materialized when the watermark passes the end of the window. Moreover, speculative results are emitted when the
 *  window is processed. The timeline is stored in format that is friendly for consumption by a charting library.
 *
 *  How to run?
 *  ------------
 *
 *      mvn compile -e exec:java -Dexec.mainClass=com.selligent.tech.pipelines.DemoPipeline
 *
 *  Clear topic
 *  ------------
 *
 *      gcloud alpha pubsub subscriptions pull projects/uh-bigdata/subscriptions/demo-sub --auto-ack
 *
 *  Helpfull
 *  -------------
 *
 *      cbt -project=uh-bigdata -instance=bt-demo createtable demo
 *      cbt -project=uh-bigdata -instance=bt-demo createfamily demo perTenant
 *      cbt -project=uh-bigdata -instance=bt-demo read demo
 *
 *  Created by Laurens Vijnck on 23/07/19.
 */
public class DemoPipeline {

    private static final Logger LOG = LoggerFactory.getLogger(DemoPipeline.class);

    /**
     * Function performs a simple input-to-output mapping function, i.e., a single
     * input produces a single output. The extractor outputs KV-pair where the tenant
     * attribute of the event is promoted to the key.
     */
    private static class OrganizationExtractor extends SimpleFunction<OptiExtEvent, KV<String, OptiExtEvent>> {
        public  KV<String, OptiExtEvent> apply(OptiExtEvent event) {
            return KV.of(event.getTenantId(), event);
        }
    }

    private static void assemblePipeline(@NotNull Pipeline pipeline, @NotNull DemoPipelineOptions options) {

        // Ingest and parse events
        PCollection<KV<String, OptiExtEvent>> events = pipeline
                .apply("Ingest", PubsubIO.readStrings().fromSubscription(options.getPubSubInputTopicSubscription()).withTimestampAttribute("event_ts"))
                .apply("Parse", ParseJsons.of(OptiExtEvent.class)).setCoder(new OptiExtEventCoder())
                .apply("ExtractTenant", MapElements.via(new OrganizationExtractor()));

        // Window data
        PCollection<KV<String, OptiExtEvent>> windowedEvents = events
                .apply("Window", Window.<KV<String, OptiExtEvent>>into(
                        FixedWindows.of(Duration.standardSeconds(options.getWindowSizeInSeconds()))
                )
                .triggering(
                        AfterWatermark.pastEndOfWindow()
                            .withEarlyFirings(AfterProcessingTime.pastFirstElementInPane()
                                    .plusDelayOf(Duration.standardSeconds(options.getEarlyFiringDelay()))
                            )
                )
                .accumulatingFiredPanes()
                .withAllowedLateness(Duration.ZERO, Window.ClosingBehavior.FIRE_ALWAYS)
                .withTimestampCombiner(TimestampCombiner.END_OF_WINDOW)
        );

        // Combine results
        PCollection<KV<String, Long>> grouped = windowedEvents.apply("Combine", Count.perKey());

        // Process results
        grouped.apply("WriteToBigTable", new BigTableTenantWindowWriter(options));
        grouped.apply("Alerting", new AlertingCreator(options));
    }

    public static void main(String[] args) {

        // Parse arguments into options
        DemoPipelineOptions options = PipelineOptionsFactory
                .fromArgs(args)
                .withValidation()
                .create()
                .as(DemoPipelineOptions.class);

        // Create pipeline object
        Pipeline p = Pipeline.create(options);

        // Set specific Dataflow options
        options.setJobName("demo-pipeline");
        options.setRegion("europe-west1");
        options.setZone("europe-west1-b");
        options.setProject("uh-bigdata");
        options.setWorkerMachineType("n1-standard-1");
        options.setRunner(DataflowRunner.class);
        options.setUpdate(true);

        // Registering coders (for serialization purposes)
        CoderRegistry cr = p.getCoderRegistry();
        cr.registerCoderForClass(OptiExtEvent.class, new OptiExtEventCoder());

        // Assemble pipeline
        assemblePipeline(p, options);

        // Run the pipeline
        p.run();
    }
}
