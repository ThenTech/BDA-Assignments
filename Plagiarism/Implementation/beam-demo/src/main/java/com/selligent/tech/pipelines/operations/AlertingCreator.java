package com.selligent.tech.pipelines.operations;

import com.google.common.collect.ImmutableList;
import com.google.datastore.v1.*;
import com.selligent.tech.common.GenericLogger;
import com.selligent.tech.models.Alert;
import com.selligent.tech.models.types.AlertType;
import com.selligent.tech.pipelines.config.DemoPipelineOptions;
import org.apache.beam.sdk.io.gcp.datastore.DatastoreIO;
import org.apache.beam.sdk.transforms.*;
import org.apache.beam.sdk.transforms.windowing.IntervalWindow;
import org.apache.beam.sdk.values.KV;
import org.apache.beam.sdk.values.PCollection;
import org.apache.beam.sdk.values.PDone;

/**
 * Custom transform that operates on incoming (organization, count)-pairs. The transform
 * determines whether the input element should trigger an alert based on the settings defined
 * in the {@link DemoPipelineOptions}. Alters are parsed into Datastore Entities and written
 * to Datastore using the {@link DatastoreIO} sink.
 *
 * Created by Laurens Vijnck on 23/07/19.
 */
public class AlertingCreator extends PTransform<PCollection<KV<String, Long>>, PDone> {

    private final DemoPipelineOptions options;

    public AlertingCreator(DemoPipelineOptions options) {
        this.options = options;
    }

    @Override
    public PDone expand(PCollection<KV<String, Long>> input) {

        // Apply transforms
        input
                .apply("CreateAlerts", ParDo.of(new AlertCreator(options.getMinAlteringThreshold(), options.getMaxAlteringThreshold())))
                .apply("Print", ParDo.of(new GenericLogger<>()))
                .apply("MapToEntity", MapElements.via(new AlertEntityV1Convertor()))
                .apply("WriteToDatastore", DatastoreIO.v1().write().withProjectId(options.getProject()));

        return PDone.in(input.getPipeline());
    }

    /**
     * Function determines whether the incoming event should trigger an {@link Alert}. This
     * decision is based on the minThreshold and maxThreshold values that are passed
     * to the transform upon instantiation.
     */
    private static class AlertCreator extends DoFn<KV<String, Long>, Alert> {

        private final Integer minThreshold;
        private final Integer maxThreshold;

        public AlertCreator(Integer minThreshold, Integer maxThreshold) {
            this.minThreshold = minThreshold;
            this.maxThreshold = maxThreshold;
        }

        @ProcessElement
        public void processElement(@Element KV<String, Long> element, ProcessContext c, IntervalWindow window) {

            // Only final panes should trigger alerts
            if(c.pane().isLast()) {

                if(element.getValue() < minThreshold) {
                    c.output(new Alert(element.getKey(), element.getValue(), AlertType.BELOW_MIN, window.end().getMillis()));
                } else if(element.getValue() > maxThreshold) {
                    c.output(new Alert(element.getKey(), element.getValue(), AlertType.ABOVE_MAX, window.end().getMillis()));
                }
            }
        }
    }

    /**
     * Transform to convert an {@link Alert} object to a Datastore {@link Entity}.
     */
    private static class AlertEntityV1Convertor extends SimpleFunction<Alert, Entity> {
        public Entity apply(Alert alert) {

            // Instantiate keybuilder
            Key.Builder builder = Key.newBuilder();

            // Parent key
            Key.PathElement parent = builder.addPathBuilder()
                    .setKind("tenant")
                    .setName(alert.getTenant())
                    .build();

            // Key for entity
            Key.PathElement pathElement = builder.addPathBuilder()
                    .setKind("alert")
                    .setName(alert.getKey())
                    .build();

            // Build key
            Key key = builder.build();

            // Build entity
            return Entity.newBuilder()
                    .setKey(key)
                    .putProperties("tenant", Value.newBuilder().setStringValue(alert.getTenant()).setExcludeFromIndexes(false).build())
                    .putProperties("count", Value.newBuilder().setIntegerValue(alert.getCount()).setExcludeFromIndexes(false).build())
                    .putProperties("timestamp", Value.newBuilder().setIntegerValue(alert.getTimestamp()).setExcludeFromIndexes(false).build())
                    .build();
        }
    }
}
