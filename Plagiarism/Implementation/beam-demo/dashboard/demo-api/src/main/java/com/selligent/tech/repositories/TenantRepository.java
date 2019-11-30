package com.selligent.tech.repositories;

import com.google.cloud.bigtable.hbase.BigtableConfiguration;
import com.selligent.tech.models.TimelinePair;
import org.apache.hadoop.hbase.TableName;
import org.apache.hadoop.hbase.client.Connection;
import org.apache.hadoop.hbase.client.Result;
import org.apache.hadoop.hbase.client.Scan;
import org.apache.hadoop.hbase.client.Table;
import org.apache.hadoop.hbase.util.Bytes;
import org.springframework.stereotype.Repository;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

@Repository("tenantRepository")
public class TenantRepository {

    private static final Connection connection = BigtableConfiguration.connect("uh-bigdata", "bt-demo");
    private static final String DEMO_TABLE = "demo";
    private static final String TENANT_CF = "perTenant";

    public List<TimelinePair> fetchTimeline(String tenant, Long startTime, Long endTime) throws IOException {
        try (Table table = connection.getTable(TableName.valueOf(DEMO_TABLE))) {

            // Create rowscan
            Scan scan = new Scan(Bytes.toBytes("interactions#" + tenant + "#" + startTime), Bytes.toBytes("interactions#" + tenant + "#" + endTime));
            scan.addFamily(Bytes.toBytes(TENANT_CF));

            // Iterate result and parse
            List<TimelinePair> timeline = new ArrayList<>();
            Iterable<Result> iter = table.getScanner(scan);
            for(Result result: iter) {

                try {
                    // Create pair
                    TimelinePair pair = new TimelinePair();

                    // Get count
                    byte[] array;
                    array = result.getValue(Bytes.toBytes(TENANT_CF), Bytes.toBytes("count"));
                    pair.setCount(Long.parseLong(Bytes.toString(array)));

                    // Get time
                    String ts = Bytes.toString(result.getRow()).split("#")[2]; // ugly but will do
                    pair.setTimestamp(Long.parseLong(ts));

                    timeline.add(pair);
                } catch (Exception e) {
                    // Tenant not found, ignore..
                }
            }

            return timeline;
        }
    }
}
