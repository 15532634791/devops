<template>
    <div className="grid-content ep-bg-purple" id="mychart"></div>
</template>

<script>
import {onMounted, reactive} from "vue";
import * as echarts from "echarts";

export default {
    setup() {
        let option = reactive({
            title: {
                text: "装维满意度占比（整体）",
                subtext: "实时",
                left: "right"
            },
            tooltip: {
                trigger: "item",
                formatter: "{a} <br/>{b}: {c} ({d}%)"
            },
            legend: {
                orient: "vertical",
                left: "left"
            },
            series: [
                {
                    name: "满意度",
                    type: "pie",
                    radius: "50%",
                    data: [
                        {value: 1048, name: "10分"},
                        {value: 735, name: "7-9分"},
                        {value: 580, name: "1-6分"},
                        {value: 484, name: "其他"}
                    ],
                    emphasis: {
                        itemStyle: {
                            shadowBlur: 10,
                            shadowOffsetX: 0,
                            shadowColor: "rgba(0, 0, 0, 0.5)"
                        }
                    },
                    label: {
                        formatter: "{b}: {d}%"
                    }
                }
            ]
        });

        onMounted(() => {
            let echartBox = document.getElementById("mychart");
            let myChart = echarts.init(echartBox);
            myChart.setOption(option);
            myChart.on("click", function (params) {
                console.log(params);
            });
        });

        return {};
    }
};
</script>