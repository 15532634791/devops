<template>

    <div class="container" style=" max-width:100%">


        <el-row :gutter="20">

            <el-col :span="2">
                <div class="grid-content ep-bg-purple"/>


            </el-col>


            <el-col :span="15">

            </el-col>


            <el-col :span="6">
                <div class="grid-content ep-bg-purple"/>
                <el-input
                        v-model.trim="searchText"
                        placeholder="搜索实例id"
                        :prefix-icon="Search"
                        @input="handleSearch"
                        style="border-radius: 40px;"
                />

            </el-col>

        </el-row>


        <el-table :data="currentPageData" stripe style="width: 100%; margin-top: 5px">
            <el-table-column prop="instanceId" label="实例ID" width="180px"/>
            <el-table-column prop="account" label="账号"/>
            <el-table-column prop="instanceType" label="类型"/>
            <el-table-column prop="instanceStatus" label="状态"/>
            <el-table-column prop="affiliation" label="所属"/>
            <el-table-column prop="affiliationData" label="所属数据"/>
            <el-table-column prop="accountDescription" label="账号描述"/>
            <el-table-column prop="characterSet" label="字符集"/>
            <el-table-column prop="created_by" label="所属者ID"/>
<!--            <el-table-column fixed="right" label="测试列" width="110">-->
<!--                <template #default="scope">-->


<!--                    <div style="display: flex; align-items: center">-->

<!--                        <el-popover-->
<!--                                :width="300"-->
<!--                        >-->
<!--                            <template #reference>-->
<!--                                <el-button style="margin-right: 16px">实例id</el-button>-->
<!--                            </template>-->

<!--                            <template #default>-->
<!--                                {{ scope.row.characterSet }}-->
<!--                            </template>-->
<!--                        </el-popover>-->
<!--                    </div>-->

<!--                </template>-->
<!--            </el-table-column>-->

        </el-table>


        <el-pagination
                :page-sizes="[10, 20, 30, 40, 50]"
                :page-size="pageSize"
                :current-page.sync="currentPage"
                layout="total,sizes,prev,pager,next,jumper"
                :total="filteredData.length"
                @size-change="handleSizeChange"
                @current-change="handleCurrentChange"
                style="margin: 10px"
        ></el-pagination>





               <div className="trend-chart">
                <div className="chart-container" style="height: 300px">
                    <div ref="chartRef" style="width: 100%; height: 100%;"></div>
                </div>
            </div>





    </div>


</template>

<script lang="ts" setup>
import {Search} from '@element-plus/icons-vue'
import {ref, computed, onBeforeMount} from 'vue';
import {ElPagination} from 'element-plus';
import axios from "axios";

const total = ref(15)
const dialog = ref(false)
const title = ref('填写构建信息')
const dataList = ref([])
const pageSize = ref(10);          // 每页显示的数据数量
const currentPage = ref(1);       // 当前页码
const searchText = ref('');       // 搜索文本


// 使用 onBeforeMount 钩子函数来替代 created 方法
onBeforeMount(() => {
    console.log('created 方法')
    const BearerToken = localStorage.getItem('token')
    console.log(BearerToken)
    axios.get('/api/db/rds/instance/',{
      headers: {
        'Authorization': 'Bearer ' + BearerToken  // 替换为您的 token
      }
    }).then(response => {
        console.log(response.data);
        dataList.value = response.data.reverse()

    }).catch(error => {
        console.log(error);
    })
});


// 根据搜索文本过滤数据
const filteredData = computed(() => {
    if (searchText.value === '') {
        return dataList.value;
    } else {
        return dataList.value.filter(item => item.instanceId.includes(searchText.value));
    }
});

// 根据当前页码和每页显示的数据数量计算出过滤后的数据数组
const currentPageData = computed(() => {
    const startIndex = (currentPage.value - 1) * pageSize.value;
    return filteredData.value.slice(startIndex, startIndex + pageSize.value);
});

// 监听每页显示的数据数量变化
const handleSizeChange = (val: number) => {
    pageSize.value = val;
    currentPage.value = 1;   // 重置为第一页
};

// 监听当前页码变化
const handleCurrentChange = (val: number) => {
    currentPage.value = val;
};

// 处理搜索输入事件
const handleSearch = () => {
    currentPage.value = 1;   // 搜索时重置为第一页
};



import {onMounted, ref} from 'vue';
import * as echarts from 'echarts';

interface ChartOption {
    title: {
        text: string;
        left: string;
        textStyle: {
            fontWeight: string;
            fontSize: number;
        };
    };
    legend: {
        data: string[];
        top: number;
    };
    tooltip: {
        trigger: string;
    };
    xAxis: {
        type: string;
        boundaryGap: boolean;
        data: string[];
    };
    yAxis: {
        type: string;
        splitNumber: number;
    };
    series: {
        name: string;
        type: string;
        data: number[];
        smooth: boolean;
    }[];
}
const chartOption: ChartOption = {
            title: {
                text: '数据库监控趋势图',
                left: 'center',
                textStyle: {
                    fontWeight: 'normal',
                    fontSize: 34,
                },
            },
            legend: {
                data: ['CPU使用率', '内存使用率', '磁盘使用率'],
                top: 50,
            },
            tooltip: {
                trigger: 'axis',
            },
            xAxis: {
                type: 'category',
                boundaryGap: false,
                data: [
                    '2021/1/1',
                    '2021/1/2',
                    '2021/1/3',
                    '2021/1/4',
                    '2021/1/5',
                    '2021/1/6',
                    '2021/1/7',
                ],
            },
            yAxis: {
                type: 'value',
                splitNumber: 4,
            },
            series: [
                {
                    name: 'CPU使用率',
                    type: 'line',
                    data: [120, 132, 101, 134, 90, 230, 210],
                    smooth: true,
                },
                {
                    name: '内存使用率',
                    type: 'line',
                    data: [220, 182, 191, 234, 290, 330, 310],
                    smooth: true,
                },
                {
                    name: '磁盘使用率',
                    type: 'line',
                    data: [150, 232, 201, 154, 190, 330, 410],
                    smooth: true,
                },
            ],
        };

const chartRef = ref(null);

onMounted(() => {
    const chart = echarts.init(chartRef.value);
    chart.setOption(chartOption);
});







</script>

<style scoped>
.dialog-footer button:first-child {
    margin-right: 10px;
}

.my-message-box .el-message-box__header {
    background-color: #3498db;
    color: white;
}

.my-message-box .el-message-box__content {
    font-size: 16px;
}

.el-row {
    margin-bottom: 20px;
}

.el-row:last-child {
    margin-bottom: 0;
}

.el-col {
    border-radius: 4px;
}

.grid-content {
    border-radius: 4px;
    min-height: 36px;
}
</style>