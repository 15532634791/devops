<template>
    <div class="grid-content ep-bg-purple" id="ProportionOfDecorationServices"></div>
</template>
<script>
import {onMounted, reactive} from "vue";
import * as echarts from "echarts";

export default {
    setup() {
        // 图标的参数信息 可查询官网看例子  或者可以直接复制官网的option过来直接展示
        let option = reactive({
                    title: {
                        text: 'World Population'
                    },
                    tooltip: {
                        trigger: 'axis',
                        axisPointer: {
                            type: 'shadow'
                        }
                    },
                    legend: {},
                    grid: {
                        left: '3%',
                        right: '4%',
                        bottom: '3%',
                        containLabel: true
                    },
                    xAxis: {
                        type: 'value',
                        boundaryGap: [0, 0.01]
                    },
                    yAxis: {
                        type: 'category',
                        data: ['Brazil', 'Indonesia', 'USA', 'India', 'China', 'World']
                    },
                    series: [
                        {
                            name: '2011',
                            type: 'bar',
                            data: [18203, 23489, 29034, 104970, 131744, 630230]
                        },
                        {
                            name: '2012',
                            type: 'bar',
                            data: [19325, 23438, 31000, 121594, 134141, 681807]
                        }
                    ]
                }
            )
        ;
        onMounted(() => {
            // 接下来的使用，初始化图表，设置配置项
            let echartBox = document.getElementById("ProportionOfDecorationServices");
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