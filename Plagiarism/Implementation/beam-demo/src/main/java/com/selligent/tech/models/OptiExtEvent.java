package com.selligent.tech.models;

import org.codehaus.jackson.annotate.JsonProperty;
import com.google.cloud.datastore.*;

/**
 * Created by Laurens Vijnck on 23/07/19.
 */
public class OptiExtEvent {
    /*
     * Meta
     */
    @JsonProperty("tenantId")
    private String tenantId;

    @JsonProperty("organizationId")
    private String organizationId;

    /*
     * Actor
     */
    @JsonProperty("audienceId")
    private int audienceId;

    @JsonProperty("consumerId")
    private String consumerId;

    @JsonProperty("type")
    private String type;

    /*
     * Request
     */
    @JsonProperty("timestamp")
    private long timestamp;

    @JsonProperty("channel")
    private String channel;

    @JsonProperty("journeyId")
    private String journeyId;

    @JsonProperty("actionId")
    private String actionId;

    @JsonProperty("messageId")
    private String messageId;

    /*
     * Action
     */
    @JsonProperty("action")
    private String action; // View, click, delivery.

    public OptiExtEvent() {
        this.tenantId = "";
        this.organizationId = "";
        this.consumerId = "";
        this.type = "";
        this.channel = "";
        this.journeyId = "";
        this.actionId = "";
        this.messageId = "";
        this.action = "";
    }

    public String getTenantId() {
        return tenantId;
    }

    public void setTenantId(String tenantId) {
        this.tenantId = tenantId;
    }

    public String getOrganizationId() {
        return organizationId;
    }

    public void setOrganizationId(String organizationId) {
        this.organizationId = organizationId;
    }

    public int getAudienceId() {
        return audienceId;
    }

    public void setAudienceId(int audienceId) {
        this.audienceId = audienceId;
    }

    public String getConsumerId() {
        return consumerId;
    }

    public void setConsumerId(String consumerId) {
        this.consumerId = consumerId;
    }

    public long getTimestamp() {
        return timestamp;
    }

    public void setTimestamp(long timestamp) {
        this.timestamp = timestamp;
    }

    public String getChannel() {
        return channel;
    }

    public void setChannel(String channel) {
        this.channel = channel;
    }

    public String getMessageId() {
        return messageId;
    }

    public void setMessageId(String messageId) {
        this.messageId = messageId;
    }

    public String getAction() {
        return action;
    }

    public void setAction(String action) {
        this.action = action;
    }

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public String getJourneyId() {
        return journeyId;
    }

    public void setJourneyId(String journeyId) {
        this.journeyId = journeyId;
    }

    public String getActionId() {
        return actionId;
    }

    public void setActionId(String actionId) {
        this.actionId = actionId;
    }

    public Entity toEntity(Key OptieExtKey) {
        // Build entity
        return Entity.newBuilder(OptieExtKey)
                .set("tenantId", this.tenantId)
                .set("organizationId", this.organizationId)
                .set("consumerId", this.consumerId)
                .set("channel", this.channel)
                .set("journeyId", this.journeyId)
                .set("actionId", this.actionId)
                .set("messageId", this.messageId)
                .set("action", this.action)
                .set("timestamp", this.timestamp)
                .build();
    }

    public String getKey() {
        return tenantId + "#" + organizationId + "#" + consumerId + "#" + timestamp;
    }
}