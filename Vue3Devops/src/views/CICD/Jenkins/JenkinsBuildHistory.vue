<template>

    <div class="container" style=" max-width:100%">



        <ul className="nav" style="text-align: center;">
            <li className="nav-item">
                <button type="button" class="btn" style="witdh: 200px;font-size: 20px">
                    <router-link to="/jenkins/list" style="text-decoration: none; color: black; font-size: 20px"><b>构建记录列表</b>
                    </router-link>
                </button>
            </li>

            <li className="nav-item">

                <button type="button" class="btn" style="  witdh: 200px;font-size: 20px">
                    <!--                    <a className="nav-link" href="#">-->
                    <router-link to="/jenkins/history" style="text-decoration: none; color: black; font-size: 20px"><b>jenkins构建历史</b>
                    </router-link>
                    <!--                </a>-->

                </button>

            </li>

            <li className="nav-item">


                <button @click="toggleOverlay" class="btn"
                        style="background-color:#5CADAD; witdh: 200px;font-size: 20px"><b> <span style="color: white">启动构建</span>
                </b></button>
            </li>

        </ul>

        <br>
        <input type="text" class="form-control" placeholder="搜索构建名称"
               style="border: black; box-shadow: 0px 1px 0px 0px black;">


        <table class="table table-striped table-hover table-bordered" style="margin-top: 10px">
            <thead>
            <tr>
                <th scope="col">id</th>
                <th scope="col"> 构建状态</th>
                <th scope="col"> 任务名称</th>
                <th scope="col">任务id</th>
                <th scope="col">日期ms</th>
                <th scope="col">控制台输出</th>
            </tr>
            </thead>
            <tbody>


            <tr v-for="item in pageData" :key="item.id">
                <th>{{ item.id }}</th>
                <td> {{ item.status }}</td>
                <td>{{ item.name }}</td>
                <td>1</td>
                <td>21526</td>
                <td>
                 按钮
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

export default {
    name: 'MyComponent',
    components: {Message},
    data() {
        return {
            currentPage: 1,
            pageSize: 10,
            total: 15,
            dataList: [
                {
                    id: 1,
                    status: '成功',
                    name: 'my_new_job_0003',
                    last_success: '2023-09-23 00:00:01',
                    last_failed: '2023-09-23 00:00:02',
                    last_continue_time: '3S'
                },
                {
                    id: 1,
                    status: '成功',
                    name: 'my_new_job_0003',
                    last_success: '2023-09-23 00:00:01',
                    last_failed: '2023-09-23 00:00:02',
                    last_continue_time: '3S'
                },
                {
                    id: 1,
                    status: '成功',
                    name: 'my_new_job_0003',
                    last_success: '2023-09-23 00:00:01',
                    last_failed: '2023-09-23 00:00:02',
                    last_continue_time: '3S'
                },
                {
                    id: 1,
                    status: '成功',
                    name: 'my_new_job_0003',
                    last_success: '2023-09-23 00:00:01',
                    last_failed: '2023-09-23 00:00:02',
                    last_continue_time: '3S'
                },
                {
                    id: 1,
                    status: '成功',
                    name: 'my_new_job_0003',
                    last_success: '2023-09-23 00:00:01',
                    last_failed: '2023-09-23 00:00:02',
                    last_continue_time: '3S'
                },
                {
                    id: 1,
                    status: '成功',
                    name: 'my_new_job_0003',
                    last_success: '2023-09-23 00:00:01',
                    last_failed: '2023-09-23 00:00:02',
                    last_continue_time: '3S'
                },
                {
                    id: 1,
                    status: '成功',
                    name: 'my_new_job_0003',
                    last_success: '2023-09-23 00:00:01',
                    last_failed: '2023-09-23 00:00:02',
                    last_continue_time: '3S'
                },
                {
                    id: 1,
                    status: '成功',
                    name: 'my_new_job_0003',
                    last_success: '2023-09-23 00:00:01',
                    last_failed: '2023-09-23 00:00:02',
                    last_continue_time: '3S'
                },
                {
                    id: 1,
                    status: '成功',
                    name: 'my_new_job_0003',
                    last_success: '2023-09-23 00:00:01',
                    last_failed: '2023-09-23 00:00:02',
                    last_continue_time: '3S'
                },


            ]
        }
    },
    created() {
        // 模拟数据
        for (let i = 1; i <= 100; i++) {
            // this.dataList.push({
            //     id: i,
            //     name: `Data ${i}`
            // })
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
        }
    }
}
</script>
