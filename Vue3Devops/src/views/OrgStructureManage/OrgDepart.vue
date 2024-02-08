<template>

    <div class="container" style=" max-width:100%">


        <el-row :gutter="20">

            <el-col :span="2">
                <div class="grid-content ep-bg-purple"/>

                <n-button round @click="dialog = true" color="#6495ED">

                    <el-icon :size="17">
                        <Pointer/>
                    </el-icon>
                    &nbsp;新 建
                </n-button>
            </el-col>


            <el-col :span="15">
                <div class="grid-content ep-bg-purple"/>

                <n-button round @click="syncImageData" color="#6495ED">

                    <el-icon :size="17">
                        <Refresh/>
                    </el-icon>
                    &nbsp;数据同步
                </n-button>
            </el-col>


            <el-col :span="6">
                <div class="grid-content ep-bg-purple"/>
                <el-input
                        v-model.trim="searchText"
                        placeholder="搜索仓库名称"
                        :prefix-icon="Search"
                        @input="handleSearch"
                        style="border-radius: 40px;"
                />

            </el-col>


        </el-row>


        <el-drawer
                v-model="dialog"
                :title="title"
                :before-close="handleClose"
                direction="rtl"
                class="demo-drawer"
                size="70%"
                :with-header="false"

        >
            <div class="demo-drawer__content" style="justify-content: center;">


            </div>
        </el-drawer>


        <el-table :data="currentPageData" stripe style="width: 100%; margin-top: 5px">
            <el-table-column fixed="left" prop="repoName" label="仓库名称" width="300"/>
            <el-table-column prop="repoNamespace" label="命名空间" width="300"/>
            <el-table-column prop="repoStatus" label="仓库状态" width="100"/>
            <el-table-column prop="repoType" label="类型" width="100"/>
            <el-table-column prop="repoAuthorizeType" label="权限" width="100"/>
            <el-table-column prop="gmtModified" label="创建时间" width="180"/>
            <el-table-column prop="repoUrl" label="仓库地址" width="750"/>
            <el-table-column fixed="right" label="操作" width="150">
                <template #default="scope">
                    <el-button type="primary" text
                               @click="handleClickTableDetail(scope.row.repoName, scope.row.repoNamespace)">

                        <el-icon :size="20">
                            <Search/>
                        </el-icon>

                    </el-button>

                    <el-popconfirm
                            confirm-button-text="确定"
                            cancel-button-text="取消"
                            icon-color="#626AEF"
                            title="确定删除吗？"
                            @confirm="confirmEvent"
                            @cancel="cancelEvent"
                    >
                        <template #reference>
                            <el-button text type="primary" style="border: none !important;">
                                <el-icon :size="20">
                                    <Delete/>
                                </el-icon>


                            </el-button>
                        </template>
                    </el-popconfirm>
                </template>
            </el-table-column>


        </el-table>

        <el-dialog v-model="dialogVisibleDetailForImage" title="命令输出详情" width="80%">
            <table class="table  table-hover  " style="margin-top: 10px">
                <thead>
                <tr>

                    <th scope="col" style="text-align: left;"> 镜像版本</th>
                    <th scope="col" style="text-align: left;"> 镜像大小</th>
                    <th scope="col" style="text-align: center;"> 镜像创建时间</th>
                    <th scope="col" style="text-align: center;"> 镜像更新时间</th>
                    <th scope="col" style="text-align: center;"> 镜像id</th>
                    <th scope="col" style="text-align: center;"> 镜像digest</th>
                    <th scope="col" style="text-align: center;"> 镜像状态</th>
                    <th scope="col" style="text-align: center;"> 操作</th>
                </tr>
                </thead>
                <tbody>

                <tr v-for="item in imageInfo" :key="item.id">

                    <td style="text-align: left;"> {{ item.tag }}</td>
                    <td style="text-align: left;">{{ item.imageSize }}</td>
                    <td style="text-align: center;"> {{ item.imageCreate }}</td>
                    <td style="text-align: center;"> {{ item.imageUpdate }}</td>
                    <td style="text-align: center;">

                        <el-tooltip
                                class="box-item"
                                effect="dark"
                                placement="top"
                        >
                            <template #content>
                                <a
                                        :href="item.imageId"
                                        target="_blank"
                                        @click.prevent="copyToClipboard(item.imageId)"
                                        style="text-decoration: none; font-size: 20px; color: #b6d4fe"
                                >
                                    {{ item.imageId }}
                                </a>
                            </template>
                            <el-button style="width: 2em; height: 2em; border: none !important;color: black">
                                <el-icon>
                                    <Key/>
                                </el-icon>
                            </el-button>
                        </el-tooltip>

                    </td>
                    <td style="text-align: center;">


                        <el-tooltip
                                class="box-item"
                                effect="dark"
                                placement="top"
                        >
                            <template #content>
                                <a
                                        :href="item.digest"
                                        target="_blank"
                                        @click.prevent="copyToClipboard(item.digest)"
                                        style="text-decoration: none; font-size: 20px; color: #b6d4fe"
                                >
                                    {{ item.digest }}
                                </a>
                            </template>
                            <el-button style="width: 2em; height: 2em; border: none !important;color: black">
                                <el-icon>
                                    <Key/>
                                </el-icon>
                            </el-button>
                        </el-tooltip>


                    </td>
                    <td style="text-align: center;"> {{ item.status }}</td>
                    <td style="text-align: center;">
                        <div style="white-space: nowrap;">

                            <el-popconfirm title="要删除此镜像吗？">
                                <template #reference>
                                    <el-button style="border: none !important;" @click="deleteItem(item.id12)">
                                        <Delete
                                                style="width: 1.5em; height: 1.5em; color: black"/>

                                    </el-button>
                                </template>
                            </el-popconfirm>


                        </div>
                    </td>
                </tr>


                </tbody>
            </table>
        </el-dialog>

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
import {ref} from 'vue'
import {Calendar, Search} from '@element-plus/icons-vue'

const dialogVisibleDetailForImage = ref(false)

const dialogVisibleDetail = ref(false)
const handleCloseDetail = (done: () => void) => {
    dialogVisibleDetail.value = false

}
import {UploadFilled} from '@element-plus/icons-vue'
import {ElMessage} from 'element-plus'
import {ref, computed, onBeforeMount} from 'vue';
import {ElPagination} from 'element-plus';
import type {UploadInstance} from 'element-plus';
import {ElMessageBox} from 'element-plus'
import axios from "axios";

const total = ref(15)
const dialog = ref(false)
const loading = ref(false)
const title = ref('填写构建信息')

const dataList = ref([])

const pageSize = ref(10);          // 每页显示的数据数量
const currentPage = ref(1);       // 当前页码
const searchText = ref('');       // 搜索文本

const imageInfo = ref([{
    imageUpdate: '',
    imageId: '',
    digest: '',
    tag: '',
    imageSize: '',
    imageCreate: '',
    status: '',
}])


// 使用 onBeforeMount 钩子函数来替代 created 方法
onBeforeMount(() => {
    console.log('created 方法')
    axios.get('http://25.42.38.89:8000/project/manage/image/list/').then(response => {
        console.log(response.data);
        dataList.value = response.data.reverse()

    }).catch(error => {
        console.log(error);
    })
});


const handleClose = () => {
    dialog.value = false
    if (dialog.value) {
        return
    }
}

const syncImageData = () => {
    ElMessage({
        message: '数据同步请求已发送',
        type: 'success',
    })

    axios.get('http://25.42.38.89:8000/project/manage/image/sync/').then(response => {
        console.log(response.data);

        ElMessage({
            message: '数据同步已完成',
            type: 'success',
        })


    }).catch(error => {
        console.log(error);
    })
}


// 根据搜索文本过滤数据
const filteredData = computed(() => {
    if (searchText.value === '') {
        return dataList.value;
    } else {
        return dataList.value.filter(item => item.repoName.includes(searchText.value));
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


const handleClickTableDetail = (RepoName, RepoNamespace) => {
    dialogVisibleDetailForImage.value = true

    imageInfo.value = [
        {
            imageUpdate: '',
            imageId: '',
            digest: '',
            tag: '',
            imageSize: '',
            imageCreate: '',
            status: '',
        }
    ]

    console.log(RepoName, RepoNamespace)
    axios.get('http://25.42.38.89:8000/project/manage/image/tags/?RepoName=' + RepoName + '&RepoNamespace=' + RepoNamespace).then(response => {
        console.log(response.data);
        imageInfo.value = response.data

    }).catch(error => {
        console.log(error);
    })

};

const confirmEvent = () => {
    console.log('confirm!')
    ElMessage({
            message: '删除成功',
            type: 'success',
        }
    )
}


const cancelEvent = () => {
    console.log('cancel!')
    ElMessage({
        message: '取消删除',
        type: 'warning',
    })
}
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