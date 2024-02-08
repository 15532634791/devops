<template >

    <div class="container" style="margin: 15px; max-width:100%">
<!--        <h3 style="text-align: center;">Gitlab Project</h3>-->



        <form >
            <button type="button" class="btn btn-secondary" data-bs-toggle="modal" data-bs-target="#exampleModal">
                <b>新建Gitlab项目 </b>
            </button>


            <div style="float: right">
                <label for="inputPassword2" class="visually-hidden">Password</label>
                <input type="text" class="form-control d-inline w-auto ms-3" placeholder="搜索项目名称" v-model="searchQuery">

            </div>

        </form>

        <table class="table table-striped table-hover table-bordered" style="margin-top: 10px">
            <thead>
            <tr>
                <th scope="col">id</th>
                <th scope="col">项目名称</th>
                <th scope="col">ssh地址</th>
                <th scope="col">创建时间</th>
                <th scope="col">Description</th>
                <th scope="col">详情</th>
            </tr>
            </thead>
            <tbody>
            <tr v-for="item in pageData" :key="item.id">
                <th>{{ item.id }}</th>
                <td> {{ item.name_with_namespace}} </td>
                <td>  {{ item.web_url }}</td>
                <td> {{ item.create_at }} </td>
                <td> {{ item.description }} </td>
                <td><a href="" style="text-decoration: none; align-text:center"> <el-icon><View /></el-icon></a> </td>
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


    <!-- Modal -->
    <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true" style="width: 100%">
        <div class="modal-dialog" >
            <div class="modal-content" style="width: 800px">

                <div class="modal-header" style="width: 800px">
                    <h1 class="modal-title fs-5" id="exampleModalLabel" style="text-align: center">新建Gitlab项目</h1>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>

                <div class="modal-body" style="width: 800px">
                    <div style="margin: 10px; border: #0b2e13">
                        <form className="row g-4" action="http://127.0.0.1:8000/cicd/gitlab/project" method="post">
                            <div className="col-11">

                                <label for=""> <b>项目名称</b></label>
                                <input type="text" className="form-control" id="inputAddress" placeholder="必须以小写或大写字母、数字、表情符号或下划线开头。也可以包含点、加号、破折号或空格" name="project_name">
<!--                                <p style="font-size: 10px">必须以小写或大写字母、数字、表情符号或下划线开头。也可以包含点、加号、破折号或空格。</p>-->
                            </div>

                          <div className="col-11">

                                <label for=""> <b>项目描述</b></label>

                                <textarea type="text" className="form-control" id="inputAddress001" placeholder="项目描述信息" name="description"></textarea>

                            </div>

                            <div className="col-md-4">
                                <label htmlFor="inputCity" className="form-label"> <b>项目URL</b></label>
                                <input type="text" className="form-control" id="inputCity" disabled="true"
                                       value="http://25.42.178.72:8929">
                            </div>

                            <div className="col-md-4">
                                <label htmlFor="inputState" className="form-label"><b>群组或用户 <a href="">创建一个群组?</a></b></label>

                                <select v-model="selectedOption" className="form-select">
                                    <option v-for="option in options" :value="option.value">{{ option.label }}</option>
                                </select>
                            </div>

                            <div className="col-md-3">

                                <label htmlFor="inputZip" className="form-label"> <b>项目标识串</b></label>
                                <input type="text" className="form-control" id="inputZip" name="project_slug">
                            </div>

                            <div className="col-10">

                                <label for=""> <b>项目可见性</b></label>
                                <div className="form-check">
                                    <input className="form-check-input" type="radio" name="visibility" id="flexRadioDefault1" value="private">
                                    <label className="form-check-label" >
                                        私有
                                    </label>
                                    <p style="font-size: 10px">项目访问权限必须明确授予每个用户。如果此项目是一个群组的一部分，访问权限将授予该群组的成员。</p>
                                </div>
                                <div className="form-check">
                                    <input className="form-check-input" type="radio" name="visibility" id="flexRadioDefault2" value="internal"
                                           checked>
                                    <label className="form-check-label">
                                        内部
                                    </label>
                                    <p style="font-size: 10px">除外部用户外，任何登录用户均可访问该项目。</p>
                                </div>

                                <div className="form-check">
                                    <input className="form-check-input" type="radio" name="visibility" id="flexRadioDefault2" value="public"
                                           checked>
                                    <label className="form-check-label" htmlFor="flexRadioDefault2">
                                        公开
                                    </label>
                                    <p style="font-size: 10px">无需任何身份验证即可访问该项目。</p>
                                </div>
                            </div>


                            <div className="col-10">

                                <label for=""><b>项目配置</b></label>
                                <div className="form-check">
                                    <input className="form-check-input" type="checkbox" id="gridCheck" name="initialize_with_readme">
                                    <label className="form-check-label" htmlFor="gridCheck">
                                        使用自述文件初始化仓库
                                    </label>
                                    <p style="font-size: 10px" >允许您立即克隆这个项目的仓库。如果您计划推送一个现有的仓库，请跳过这个步骤。</p>
                                </div>
                                <div className="form-check">
                                    <input className="form-check-input" type="checkbox" id="gridCheck" name="sast">
                                    <label className="form-check-label" htmlFor="gridCheck">
                                        启用静态应用安全测试 (SAST)
                                    </label>
                                    <p style="font-size: 10px">分析源代码查找已知安全漏洞. 了解更多。</p>
                                </div>
                            </div>

                            <div className="col-10">
                                <button type="submit" className="btn btn-primary" @click="refreshHtml">新建</button>
                                &nbsp;
<!--                                <button type="quit" className="btn  btn-success">取消</button>-->

                            </div>
                        </form>
                    </div>
                </div>

            </div>
        </div>

    </div>


</template>

<script>
import axios from 'axios';
export default {
    name: 'MyComponent',
    data() {
        return {
            currentPage: 1,
            pageSize: 10,
            total: 15,
            searchQuery: '',
            dataList: [
                {   id: 1,
                    name_with_namespace: 'wangze',
                    web_url: 'http://localhost:5173/gitlab',
                    create_at: '2023-09-23 00:00:01',
                    description: '1232'
                },
                {   id: 1,
                    name_with_namespace: 'weweq',
                    web_url: 'http://localhost:5173/gitlab',
                    create_at: '2023-09-23 00:00:01',
                    description: '1232'
                },
                {   id: 1,
                    name_with_namespace: 'gggg1',
                    web_url: 'http://localhost:5173/gitlab',
                    create_at: '2023-09-23 00:00:01',
                    description: '1232'
                },
                {   id: 1,
                    name_with_namespace: 'Gitlab 1',
                    web_url: 'http://localhost:5173/gitlab',
                    create_at: '2023-09-23 00:00:01',
                    description: '1232'
                },
                {   id: 1,
                    name_with_namespace: 'Gitlab 1',
                    web_url: 'http://localhost:5173/gitlab',
                    create_at: '2023-09-23 00:00:01',
                    description: '1232'
                },
                {   id: 1,
                    name_with_namespace: 'Gitlab 1',
                    web_url: 'http://localhost:5173/gitlab',
                    create_at: '2023-09-23 00:00:01',
                    description: '1232'
                },
                {   id: 1,
                    name_with_namespace: 'Gitlab 1',
                    web_url: 'http://localhost:5173/gitlab',
                    create_at: '2023-09-23 00:00:01',
                    description: '1232'
                },
                {   id: 1,
                    name_with_namespace: 'Gitlab 1',
                    web_url: 'http://localhost:5173/gitlab',
                    create_at: '2023-09-23 00:00:01',
                    description: '1232'
                },
                {   id: 1,
                    name_with_namespace: 'Gitlab 1',
                    web_url: 'http://localhost:5173/gitlab',
                    create_at: '2023-09-23 00:00:01',
                    description: '1232'
                },
                {   id: 1,
                    name_with_namespace: 'Gitlab 1',
                    web_url: 'http://localhost:5173/gitlab',
                    create_at: '2023-09-23 00:00:01',
                    description: '1232'
                },
                {   id: 1,
                    name_with_namespace: 'Gitlab 1',
                    web_url: 'http://localhost:5173/gitlab',
                    create_at: '2023-09-23 00:00:01',
                    description: '1232'
                },
                {   id: 1,
                    name_with_namespace: 'Gitlab 1',
                    web_url: 'http://localhost:5173/gitlab',
                    create_at: '2023-09-23 00:00:01',
                    description: '1232'
                },
                {   id: 1,
                    name_with_namespace: 'Gitlab 1',
                    web_url: 'http://localhost:5173/gitlab',
                    create_at: '2023-09-23 00:00:01',
                    description: '1232'
                },
                {   id: 1,
                    name_with_namespace: 'Gitlab 1',
                    web_url: 'http://localhost:5173/gitlab',
                    create_at: '2023-09-23 00:00:01',
                    description: '1232'
                },
                {   id: 1,
                    name_with_namespace: 'Gitlab 1',
                    web_url: 'http://localhost:5173/gitlab',
                    create_at: '2023-09-23 00:00:01',
                    description: '1232'
                },
                {   id: 1,
                    name_with_namespace: 'Gitlab 1',
                    web_url: 'http://localhost:5173/gitlab',
                    create_at: '2023-09-23 00:00:01',
                    description: '1232'
                },
                {   id: 1,
                    name_with_namespace: 'Gitlab 1',
                    web_url: 'http://localhost:5173/gitlab',
                    create_at: '2023-09-23 00:00:01',
                    description: '1232'
                },
                {   id: 1,
                    name_with_namespace: 'Gitlab 1',
                    web_url: 'http://localhost:5173/gitlab',
                    create_at: '2023-09-23 00:00:01',
                    description: '1232'
                },
                {   id: 1,
                    name_with_namespace: 'Gitlab 1',
                    web_url: 'http://localhost:5173/gitlab',
                    create_at: '2023-09-23 00:00:01',
                    description: '1232'
                },
                {   id: 1,
                    name_with_namespace: 'jenkins',
                    web_url: 'http://localhost:5173/gitlab',
                    create_at: '2023-09-23 00:00:01',
                    description: '1232'
                },
                {   id: 1,
                    name_with_namespace: 'Gitlab 1',
                    web_url: 'http://localhost:5173/gitlab',
                    create_at: '2023-09-23 00:00:01',
                    description: '1232'
                },



            ],
            selectedOption: '*',
            options: [
                { label: 'root', value: 'root' },
            ]
        }
    },
    created() {
        // 模拟数据

      axios.get('http://127.0.0.1:8000/cicd/gitlab/project').then(response => {
        console.log(response.data);
        this.dataList = response.data
      }).catch(error => {
        console.log(error);
      })
        console.log(1);
    },
    computed: {
        pageData() {
            const start = (this.currentPage - 1) * this.pageSize
            const end = start + this.pageSize
            return this.filteredUsers.slice(start, end)
        },
        filteredUsers() {
            return this.dataList.filter(user =>
                this.searchQuery ? user.name_with_namespace.toLowerCase().includes(this.searchQuery.toLowerCase()) : true
            );
        },
        refreshHtml() {
            window.location.reload()
        }
    },
    methods: {
        handleCurrentChange(currentPage) {
            this.currentPage = currentPage
        }
    }
}
</script>
