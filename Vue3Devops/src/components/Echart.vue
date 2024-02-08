<template>
  <div ref="chart" style="width: 100%; height: 100%;"></div>
</template>

<script>
import * as echarts from 'echarts';

export default {
  props: {
    option: {
      type: Object,
      default: () => ({}),
    },
  },
  mounted() {
    const chart = echarts.init(this.$refs.chart);
    chart.setOption(this.option);
  },
  watch: {
    option: {
      deep: true,
      handler(value) {
        const chart = echarts.init(this.$refs.chart);
        chart.setOption(value);
      }
    }
  },
  beforeDestroy() {
    echarts.dispose(this.$refs.chart);
  },
};
</script>
