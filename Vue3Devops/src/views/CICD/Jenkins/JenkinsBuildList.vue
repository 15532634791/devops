<template>

    <div class="container" style=" max-width:100%">


        <ul className="nav" style="text-align: center; margin: 10px">
            <li className="nav-item">

                <button type="button" class="btn" style="witdh: 200px;font-size: 15px">
                构建记录列表

                </button>

            </li>

            <li className="nav-item">

                <button type="button" class="btn" style="witdh: 200px;font-size: 15px">
                    <router-link to="/jenkins/history" style="text-decoration: none; color: deepskyblue">构建记录列表</router-link>

                </button>



            </li>




            <li className="nav-item">


                 <el-button text @click="dialogVisible = true" style="background-color:#5CADAD; ">
                   <span style="color: white">  构建 </span>
                  </el-button>


            </li>



        </ul>


        <el-dialog v-model="dialogVisible" width="900px" >

            <el-button type="primary"    @click="changeBuild">{{ this.dialog_title }} &nbsp; <el-icon><Promotion /></el-icon></el-button>

              <div v-if="awesome">
<!--                 <UrlUploadView></UrlUploadView>-->
                  <form @submit.prevent="submitForm">
                        <div style="margin: 10px; border: #0b2e13">
                            <form className="row g-4">


                                <div className="col-5">

                                    <label for=""> <b><span style="color: red">*</span> 构建名称 </b></label>
                                    <input type="text" className="form-control" id="inputAddress"
                                           placeholder="请输入构建名称">
                                </div>

                                <div className="col-5">

                                    <label for=""> <b><span style="color: red">*</span>文件URL</b></label>
                                    <input type="text" className="form-control" id="inputAddress"
                                           placeholder="请输入文件URL">

                                </div>

                                <div className="col-5">

                                    <label for=""> <b>credentialID</b></label>
                                    <input type="text" className="form-control" id="inputAddress"
                                           placeholder="credentialID为jenkins凭据ID，非必填">
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

                                    <label for=""> <b> <span style="color: red">*</span>Dockerfile位置(/data)</b></label>
                                    <input type="file" className="form-control" id="inputAddress"
                                           placeholder="http://">
                                </div>

                                <div className="col-5">

                                    <label for=""> <b> <span style="color: red">*</span>构建参数</b></label>
                                    <input type="text" className="form-control" id="inputAddress"
                                           placeholder="">

                                </div>

                                <div className="col-10">

                                    <label for=""> <b> 构建脚本</b></label>
                                    <textarea className="form-control" style="height: 100px" name="description"
                                              placeholder="echo 'Hello World!'"></textarea>

                                </div>


                            </form>
                        </div>

                        <div class="overlay-buttons" style="text-align: center">
                            <el-button type="primary" @click="dialogVisible = false">
                              Confirm
                            </el-button>
                            <el-button @click="dialogVisible = false">Cancel</el-button>

                        </div>


                    </form>

              </div>


              <div v-else>
<!--                <FileUploadView></FileUploadView>-->

                  <form @submit.prevent="submitForm">
                        <div style="margin: 10px; border: #0b2e13">
                            <form className="row g-4">
                                <div className="col-5">

                                    <label for=""> <b><span style="color: red">*</span> 构建名称 </b></label>
                                    <input type="text" className="form-control" id="inputAddress"
                                           placeholder="请输入构建名称">
                                </div>

                                <div className="col-5">

                                    <label for=""> <b><span style="color: red">*</span>文件URL</b></label>
                                    <input type="text" className="form-control" id="inputAddress"
                                           placeholder="请输入文件URL">

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

                                    <label for=""> <b> <span style="color: red">*</span>上传Jar包</b></label>
                                    <input type="file" className="form-control" id="inputAddress">
                                </div>

                                <div className="col-10">

                                    <label for=""> <b> 构建脚本</b></label>
                                    <textarea className="form-control" style="height: 100px" name="description"
                                              placeholder="echo 'Hello World!'"></textarea>

                                </div>


                            </form>
                        </div>

                        <div class="overlay-buttons" style="text-align: center">
                            <el-button type="primary" @click="dialogVisible = false">
                              Confirm
                            </el-button>
                            <el-button @click="dialogVisible = false">Cancel</el-button>

                        </div>


                    </form>
              </div>


          </el-dialog>


        <br>
        <input type="text" class="form-control" placeholder="搜索构建名称"
               style="border: black; box-shadow: 0px 1px 0px 0px black;border-radius: 0;">


        <table class="table  table-hover " style="margin-top: 10px">
            <thead>
            <tr>

                <th scope="col" style="text-align: center;"> 构建名称</th>
                <th scope="col" style="text-align: center;"> 构建版本</th>
                <th scope="col" style="text-align: center;">构建状态</th>
                <th scope="col" style="text-align: center;">持续时长</th>
                <th scope="col" style="text-align: center;">创建人</th>
                <th scope="col" style="text-align: center;">创建时间</th>
                <th scope="col" style="text-align: center;">源地址</th>
                <th scope="col" style="text-align: center;">操作</th>
            </tr>
            </thead>
            <tbody>


            <tr v-for="item in pageData" :key="item.id">

                <td style="text-align: center;"> {{ item.status }}</td>
                <td style="text-align: center;">
                    1.11
                </td>
                <td style="text-align: center;">{{ item.name }}</td>
                <td style="text-align: center;"> {{ item.last_success }}</td>
                <td style="text-align: center;"> {{ item.last_failed }}</td>
                <td style="text-align: center;"> {{ item.last_continue_time }}</td>
                <td style="text-align: center;"><a href="" style="text-decoration: none">

                    <a v-bind:href="uuurl" target="_blank"> https://image.baidu.com/ </a>
                </a></td>
                <td style="text-align: center;">
                    <el-icon style="color: limegreen"><CaretRight /></el-icon>

                    <router-link to="/jenkins/history">发布申请</router-link>
                </td>
            </tr>


            </tbody>
        </table>

        <div>
            <el-pagination
                    :current-page="currentPage"
                    :page-size="pageSize"
                    :total="total"
                    @current-change="handleCurrentChange"
            />
        </div>
    </div>


</template>

<script>
import {Message} from "@element-plus/icons-vue";
import FileUploadView from "@/views/OrgStructureManage/FileUploadView.vue";
import UrlUploadView from "@/views/OrgStructureManage/UrlUploadView.vue";
export default {
    name: 'MyComponent',
    components: {
        Message,
        FileUploadView,
        UrlUploadView
    },
    data() {
        return {

            dialog_title: '点击切换（Jar构建）',
            currentPage: 1,
            pageSize: 10,
            total: 15,
            awesome: true,
            uuurl:'https://image.baidu.com/',
            dialogVisible: false,
            dataList: [
                {
                    id: 1,
                    status: 'GD-PS0001',
                    name: '完成',
                    last_success: '五分钟',
                    last_failed: '王泽',
                    last_continue_time: '2023-09-23 00:00:02'
                },
                {
                    id: 1,
                    status: 'GD-PS0001',
                    name: '完成',
                    last_success: '五分钟',
                    last_failed: '王泽',
                    last_continue_time: '2023-09-23 00:00:02'
                }, {
                    id: 1,
                    status: 'GD-PS0001',
                    name: '完成',
                    last_success: '五分钟',
                    last_failed: '王泽',
                    last_continue_time: '2023-09-23 00:00:02'
                }, {
                    id: 1,
                    status: 'GD-PS0001',
                    name: '完成',
                    last_success: '五分钟',
                    last_failed: '王泽',
                    last_continue_time: '2023-09-23 00:00:02'
                }, {
                    id: 1,
                    status: 'GD-PS0001',
                    name: '完成',
                    last_success: '五分钟',
                    last_failed: '王泽',
                    last_continue_time: '2023-09-23 00:00:02'
                }, {
                    id: 1,
                    status: 'GD-PS0001',
                    name: '完成',
                    last_success: '五分钟',
                    last_failed: '王泽',
                    last_continue_time: '2023-09-23 00:00:02'
                }, {
                    id: 1,
                    status: 'GD-PS0001',
                    name: '完成',
                    last_success: '五分钟',
                    last_failed: '王泽',
                    last_continue_time: '2023-09-23 00:00:02'
                }, {
                    id: 1,
                    status: 'GD-PS0001',
                    name: '完成',
                    last_success: '五分钟',
                    last_failed: '王泽',
                    last_continue_time: '2023-09-23 00:00:02'
                }, {
                    id: 1,
                    status: 'GD-PS0001',
                    name: '完成',
                    last_success: '五分钟',
                    last_failed: '王泽',
                    last_continue_time: '2023-09-23 00:00:02'
                }, {
                    id: 1,
                    status: 'GD-PS0001',
                    name: '完成',
                    last_success: '五分钟',
                    last_failed: '王泽',
                    last_continue_time: '2023-09-23 00:00:02'
                }, {
                    id: 1,
                    status: 'GD-PS0001',
                    name: '完成',
                    last_success: '五分钟',
                    last_failed: '王泽',
                    last_continue_time: '2023-09-23 00:00:02'
                }, {
                    id: 1,
                    status: 'GD-PS0001',
                    name: '完成',
                    last_success: '五分钟',
                    last_failed: '王泽',
                    last_continue_time: '2023-09-23 00:00:02'
                }, {
                    id: 1,
                    status: 'GD-PS0001',
                    name: '完成',
                    last_success: '五分钟',
                    last_failed: '王泽',
                    last_continue_time: '2023-09-23 00:00:02'
                }, {
                    id: 1,
                    status: 'GD-PS0001',
                    name: '完成',
                    last_success: '五分钟',
                    last_failed: '王泽',
                    last_continue_time: '2023-09-23 00:00:02'
                }, {
                    id: 1,
                    status: 'GD-PS0001',
                    name: '完成',
                    last_success: '五分钟',
                    last_failed: '王泽',
                    last_continue_time: '2023-09-23 00:00:02'
                }, {
                    id: 1,
                    status: 'GD-PS0001',
                    name: '完成',
                    last_success: '五分钟',
                    last_failed: '王泽',
                    last_continue_time: '2023-09-23 00:00:02'
                }, {
                    id: 1,
                    status: 'GD-PS0001',
                    name: '完成',
                    last_success: '五分钟',
                    last_failed: '王泽',
                    last_continue_time: '2023-09-23 00:00:02'
                },

            ]
        }
    },
    created() {
        // 模拟数据
        for (let i = 1; i <= 100; i++) {

            console.log(1)
        }
    },
    computed: {
        pageData() {
            const start = (this.currentPage - 1) * this.pageSize
            const end = start + this.pageSize
            return this.dataList.slice(start, end)
        }
    },
    methods: {
        handleCurrentChange(currentPage) {
            this.currentPage = currentPage
        },
        changeBuild(){
            this.awesome = !this.awesome
            if (this.awesome === true){
                this.dialog_title = '点击切换（Jar构建）'
            }else{
                this.dialog_title = '点击切换（Url构建）'
            }
        }

    }

}
</script>


<style scoped>
.overlay {
    position: fixed;
    right: 0;
    top: 58px;
    width: 60%;
    height: 90vh;
    background-color: white;
    z-index: 9999;
    overflow-x: hidden;
    transition: 0.2s;
    transform: translateX(100%);
    border: black 1px;
}

.overlay.show {
    transform: translateX(0);
}

.overlay-content {
    position: relative;
    width: 100%;
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}

.overlay-buttons {
    margin-top: 10px;
}
</style>