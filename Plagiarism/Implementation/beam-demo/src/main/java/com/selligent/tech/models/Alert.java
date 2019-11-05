package com.selligent.tech.models;

import com.selligent.tech.models.types.AlertType;
import java.io.Serializable;

/**
 * Created by Laurens on 14/02/19.
 */
public class Alert implements Serializable {
    private String tenant;
    private Long count;
    private AlertType alertType;
    private Long timestamp;

    public Alert(String tenant, Long count, AlertType alertType, Long timestamp) {
        this.tenant = tenant;
        this.count = count;
        this.alertType = alertType;
        this.timestamp = timestamp;
    }

    public String getTenant() {
        return tenant;
    }

    public Long getCount() {
        return count;
    }

    public AlertType getAlertType() {
        return alertType;
    }

    public Long getTimestamp() {
        return timestamp;
    }

    public String toString() {
        return this.tenant + " : " + this.count + "(" + alertType.toString() + ")";
    }

    public String getKey() {
        return this.tenant + "#" + this.timestamp;
    }
}
