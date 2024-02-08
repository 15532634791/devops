<template>
    <div className="grid-content ep-bg-purple" id="OverviewOfGridOutboundCalls"></div>
</template>
<script>
import {onMounted, reactive} from "vue";
import * as echarts from "echarts";

export default {
    setup() {
        // 图标的参数信息 可查询官网看例子  或者可以直接复制官网的option过来直接展示
        let option = reactive( {
  legend: {},
  tooltip: {},
  dataset: {
    dimensions: ['product', '2015', '2016', '2017'],
    source: [
      { product: 'Matcha Latte', 2015: 43.3, 2016: 85.8, 2017: 93.7 },
      { product: 'Milk Tea', 2015: 83.1, 2016: 73.4, 2017: 55.1 },
      { product: 'Cheese Cocoa', 2015: 86.4, 2016: 65.2, 2017: 82.5 },
      { product: 'Walnut Brownie', 2015: 72.4, 2016: 53.9, 2017: 39.1 }
    ]
  },
  xAxis: { type: 'category' },
  yAxis: {},
  // Declare several bar series, each will be mapped
  // to a column of dataset.source by default.
  series: [{ type: 'bar' }, { type: 'bar' }, { type: 'bar' }]
}
            )
        ;
        onMounted(() => {
            // 接下来的使用，初始化图表，设置配置项
            let echartBox = document.getElementById("OverviewOfGridOutboundCalls");
            let myChart = echarts.init(echartBox);
            myChart.setOption(option);
            // 绑定事件 都是小写
            myChart.on("click", function (params) {
                // 控制台打印数据的名称
                console.log(params);
            });
        });
        return {};
    },
};
</script>