<template>

    <div class="container" style=" max-width:100%">


        <el-row :gutter="20">

            <el-col :span="2">
                <div class="grid-content ep-bg-purple"/>

                <n-button round @click="newNamespace" color="#6495ED">

                    <el-icon :size="17">
                        <Pointer/>
                    </el-icon>
                    &nbsp;新 建
                </n-button>
            </el-col>


            <el-col :span="15">
                <div class="grid-content ep-bg-purple"/>

                <n-button round @click="syncData" color="#6495ED">

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
                        placeholder="搜索构建名称"
                        :prefix-icon="Search"
                        @input="handleSearch"
                        style="border-radius: 40px;"
                />

            </el-col>

        </el-row>

        <div>
            <!--抽屉框-->
            <el-drawer

                    v-model="dialogNamespace"
                    title="创建命名空间"
                    :before-close="handleCloseNamespace"
                    size="70%"
                    class="demo-drawer"
            >
                <div class="demo-drawer__content">

                    <el-form label-width="220px">
                        <p>
                            <el-text size="large">组织</el-text>
                        </p>
                        <el-tree-select
                                v-model="form_data.org_value"
                                :data="org_list"
                                check-strictly
                                @change="treeSelect"
                                :render-after-expand="false"
                                style="width: 80%; "
                                placeholder="请选择组织"

                        />
                        <br>
                        <p style="margin-top: 10px">
                            <el-text size="large">资源集</el-text>
                        </p>
                        <el-select v-model="form_data.resource_set_value" placeholder="请选择资源集合"
                                   style="width: 80%; ">
                            <el-option
                                    v-for="item in resource_set_list"
                                    :key="item.value"
                                    :label="item.label"
                                    :value="item.value"
                            />
                        </el-select>

                        <p style="margin-top: 10px">
                            <el-text size="large">地域</el-text>
                        </p>
                        <el-select v-model="form_data.region_value" placeholder="请选择地域"
                                   style="width: 80%">
                            <el-option
                                    v-for="item in region_list"
                                    :key="item.value"
                                    :label="item.label"
                                    :value="item.value"
                            />
                        </el-select>

                        <p style="margin-top: 10px">
                            <el-text>命名空间</el-text>
                        </p>
                        <el-input v-model="form_data.namespace_value" placeholder="命名空间"
                                  style="width: 80%; " required/>

                    </el-form>


                    <div class="demo-drawer__footer" style="margin-top: 10px">
                        <el-button @click="cancelFormNamespace">取消</el-button>
                        <el-button type="primary" @click="onClickNamespace">提交</el-button>
                    </div>
                </div>
            </el-drawer>
        </div>

        <el-table :data="currentPageData" stripe style="width: 100%; margin-top: 5px">
            <el-table-column fixed="left" prop="namespaceName" label="命名空间" width="220"/>
<!--            <el-table-column fixed="left" prop="region" label="地域" width="100"/>-->
            <el-table-column  label="地域" width="100">
                <template #default="scope">
                    jibei-1
                </template>
            </el-table-column>
            <el-table-column prop="authorizeType" label="权限"/>
            <el-table-column prop="namespaceStatus" label="命名空间状态" width="120"/>
            <el-table-column prop="autoCreate" label="自动创建仓库" width="200">
                 <template #default="scope">
                   <el-switch
                            v-model="scope.row.autoCreate"
                            inline-prompt
                            active-text="是"
                            inactive-text="否"
                            style="--el-switch-on-color: #13ce66; --el-switch-off-color: #545c64;width: 2.5em; height: 2.5em; margin-right: 8px;"
                            @click="changePermisson"
                    />
                </template>
            </el-table-column>
            <el-table-column prop="defaultVisibility" label="默认仓库类型" width="150"/>
            <el-table-column prop="DepartmentName" label="组织" width="230"/>
            <el-table-column prop="ResourceGroupName" label="资源集" width="330"/>
            <el-table-column fixed="right" label="操作" width="120">
                <template #default="scope">
                    <el-popconfirm
                            confirm-button-text="确定"
                            cancel-button-text="取消"
                            icon-color="#626AEF"
                            title="确定删除吗？"
                            @confirm="confirmEvent"
                            @cancel="cancelEvent"
                    >
                        <template #reference>
                            <el-button text style="border: none !important;">
                                <Delete
                                        style="width: 1.5em; height: 1.5em; color: black"/>

                            </el-button>
                        </template>
                    </el-popconfirm>

                    <!--                    <el-popover-->
                    <!--                            placement="left"-->
                    <!--                            :width="800"-->
                    <!--                            trigger="click"-->
                    <!--                            :content=scope.row.jarBuildImageAddress-->
                    <!--                    >-->
                    <!--                        <template #reference>-->
                    <!--                            <el-button class="m-2" type="primary" text>-->
                    <!--                                <el-icon :size="20"><Promotion /></el-icon>-->
                    <!--                            </el-button>-->
                    <!--                        </template>-->
                    <!--                    </el-popover>-->
                </template>
            </el-table-column>

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

const dialogNamespace = ref(false)

const form_data = ref(
    {
        org_value: '',
        resource_set_value: '',
        region_value: '',
        namespace_value: '',
    }
)

const org_list = ref([
    {
        value: '160',
        label: '国网冀北电力有限公司',
        children: [
            {
                value: '1-1',
                label: '研发测试平台',
                children: [
                    {
                        value: '1-1-1',
                        label: '云平台',
                    },
                ],
            },
            {
                value: '1-1',
                label: '发展策划部',
            },
            {
                value: '1-1',
                label: '财务部',
            },
            {
                value: '1-1',
                label: '安监部、保卫部',
            },
            {
                value: '1-1',
                label: '设备管理部',
            },
        ],
    },

])

const region_list = ref([
    {
        value: 'jibei-1',
        label: 'jibei-1',
    },
])

const resource_set_list = ref([
    {
        value: '191',
        label: 'DefaultResourceSet(国网冀北电力)',
    },

])


// 使用 onBeforeMount 钩子函数来替代 created 方法
onBeforeMount(() => {
    console.log('created 方法')
    axios.get('http://25.42.38.89:8000/project/manage/namespace/detail/').then(response => {
        console.log(response.data);
        dataList.value = response.data.reverse()

    }).catch(error => {
        console.log(error);
    })
});


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

const newNamespace = () => {
    dialogNamespace.value = true;

    form_data.value =
    {
        org_value: '',
        resource_set_value: '',
        region_value: '',
        namespace_value: '',
    }

    console.log(
        form_data.value
    );
}

// 根据搜索文本过滤数据
const filteredData = computed(() => {
    if (searchText.value === '') {
        return dataList.value;
    } else {
        return dataList.value.filter(item => item.namespaceName.includes(searchText.value));
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


const onClickNamespace = () => {
    dialogNamespace.value = false
    console.log(
        form_data.value
    );
    axios.post('http://25.42.38.89:8000/project/manage/namespace/list/', form_data.value).then(response => {
                console.log(response.data);
                // if (response.data.status === 'success'){
                //     ElMessage({
                //         message: '创建完成',
                //         type: 'success',
                //     });
                // }

            }).catch(error => {
                console.log(error);
            })

            ElMessage({
                message: '创建命名空间请求已发送',
                type: 'success',
            });
}

const handleCloseNamespace = (done) => {
    dialogNamespace.value = false
}

const cancelFormNamespace = () => {
    dialogNamespace.value = false

}


const syncData = () => {
    ElMessage({
        message: '数据同步请求已发送',
        type: 'success',
    })
    axios.get('http://25.42.38.89:8000/project/manage/namespace/sync/').then(response => {
        console.log(response.data);

        ElMessage({
            message: '数据同步已完成',
            type: 'success',
        })


    }).catch(error => {
        console.log(error);
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