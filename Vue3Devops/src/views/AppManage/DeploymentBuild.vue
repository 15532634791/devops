<template>

    <div class="container" style=" max-width:100%">


        <el-row :gutter="20">

            <el-col :span="17">
                <div class="grid-content ep-bg-purple"/>

                <n-button round @click="dialog = true" color="#6495ED">

                    <el-icon><CirclePlus /></el-icon>
                    &nbsp;&nbsp;新 建&nbsp;&nbsp;
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


        <el-drawer
                v-model="dialog"
                :title="title"
                :before-close="handleClose"
                direction="rtl"
                class="demo-drawer"
                size="65%"
                :with-header="false"

        >
            <div class="demo-drawer__content" style="justify-content: center;">


                <el-button :round="false"
                           :style="{ background:  urlButtonColor, color: font_color, width: button_width,marginRight: button_right, borderRadius: 0, border: button_border, marginTop: '10px', height: '37px'}"
                           @click="showJar"> JAR构建
                </el-button>
                <el-button :round="false"
                           :style="{ background:  jarButtonColor, color: font_color, width: button_width,marginLeft: button_right,borderRadius: 0, border: button_border, marginTop: '10px', height: '37px'}"
                           @click="showUrl"> URL构建
                </el-button>


                <div v-if="jar_div" style="margin-top: 10px;padding-top: 10px">

                    <form @submit.prevent="submitForm">
                        <div style="margin: 10px; border: #0b2e13">
                            <form className="row g-4">
                                <div className="col-10">

                                    <label for=""> <b><span style="color: red">*</span> 构建名称 </b></label>
                                    <input type="text" className="form-control" id="inputAddress"
                                           placeholder="请输入构建名称" v-model="jarBuildName"
                                           @change="methodGetBuildName(jarBuildName)" required>
                                </div>


                                <div className="col-10">

                                    <label for=""> <b> <span style="color: red">*</span>命名空间</b></label>
                                    <div class="input-group mb-3">
                                        <span class="input-group-text" id="basic-addon3">cr.registry.jibei-1.res.sgmc.com.cn/</span>
                                        <input type="text" class="form-control" id="basic-url"
                                               placeholder="填写命名空间后可以选择镜像仓库"
                                               aria-describedby="basic-addon3" v-model="jarBuildNameSpace"
                                               @change="methodGetRepoByNamespace(jarBuildNameSpace)" required>
                                    </div>


                                </div>
                                <div className="col-5">

                                    <label for=""> <b> <span style="color: red">*</span>镜像仓库</b></label>
                                    <select class="form-select" aria-label="Default select example"
                                            v-model="jarBuildRepo" @change="clickUpload">
                                        <option v-for="option in getRepoListByNamespace" :value="option.value"
                                                :key="option.value">
                                            {{ option.label }}
                                        </option>
                                    </select>

                                </div>

                                <div className="col-5">

                                    <label for=""> <b> <span style="color: red">*</span>镜像版本</b></label>
                                    <input type="text" className="form-control" id="inputAddress"
                                           placeholder="请输入镜像版本号" v-model="jarBuildVersion"
                                           @change="clickUpload" required>

                                </div>

                                <div className="col-10" @click="clickUpload">
                                    <label for=""> <b> <span style="color: red">*</span>上传Jar包及Dockerfile
                                    </b></label>

                                    <el-upload
                                            ref="uploadRef"
                                            class="upload-demo"
                                            drag
                                            :action="uploadAddress"
                                            multiple
                                            :auto-upload="true"
                                            :before-upload="handleBeforeUpload"
                                            :on-success="fileUploadSuccess"
                                            :disabled="uploadDisabled"
                                    >
                                        <el-icon class="el-icon--upload">
                                            <upload-filled/>
                                        </el-icon>
                                        <div class="el-upload__text">
                                            双击<em>上传</em>
                                        </div>

                                    </el-upload>


                                </div>


                                <div className="col-10">

                                    <label for=""> <b> 构建脚本</b></label>
                                    <textarea className="form-control" style="height: 100px" name="description"
                                              placeholder="echo 'JAR'" v-model="jarBuildCommand"></textarea>

                                </div>

                            </form>
                        </div>


                    </form>


                </div>

                <div v-else-if="url_div" style="margin-top: 10px;padding-top: 10px;">
                    <form @submit.prevent="submitForm">
                        <div style="margin: 10px; border: #0b2e13">
                            <form className="row g-4">


                                <div className="col-5">

                                    <label for=""> <b><span style="color: red">*</span> 构建名称（不可以出现连续五个下划线:
                                        _____） </b></label>
                                    <input type="text" className="form-control" id="inputAddress"
                                           placeholder="请输入构建名称">
                                </div>

                                <div className="col-5">

                                    <label for=""> <b><span style="color: red">*</span>文件URL</b></label>
                                    <input type="text" className="form-control" id="inputAddress"
                                           placeholder="请输入文件URL">

                                </div>


                                <div className="col-5">

                                    <label for=""> <b>分支</b></label>
                                    <input type="text" className="form-control" id="inputAddress"
                                           placeholder="./*master">

                                </div>

                                <div className="col-5">

                                    <label for=""> <b> <span style="color: red">*</span>镜像名称</b></label>
                                    <input type="text" className="form-control" id="inputAddress"
                                           placeholder="请输入镜像名称">
                                </div>

                                <div className="col-5">

                                    <label for=""> <b> <span style="color: red">*</span>镜像版本</b></label>
                                    <input type="text" className="form-control" id="inputAddress"
                                           placeholder="请输入镜像版本号">

                                </div>

                                <div className="col-5">

                                    <label for=""> <b> <span style="color: red">*</span>构建参数</b></label>
                                    <input type="text" className="form-control" id="inputAddress"
                                           placeholder="">

                                </div>

                                <div className="col-10">
                                    <label for=""> <b> <span style="color: red">*</span>上传Dockerfile</b></label>
                                    <el-upload
                                            class="upload-demo"
                                            drag
                                            action="https://run.mocky.io/v3/9d059bf9-4660-45f2-925d-ce80ad6c4d15"
                                            multiple

                                    >
                                        <el-icon class="el-icon--upload">
                                            <upload-filled/>
                                        </el-icon>
                                        <div class="el-upload__text">
                                            将Dockerfile拖动到此处 <em>或者点击上传</em>
                                        </div>
                                        <template #tip>
                                            <div class="el-upload__tip">
                                                上传Dockerfile
                                            </div>
                                        </template>
                                    </el-upload>


                                </div>


                                <div className="col-10">

                                    <label for=""> <b> 构建脚本</b></label>
                                    <textarea className="form-control" style="height: 100px" name="description"
                                              placeholder="echo 'URL'"></textarea>

                                </div>


                            </form>
                        </div>


                    </form>

                </div>


                <div class="demo-drawer__footer" style="padding-left: 35%;margin-top: 10px;padding-top: 10px">
                    <el-button type="primary" :loading="loading" @click="onClick">{{
                        loading ? '提交中 ...' : '提交'
                        }}
                    </el-button>
                    <el-button @click="cancelForm">取消</el-button>

                </div>
            </div>
        </el-drawer>


        <el-table :data="currentPageData" stripe style="width: 100%; margin-top: 5px">
            <el-table-column fixed="left" prop="jarBuildName" label="构建名称" width="300"/>
            <el-table-column prop="jarBuildNameSpace" label="命名空间" width="300"/>
            <el-table-column prop="jarBuildRepo" label="镜像仓库" width="300"/>
            <el-table-column prop="jarBuildVersion" label="构建版本" width="250"/>
            <el-table-column prop="jarBuildUser" label="构建人"/>
            <el-table-column prop="jarBuildTime" label="创建时间" width="180"/>
            <el-table-column prop="jarBuildImageAddress" label="镜像地址" width="750"/>

            <el-table-column fixed="right" prop="jarBuildStatus" label="构建状态" width="80"/>
            <el-table-column fixed="right" label="命令输出详情" width="110">
                <template #default="scope">
                    <el-button type="primary" text @click="handleClickTableDetail(scope.row.jarBuildCommandStdout)">
                        <el-icon :size="20"><InfoFilled /></el-icon>
                    </el-button>
                </template>
            </el-table-column>

            <el-table-column fixed="right" label="操作" width="80">
                <template #default="scope">
                    <el-button type="primary" text @click="handleClickTableDetail(scope.row.jarBuildCommand)">
                        <el-icon :size="20">
                            <Edit/>
                        </el-icon>
                    </el-button>
                </template>
            </el-table-column>
        </el-table>

        <el-dialog v-model="dialogVisibleDetailForCommand" title="命令输出详情" width="70%">
            <xmp>
                {{ dialogVisibleDetailForCommandStdout }}
            </xmp>

            <template #footer>
              <span class="dialog-footer">

                <el-button type="primary" @click="dialogVisibleDetailForCommand = false">
                  确定
                </el-button>
              </span>
            </template>
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

const dialogVisibleDetailForCommand = ref(false)

const visibleDetails = ref(false)
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

const uploadRef = ref<UploadInstance>()
const total = ref(15)
const dialog = ref(false)
const loading = ref(false)
const title = ref('填写构建信息')
const jar_div = ref(true)
const url_div = ref(false)
const urlButtonColor = ref('#6495ED')
const jarButtonColor = ref('#BEBEBE')
const font_color = ref('black')
const button_width = ref('42%')
const button_right = ref('0px')
const button_border = ref('none')
const dataList = ref([])
const jarBuildName = ref('')
const jarBuildNameSpace = ref('')
const jarBuildRepo = ref('')
const jarBuildVersion = ref('')
const jarBuildCommand = ref('')
const jarBuildCommandStdout = ref('')
const uploadDisabled = ref(true)
const uploadAddress = ref('http://127.0.0.1:8001/project/build/upload/')
const pageSize = ref(10);          // 每页显示的数据数量
const currentPage = ref(1);       // 当前页码
const searchText = ref('');       // 搜索文本
const BuildNameCheck = ref('');       // 搜索文本
const getRepoListByNamespace = ref('')
const dialogTableVisible = ref(false)

// 使用 onBeforeMount 钩子函数来替代 created 方法
onBeforeMount(() => {
    console.log('created 方法')
    axios.get('/api/project/build/deploy/').then(response => {
        console.log(response.data);
        dataList.value = response.data.reverse()

    }).catch(error => {
        console.log(error);
    })
});

const fileUploadSuccess = () => {
    ElMessage({
        message: '文件上传成功',
        grouping: true,
        type: 'success',
    })
}
const cancelForm = () => {
    dialog.value = false
}
const handleClose = () => {
    dialog.value = false
    if (dialog.value) {
        return
    }
}
const onClick = () => {

    const postData = {
        jarBuildName: jarBuildName.value,
        jarBuildNameSpace: jarBuildNameSpace.value,
        jarBuildRepo: jarBuildRepo.value,
        jarBuildVersion: jarBuildVersion.value,
        jarBuildCommand: jarBuildCommand.value

    }

    // uploadRef.value!.submit();

    axios.post('/api/project/build/deploy/', postData).then(response => {
        console.log(response.data);

    }).catch(error => {
        console.log(error);
    })

    uploadRef.value.clearFiles();
    jarBuildName.value = ''
    jarBuildRepo.value = ''


    loading.value = true
    setTimeout(() => {
        console.log("1秒后关闭");
        dialog.value = false;
        loading.value = false
    }, 1000);

    setTimeout(() => {
        axios.get('/api/project/build/deploy/').then(response => {
            console.log(response.data);
            dataList.value = response.data.reverse()

        }).catch(error => {
            console.log(error);
        })
    }, 2000);


}
const showUrl = () => {
    jar_div.value = false;
    url_div.value = true;
    urlButtonColor.value = '#BEBEBE';
    jarButtonColor.value = '#6495ED';

}
const showJar = () => {
    jar_div.value = true;
    url_div.value = false;
    urlButtonColor.value = '#6495ED';
    jarButtonColor.value = '#BEBEBE';
}

const handleBeforeUpload = (file: File) => {
    // 获取上传文件的原始名称
    const fileName = file.name;
    const newFileName = jarBuildName.value +
        '_____' +
        jarBuildNameSpace.value +
        '_____' +
        jarBuildRepo.value +
        '_____' +
        jarBuildVersion.value +
        '_____' +
        fileName;

    // 创建一个新的 File 对象并返回
    return new File([file], newFileName, {type: file.type});


};

const clickUpload = () => {
    uploadDisabled.value = true

    if (
        (jarBuildName.value.trim().length === 0) || (jarBuildNameSpace.value.trim().length === 0) || (jarBuildRepo.value.trim().length === 0) || (jarBuildVersion.value.trim().length === 0)
    ) {
        uploadAddress.value = 'https://error.com'

        ElMessage.error('需要填写全部信息，才可以上传文件，请检查填写信息完整性,')

    } else {
        if (BuildNameCheck.value.message === 'BuildNameExists') {

            ElMessage.error('构建名称已经存在')
        } else {
            uploadDisabled.value = false
            uploadAddress.value = '/api/project/build/upload/'
        }


    }

};

const methodGetBuildName = (buildName) => {

    axios.get('/api/project/build/query/?query=' + buildName).then(response => {
        console.log(response.data);
        BuildNameCheck.value = response.data
        if (BuildNameCheck.value.message === 'BuildNameNotExists') {
            console.log('BuildNameNotExists')
            ElMessage.success('构建名称可用')
        } else {
            console.log('BuildNameExists')
            uploadDisabled.value = true // 不能点击上传
            ElMessage.error('构建名称已经存在')
        }

    }).catch(error => {
        console.log(error);
    })

};

const methodGetRepoByNamespace = (namespace) => {

    axios.get('/api/project/build/repo/?namespace=' + namespace).then(response => {
        console.log(response.data);
        getRepoListByNamespace.value = response.data
        if (getRepoListByNamespace.value.length === 0) {
            ElMessage.error('命名空间：' + namespace + ' 下没有镜像仓库')
        }
    }).catch(error => {
        console.log(error);
    })


    if (
        (jarBuildName.value.trim().length === 0) || (jarBuildNameSpace.value.trim().length === 0) || (jarBuildRepo.value.trim().length === 0) || (jarBuildVersion.value.trim().length === 0)
    ) {
        uploadAddress.value = 'https://error.com'

    } else {
        uploadDisabled.value = false  // 可以点击上传
        uploadAddress.value = 'http://127.0.0.1:8001/project/build/upload/'
    }

};

// 根据搜索文本过滤数据
const filteredData = computed(() => {
    if (searchText.value === '') {
        return dataList.value;
    } else {
        return dataList.value.filter(item => item.jarBuildName.includes(searchText.value));
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

const dialogVisibleDetailForCommandStdout = ref('')
const handleClickTableDetail = (detail) => {
    dialogVisibleDetailForCommand.value = true
    dialogVisibleDetailForCommandStdout.value = ''
    dialogVisibleDetailForCommandStdout.value = detail

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