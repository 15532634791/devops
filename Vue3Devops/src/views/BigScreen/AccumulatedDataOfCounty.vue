<template>
    <div className="grid-content ep-bg-purple" id="ProportionOfInternetQuality"></div>
</template>
<script>
import {onMounted, reactive} from "vue";
import * as echarts from "echarts";

export default {
    setup() {
        // 图标的参数信息 可查询官网看例子  或者可以直接复制官网的option过来直接展示
        let option = reactive({
                    tooltip: {
                        trigger: 'axis',
                        axisPointer: {
                            type: 'cross',
                            crossStyle: {
                                color: '#999'
                            }
                        }
                    },
                    toolbox: {
                        feature: {
                            dataView: {show: true, readOnly: false},
                            magicType: {show: true, type: ['line', 'bar']},
                            restore: {show: true},
                            saveAsImage: {show: true}
                        }
                    },
                    legend: {
                        data: ['Evaporation', 'Precipitation', 'Temperature']
                    },
                    xAxis: [
                        {
                            type: 'category',
                            data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
                            axisPointer: {
                                type: 'shadow'
                            }
                        }
                    ],
                    yAxis: [
                        {
                            type: 'value',
                            name: 'Precipitation',
                            min: 0,
                            max: 250,
                            interval: 50,
                            axisLabel: {
                                formatter: '{value} ml'
                            }
                        },
                        {
                            type: 'value',
                            name: 'Temperature',
                            min: 0,
                            max: 25,
                            interval: 5,
                            axisLabel: {
                                formatter: '{value} °C'
                            }
                        }
                    ],
                    series: [
                        {
                            name: 'Evaporation',
                            type: 'bar',
                            tooltip: {
                                valueFormatter: function (value) {
                                    return value + ' ml';
                                }
                            },
                            data: [
                                2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 135.6, 162.2, 32.6, 20.0, 6.4, 3.3
                            ]
                        },
                        {
                            name: 'Precipitation',
                            type: 'bar',
                            tooltip: {
                                valueFormatter: function (value) {
                                    return value + ' ml';
                                }
                            },
                            data: [
                                2.6, 5.9, 9.0, 26.4, 28.7, 70.7, 175.6, 182.2, 48.7, 18.8, 6.0, 2.3
                            ]
                        },
                        {
                            name: 'Temperature',
                            type: 'line',
                            yAxisIndex: 1,
                            tooltip: {
                                valueFormatter: function (value) {
                                    return value + ' °C';
                                }
                            },
                            data: [2.0, 2.2, 3.3, 4.5, 6.3, 10.2, 20.3, 23.4, 23.0, 16.5, 12.0, 6.2]
                        }
                    ]
                }
            )
        ;
        onMounted(() => {
            // 接下来的使用，初始化图表，设置配置项
            let echartBox = document.getElementById("ProportionOfInternetQuality");
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