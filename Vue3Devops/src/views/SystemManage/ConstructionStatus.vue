<template>
    <div className="line-chart-container">
        <div ref="lineChart" className="line-chart"></div>
    </div>
</template>

<script>
import {ref, onMounted} from 'vue';
import * as echarts from 'echarts';

export default {
    name: 'LineChart',
    setup() {
        const lineChart = ref(null);

        onMounted(() => {
            // 创建echarts实例
            const chart = echarts.init(lineChart.value);

            // 设置图表配置项和数据
            const options = {
                xAxis: {
                    type: 'category',
                    data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
                },
                yAxis: {
                    type: 'value'
                },
                series: [
                    {
                        type: 'line',
                        data: [120, 200, 150, 80, 70, 110, 130]
                    }
                ]
            };

            // 渲染图表
            chart.setOption(options);

            // 在窗口大小变化时重新渲染图表
            window.addEventListener('resize', () => {
                chart.resize();
            });
        });

        return {
            lineChart
        };
    }
}
</script>

<style>
.line-chart-container {
    width: 100%;
    height: 400px;
}

.line-chart {
    width: 100%;
    height: 100%;
}
</style>
