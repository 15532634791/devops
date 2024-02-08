<template>


    <el-menu
            :default-active="activeIndex"
            class="el-menu-demo"
            mode="horizontal"
            :ellipsis="false"
            @select="handleSelect"
            background-color="#545c64"
            text-color="#fff"
            active-text-color="#ffd04b"
    >
        <el-menu-item index="0" style="margin-top: 5px; pointer-events: none;">
            <img
                    style="width: 130px;margin-top: 5px;"
                    src="/logo1111.png"

            />
        </el-menu-item>

        <a href="#/home/app/dashboard/" style="text-decoration: none" disabled="true">
            <el-menu-item>

                用户中心
            </el-menu-item>

        </a>
        <div class="flex-grow"/>

        <el-menu-item index="1"> 目录收缩：

            <el-switch v-model="isCollapse">
                <template #active-action>
                    <span class="custom-active-action">T</span>
                </template>
                <template #inactive-action>
                    <span class="custom-inactive-action">F</span>
                </template>
            </el-switch>
        </el-menu-item>
        <el-sub-menu index="2">
            <template #title> {{ lg_username }}</template>
            <el-menu-item index="2-1">详细信息</el-menu-item>
            <el-menu-item index="2-2">
                时间
            </el-menu-item>

            <a href="" @click="logout" style="text-decoration: none">
                <el-menu-item index="2-3">退出</el-menu-item>
            </a>
            <el-sub-menu index="2-4">
                <template #title>item four</template>
                <el-menu-item index="2-4-1">item one</el-menu-item>
                <el-menu-item index="2-4-2">item two</el-menu-item>
                <el-menu-item index="2-4-3">item three</el-menu-item>
            </el-sub-menu>
        </el-sub-menu>
    </el-menu>


    <el-container class="layout-container-demo" style="height: 100%">
        <el-aside :style="{ width: isCollapse ? '64px' : '200px' }">
            <el-scrollbar>
                <el-menu
                        default-active="2"
                        class="el-menu-vertical-demo"
                        :collapse="isCollapse"
                        @open="handleOpen"
                        @close="handleClose"
                >

                    <router-link to="/home/app/dashboard" style="text-decoration: none;">
                        <el-menu-item index="1">
                            <el-icon>
                                <Odometer/>
                            </el-icon>
                            <template #title>趋势分析</template>
                        </el-menu-item>
                    </router-link>


                    <el-sub-menu index="2">
                        <template #title>
                            <el-icon>
                                <Discount/>
                            </el-icon>
                            <span>项目管理</span>
                        </template>
                        <el-menu-item-group>


                            <router-link to="/home/app/deploy" style="text-decoration: none;">
                                <el-menu-item index="2-1">构建部署</el-menu-item>
                            </router-link>
                            <router-link to="/home/app/namespace" style="text-decoration: none;">
                                <el-menu-item index="2-2">命名空间</el-menu-item>
                            </router-link>

                            <router-link to="/home/app/image" style="text-decoration: none;">
                                <el-menu-item index="2-3">镜像仓库</el-menu-item>
                            </router-link>
                            <router-link to="/home/app/instance" style="text-decoration: none;">
                                <el-menu-item index="2-4" style="text-decoration: none;">应用实例</el-menu-item>
                            </router-link>
                            <router-link to="/home/app/cluster" style="text-decoration: none;">
                                <el-menu-item index="2-5">集群管理</el-menu-item>
                            </router-link>


                        </el-menu-item-group>

                    </el-sub-menu>


                    <el-sub-menu index="3">
                        <template #title>
                            <el-icon>
                                <Connection/>
                            </el-icon>
                            <span>配置管理</span>
                        </template>
                        <el-menu-item-group>


                            <router-link to="/home/config/file" style="text-decoration: none;">
                                <el-menu-item index="3-1">测试管理</el-menu-item>
                            </router-link>
                            <router-link to="/home/config/script" style="text-decoration: none;">
                                <el-menu-item index="3-2">自动化运维工具</el-menu-item>
                            </router-link>
                            <router-link to="/home/config/manage" style="text-decoration: none;">
                                <el-menu-item index="3-3">命名空间配置管理</el-menu-item>
                            </router-link>


                        </el-menu-item-group>

                    </el-sub-menu>


                    <el-sub-menu index="4">
                        <template #title>
                            <el-icon>
                                <Notification/>
                            </el-icon>
                            <span> 组织架构管理</span>
                        </template>
                        <el-menu-item-group>


                            <router-link to="/home/org/depart" style="text-decoration: none;">
                                <el-menu-item index="4-1">组织部门</el-menu-item>
                            </router-link>
                            <router-link to="/home/org/user" style="text-decoration: none;">
                                <el-menu-item index="4-2">用户</el-menu-item>
                            </router-link>
                            <router-link to="/home/org/permission" style="text-decoration: none;">
                                <el-menu-item index="4-3">角色和权限</el-menu-item>
                            </router-link>

                        </el-menu-item-group>

                    </el-sub-menu>


                    <el-sub-menu index="5">
                        <template #title>
                            <el-icon>
                                <Setting/>
                            </el-icon>
                            <span> 系统管理</span>
                        </template>
                        <el-menu-item-group>


                            <el-menu-item index="5-1">在运项目</el-menu-item>
                            <el-menu-item index="5-2">建设状态</el-menu-item>

                        </el-menu-item-group>

                    </el-sub-menu>


                    <el-sub-menu index="6">
                        <template #title>
                            <el-icon>
                                <Clock/>
                            </el-icon>
                            <span> 数据库监控</span>
                        </template>
                        <el-menu-item-group>


                            <el-sub-menu index="6-1">
                                <template #title>RDS</template>
                                <router-link to="/home/db/resource" style="text-decoration: none;">
                                    <el-menu-item index="6-1-1">数据库资源信息</el-menu-item>
                                </router-link>
                                <router-link to="/home/db/instance" style="text-decoration: none;">
                                    <el-menu-item index="6-1-2">实例账号数据库信息</el-menu-item>
                                </router-link>
                                <router-link to="/home/db/monitor" style="text-decoration: none;">
                                    <el-menu-item index="6-1-3">数据库监控</el-menu-item>
                                </router-link>

                            </el-sub-menu>

                            <el-sub-menu index="6-2">
                                <template #title>REDIS</template>
                                <el-menu-item index="6-2-1">数据库资源信息</el-menu-item>
                                <el-menu-item index="6-2-2">实例账号数据库信息</el-menu-item>
                                <el-menu-item index="6-2-3">数据库监控</el-menu-item>
                            </el-sub-menu>
                            <el-sub-menu index="6-3">
                                <template #title>ADB</template>
                                <el-menu-item index="6-3-1">数据库资源信息</el-menu-item>
                                <el-menu-item index="6-3-2">实例账号数据库信息</el-menu-item>
                                <el-menu-item index="6-3-3">数据库监控</el-menu-item>
                            </el-sub-menu>

                            <el-sub-menu index="6-4">
                                <template #title>慢SQL</template>
                                <el-menu-item index="6-4-1">数据库资源信息</el-menu-item>
                                <el-menu-item index="6-4-2">实例账号数据库信息</el-menu-item>
                                <el-menu-item index="6-4-3">数据库监控</el-menu-item>
                            </el-sub-menu>
                        </el-menu-item-group>

                    </el-sub-menu>


                </el-menu>

            </el-scrollbar>
        </el-aside>

        <el-container style="max-width:100%">
            <router-view></router-view>
        </el-container>
    </el-container>


</template>

<script lang="ts" setup>

import {useRouter} from 'vue-router'
import {ElMessage} from 'element-plus'
import {Menu as IconMenu, Message, Setting} from '@element-plus/icons-vue'
import {ref} from 'vue'

const showOverlay = ref(false)


const activeIndex = ref('1')

const lg_username = ref(localStorage.getItem('username'))
const handleSelect = (key: string, keyPath: string[]) => {
    console.log(key, keyPath)
}

const logout = () => {

    const router = useRouter()
    localStorage.removeItem('token')
    localStorage.removeItem('username')
    localStorage.removeItem('userId')

    router.push('/login')
    ElMessage({
        message: '退出登录',
        type: 'success',
    })
}

const isCollapse = ref(false)
const handleOpen = (key: string, keyPath: string[]) => {
    console.log(key, keyPath)
}
const handleClose = (key: string, keyPath: string[]) => {
    console.log(key, keyPath)
}


</script>


<style>
.flex-grow {
    flex-grow: 1;
}

.layout-container-demo .el-header {
    position: relative;
    background-color: var(--el-color-primary-light-7);
    color: var(--el-text-color-primary);
}

.layout-container-demo .el-aside {
    color: var(--el-text-color-primary);
    background: var(--el-color-primary-light-8);
}

.layout-container-demo .el-menu {
    border-right: none;
}

.layout-container-demo .el-main {
    padding: 0;
}

.layout-container-demo .toolbar {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    height: 100%;
    right: 20px;
}
</style>
