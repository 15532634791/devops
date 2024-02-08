<template>

    <div class="container" style=" max-width:100%">


        <el-row :gutter="20">

            <el-col :span="2">
                <div class="grid-content ep-bg-purple"/>


<!--                <el-button type="warning" >定制列展示</el-button>-->
                <el-link type="primary" disabled>定制列展示</el-link>
            </el-col>




            <el-col :span="12">
                <div class="grid-content ep-bg-purple"/>
                <el-checkbox v-model="showInstanceId">实例ID</el-checkbox>
                <el-checkbox v-model="showInstanceIp">实例IP</el-checkbox>
                <el-checkbox v-model="showInstanceName">实例名称</el-checkbox>

            </el-col>


            <el-col :span="5">
                <div class="grid-content ep-bg-purple"/>
                <el-input
                        v-model.trim="searchText"
                        placeholder="搜索实例id"
                        :prefix-icon="Search"
                        @input="handleSearch"
                        style="border-radius: 40px;"
                />

            </el-col>

            <el-col :span="2">
                <div class="grid-content ep-bg-purple"/>


                    <el-button type="primary">下载</el-button>



            </el-col>

        </el-row>


        <el-table
                :data="currentPageData"
                :default-sort="{ prop: 'creationTime', order: 'descending' }"
                style="width: 100%; margin-top: 5px"
        >

            <el-table-column v-if="showInstanceId" prop="instanceId" label="实例ID" width="190px"/>
            <el-table-column v-if="showInstanceIp" prop="instanceIp" label="实例IP" width="110px"/>
            <el-table-column v-if="showInstanceName" prop="instanceName" label="实例名称" width="180px"/>
            <el-table-column prop="port" label="端口号" width="90px"/>
            <el-table-column prop="cpu" label="CPU(核数)" width="110px"/>
            <el-table-column prop="diskSpace" label="磁盘空间(GB)" width="130px"/>
            <el-table-column prop="memory" label="内存" width="90px"/>
            <el-table-column prop="connectNumber" label="连接数" width="90px"/>
            <el-table-column prop="IOPS" label="IOPS" width="90px"/>
            <el-table-column label="内网地址" width="130">
                <template #default="scope">

                    <n-ellipsis  line-clamp="1">

                        <span >
                            {{ scope.row.internalNetworkAddress }}
                        </span>
                  </n-ellipsis>


<!--                    <div style="display: flex; align-items: center">-->

<!--                        <el-popover-->
<!--                                :width="300"-->
<!--                        >-->
<!--                            <template #reference>-->
<!--                                <el-button style="margin-right: 16px">内网地址</el-button>-->
<!--                            </template>-->

<!--                            <template #default>-->
<!--                                {{ scope.row.internalNetworkAddress }}-->
<!--                            </template>-->
<!--                        </el-popover>-->
<!--                    </div>-->

                </template>
            </el-table-column>
            <!--            <el-table-column prop="internalNetworkAddress" label="内网地址" width="396px"/>-->
            <el-table-column prop="organization" label="组织" width="130"/>
            <el-table-column prop="systemName" label="系统名称" width="130px"/>
            <el-table-column fixed="right" prop="creationTime" label="创建时间" width="180px" sortable/>

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

const showInstanceId = ref(true)
const showInstanceIp = ref(true)
const showInstanceName = ref(true)

// 使用 onBeforeMount 钩子函数来替代 created 方法
onBeforeMount(() => {
    console.log('created 方法')
    axios.get('/api/db/rds/resource/').then(response => {
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