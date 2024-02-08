<template>

    <div class="container" style=" max-width:100%">

        <el-row :gutter="20">

            <el-col :span="2">
                <div class="grid-content ep-bg-purple"/>

                <n-button round @click="" color="#6495ED">

                    <el-icon :size="17">
                        <Pointer/>
                    </el-icon>
                    &nbsp;下载
                </n-button>
            </el-col>

            <el-col :span="2">
                <div class="grid-content ep-bg-purple"/>

                <el-button @click="visible = true">
    定制列
  </el-button>
  <el-dialog v-model="visible" :show-close="false">
    <template #header="{ close, titleId, titleClass }">
      <div class="my-header">
        <h4 >选择需要展示的列</h4>


        <el-button type="" @click="close">
          <el-icon class="el-icon--left"><CircleCloseFilled /></el-icon>
          Close
        </el-button>
      </div>
    </template>
      <br>
       <el-checkbox v-model="showInstanceId">实例ID</el-checkbox>
        <el-checkbox v-model="showInstanceIp">实例IP</el-checkbox>
        <el-checkbox v-model="showInstanceName">实例名称</el-checkbox>

  </el-dialog>
            </el-col>

            <el-col :span="4">
                <div class="grid-content ep-bg-purple"/>

            </el-col>

            <el-col :span="10">
                <div class="grid-content ep-bg-purple"/>

                <div class="demo-date-picker">
                    <div class="block">
                        <!--      <p>Component value：{{ value }}</p>-->
                        选择查询时间：
                        <el-date-picker
                                v-model="value"
                                type="datetimerange"
                                start-placeholder="开始时间"
                                end-placeholder="结束时间"
                                :default-time="defaultTime"
                                format="YYYY-MM-DD HH:mm"
                        />
                        <!--                        <el-date-picker-->
                        <!--                                v-model="value"-->
                        <!--                                type="datetimerange"-->
                        <!--                                start-placeholder="开始时间"-->
                        <!--                                end-placeholder="结束时间"-->
                        <!--                                :default-time="defaultTime"-->
                        <!--                                format="YYYY-MM-DD HH:mm:ss"-->
                        <!--                        />-->
                    </div>
                </div>
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
        <p>时间value：{{ value }}</p>
        <el-table :data="currentPageData" stripe style="width: 100%; margin-top: 5px">
            <el-table-column v-if="showInstanceId" prop="instanceId" label="实例ID" width="180px"/>
            <el-table-column v-if="showInstanceId" prop="instanceName" label="实例名称" width="180px"/>

            <el-table-column v-if="showInstanceId" prop="cpuUtilization" label="CPU利用率(%)" width="120px"/>
            <el-table-column prop="memoryUtilization" label="内存利用率(%)" width="120px"/>
            <el-table-column prop="diskUtilization" label="磁盘利用率(%)" width="120px"/>
            <el-table-column prop="connectUtilization" label="连接利用率(%)" width="120px"/>
            <el-table-column prop="iopsUsage" label="IOPS使用率(%)" width="130px"/>
            <el-table-column prop="QPS" label="QPS" width="90px"/>
            <el-table-column prop="networkIncomingTraffic" label="网络入流量(%)" width="130px"/>
            <el-table-column prop="networkOutTraffic" label="网络出流量(%)" width="130"/>
            <el-table-column prop="mainBackupDelay" label="主备延迟" width="130px"/>
            <el-table-column prop="activeStandbySwitching" label="主备切换" width="180px"/>
            <el-table-column prop="numberOfTableLocks" label="表锁个数" width="180px"/>

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




        <br>
        <br>
        <div style="margin-top: 10px">
                <el-row :gutter="20" >
      <!-- 左侧列 -->
      <el-col :span="12">
        <div class="grid-content ep-bg-purple">
          <div class="chart-container" style="height: 300px">
            <div ref="chart1Ref" style="width: 100%; height: 100%;"></div>
          </div>
        </div>
      </el-col>
      <!-- 右侧列 -->
      <el-col :span="12">
        <div class="grid-content ep-bg-purple">
          <div class="chart-container" style="height: 300px">
            <div ref="chart2Ref" style="width: 100%; height: 100%;"></div>
          </div>
        </div>
      </el-col>

        <el-col :span="12">
        <div class="grid-content ep-bg-purple">
          <div class="chart-container" style="height: 300px">
            <div ref="chart3Ref" style="width: 100%; height: 100%;"></div>
          </div>
        </div>
      </el-col>
    </el-row>

        </div>




    </div>


</template>

<script lang="ts" setup>
import {ElDrawer, ElMessage} from 'element-plus'
import {Calendar, Search} from '@element-plus/icons-vue'
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

const value = ref([Date, Date])
const defaultTime = ref<[Date, Date]>([
    new Date(2000, 1, 1, 0, 0, 0),
    new Date(2000, 2, 1, 23, 59, 59),
])


const showInstanceId = ref(true)
const showInstanceIp = ref(true)
const showInstanceName = ref(true)


// 使用 onBeforeMount 钩子函数来替代 created 方法
onBeforeMount(() => {

    console.log('created 方法')
    axios.get('/api/db/rds/monitor/').then(response => {
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


import {defineComponent, onMounted, ref} from 'vue';
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


const chartOption1: ChartOption = {
    title: {
        text: 'CPU使用率趋势图',
        left: 'left',
        textStyle: {
            fontWeight: 'normal',
            fontSize: 16,
        },
    },
    legend: {
        data: ['实例1', '实例2', '实例3'],
        top: 50,
    },
    grid: {
        left: '5%',
        right: '5%',

    },
    tooltip: {
        trigger: 'axis',
    },
    xAxis: {
        type: 'category',
        boundaryGap: false,
        data: [
            '2021-1-1',
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
            name: '实例1',
            type: 'line',
            data: [20, 12, 12, 34, 90, 30, 10],
            smooth: true,
        },
        {
            name: '实例2',
            type: 'line',
            data: [22, 18, 91, 34, 90, 30, 31],
            smooth: true,
        },
        {
            name: '实例3',
            type: 'line',
            data: [50, 32, 20, 15, 19, 33, 41],
            smooth: true,
        },
    ],
};

const chartOption2: ChartOption = {
    title: {
        text: '数据库监控趋势图',
        left: 'left',
        textStyle: {
            fontWeight: 'normal',
            fontSize: 16,
        },
    },
    legend: {
        data: ['CPU使用率', '内存使用率', '磁盘使用率'],
        top: 50,
    },
    grid: {
        left: '5%',
        right: '5%',

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

const chartOption3: ChartOption = {
    title: {
        text: '数据库监控趋势图',
        left: 'left',
        textStyle: {
            fontWeight: 'normal',
            fontSize: 16,
        },
    },
    legend: {
        data: ['CPU使用率', '内存使用率', '磁盘使用率'],
        top: 50,
    },
    grid: {
        left: '5%',
        right: '5%',

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

const chart1Ref = ref(null);
const chart2Ref = ref(null);
const chart3Ref = ref(null);

onMounted(() => {
    const chart1 = echarts.init(chart1Ref.value);
    chart1.setOption(chartOption1);

    const chart2 = echarts.init(chart2Ref.value);
    chart2.setOption(chartOption2);

    const chart3 = echarts.init(chart3Ref.value);
    chart3.setOption(chartOption3);
});







import { ref } from 'vue'
import { ElButton, ElDialog } from 'element-plus'
import { CircleCloseFilled } from '@element-plus/icons-vue'

const visible = ref(false)


</script>

<style scoped>
.my-header {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
}
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