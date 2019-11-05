package com.selligent.tech.pipelines.config;

import org.apache.beam.runners.dataflow.options.DataflowPipelineOptions;
import org.apache.beam.sdk.options.Default;
import org.apache.beam.sdk.options.Description;
import org.apache.beam.sdk.options.Validation;

/**
 * Created by Laurens Vijnck on 23/07/19.
 */
public interface DemoPipelineOptions extends DataflowPipelineOptions {

    @Description("Name of the Pub/Sub subscription to ingest data")
    @Validation.Required
    @Default.String("projects/uh-bigdata/subscriptions/demo-sub")
    String getPubSubInputTopicSubscription();
    void setPubSubInputTopicSubscription(String value);

    @Description("Window size (seconds)")
    @Default.Integer(60)
    Integer getWindowSizeInSeconds();
    void setWindowSizeInSeconds(Integer value);

    @Description("Early firing delay (seconds)")
    @Default.Integer(5)
    Integer getEarlyFiringDelay();
    void setEarlyFiringDelay(Integer value);

    @Description("Min altering threshold")
    @Default.Integer(10)
    Integer getMinAlteringThreshold();
    void setMinAlteringThreshold(Integer value);

    @Description("Max altering threshold")
    @Default.Integer(30)
    Integer getMaxAlteringThreshold();
    void setMaxAlteringThreshold(Integer value);

    @Description("Name of the Bigtable instance")
    @Default.String("bt-demo")
    String getBigTableInstance();
    void setBigTableInstance(String value);

    @Description("Name of the Bigtable table")
    @Default.String("demo")
    String getBigTableTableName();
    void setBigTableTableName(String value);

    @Description("Bigtable column family name for per tenant windowed aggregations")
    @Default.String("perTenant")
    String getBigTableTenantWindowCF();
    void setBigTableTenantWindowCF(String value);
}
