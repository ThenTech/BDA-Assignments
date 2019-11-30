package com.selligent.tech.pipelines.operations;

import com.google.cloud.bigtable.beam.CloudBigtableIO;
import com.google.cloud.bigtable.beam.CloudBigtableTableConfiguration;
import com.selligent.tech.pipelines.config.DemoPipelineOptions;
import org.apache.beam.sdk.transforms.*;
import org.apache.beam.sdk.values.KV;
import org.apache.beam.sdk.values.PCollection;
import org.apache.beam.sdk.values.PDone;
import org.apache.hadoop.hbase.client.Mutation;
import org.apache.hadoop.hbase.client.Put;
import org.apache.hadoop.hbase.util.Bytes;
import org.joda.time.Instant;

/**
 * Custom transform that writes (organization, count)-pairs to Bigtable table based on the
 * settings defined in the {@link DemoPipelineOptions}. Elements in the PCollection are mapped
 * onto Bigtable mutations and written using the {@link CloudBigtableIO} sink.
 *
 * Created by Laurens Vijnck on 23/07/19.
 */
public class BigTableTenantWindowWriter extends PTransform<PCollection<KV<String, Long>>, PDone> {

    private final DemoPipelineOptions options;

    public BigTableTenantWindowWriter(DemoPipelineOptions options) {
        this.options = options;
    }

    @Override
    public PDone expand(PCollection<KV<String, Long>> input) {

        // Create Bigtable configuration
        CloudBigtableTableConfiguration config = new CloudBigtableTableConfiguration.Builder()
               .withProjectId(options.getProject())
               .withInstanceId(options.getBigTableInstance())
               .withTableId(options.getBigTableTableName()).build();

        // Apply transforms
        input
                .apply("MapToMutation", ParDo.of(new MutationMapper(options.getBigTableTenantWindowCF())))
                .apply("WriteToBigTable", CloudBigtableIO.writeToTable(config));

        return PDone.in(input.getPipeline());
    }

    /**
     * Transform to map the (organization, count)-pair to a Bigtable mutation. In the process,
     * the internal timestamp of the element is used. This timestamp is accessible via
     * the ProcessContext.
     */
    private static class MutationMapper extends DoFn<KV<String, Long>, Mutation> {

        private final String tenantWindowCF;

        public MutationMapper(String tenantWindowCF) {
            this.tenantWindowCF = tenantWindowCF;
        }

        @ProcessElement
        public void processElement(@Element KV<String, Long> element, ProcessContext c) {

            Put put = new Put(Bytes.toBytes( "interactions#" + element.getKey() + "#" + c.timestamp().getMillis()));
            put.addColumn(Bytes.toBytes(tenantWindowCF), Bytes.toBytes("count"), Bytes.toBytes(Long.toString(element.getValue())));

            c.output(put);
        }
    }
}
