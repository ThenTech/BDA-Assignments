<template>
    <el-card shadow="hover">
        <div slot="header">
            <el-row>
                <el-col :span="14">
                    <div style="line-height: 40px;">
                        Tenant Interactions Timeline
                    </div>
                </el-col>
                <el-col :span="10">
                    <div style="float: right">
                        <el-select v-model="tenant" placeholder="Tenant" @change="fetchTimeline()">
                            <el-option
                                v-for="item in tenants"
                                :key="item.value"
                                :label="item.label"
                                :value="item.value">
                            </el-option>
                        </el-select>
                    </div>
                </el-col>
            </el-row>
        </div>
        <apexchart type="area" :options="options" :series="series"></apexchart>
    </el-card>
</template>

<script>
import axios from 'axios'
import moment from 'moment'

export default {
    name: "TimelineGraph",
    data: () => ({
        series: [],
        options: {},
        polling: null,
        tenant: "jda_2A8075D4-B552-4388-A86F-C7DD62E5E0E6",
        tenants: [
            {
                value: "jda_2A8075D4-B552-4388-A86F-C7DD62E5E0E6",
                label: "C7DD62E5E0E6"
            },
            {
                value: "jda_2A8075D4-B552-4388-A86F-C7DD62E5E0E7",
                label: "C7DD62E5E0E7"
            },
            {
                value: "jda_2A8075D4-B552-4388-A86F-C7DD62E5E0E8",
                label: "C7DD62E5E0E8"
            }
        ]
    }),
    created () {
        this.options = this.getOptions();
        this.fetchTimeline(this.tenant);
        this.pollData();
    },
    methods: {
        getOptions: function () {
            return {
                chart: {
                    stacked: true,
                    events: {
                        selection: function (chart, e) {
                            console.log(new moment(e.xaxis.min))
                        }
                    },
                    toolbar: {
                        show: false
                    }
                },
                colors: ['#0491FF', '#FFBE1C', '#A7B7CD'],
                dataLabels: {
                    enabled: true
                },
                stroke: {
                    curve: 'smooth'
                },
                fill: {
                    type: 'gradient',
                    gradient: {
                        opacityFrom: 0.6,
                        opacityTo: 0.8
                    }
                },
                legend: {
                    position: 'bottom',
                    horizontalAlign: 'center'
                },
                xaxis: {
                    type: 'datetime'
                }
            }
        },
        fetchTimeline: function () {
            axios.get(`tenant/timeline?tenantId=${this.tenant}&start=${moment().subtract(10, 'minutes').valueOf()}&end=${moment().add(1, 'minutes').valueOf()}`).then(response => {
                const trans = response.data.map(function (val, idx) {
                    return [val.timestamp, val.count]
                })

                this.series = [{label: this.tenant, data: trans}]
            })
        },
        pollData () {
            this.polling = setInterval(() => {
                this.fetchTimeline()
            }, 5000)
        },
    },
    beforeDestroy () {
        clearInterval(this.polling)
    },
}
</script>