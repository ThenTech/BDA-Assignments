<template>
  <div id="app">
    <el-row>
      <el-col :span="18" :offset="3" class="m-t-20">
        <timeline-graph></timeline-graph>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import TimelineGraph from './components/TimelineGraph.vue'

// TODO Add selector for tenant

export default {
  name: 'app',
  components: {
    TimelineGraph
  },
}
</script>

<style>
  * {
    margin: 0;
    padding: 0;
    font-family: "Helvetica Neue", Helvetica, "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", "微软雅黑", Arial, sans-serif;
  }

  .m-t-20 {
    margin-top: 100px;
  }
</style>
