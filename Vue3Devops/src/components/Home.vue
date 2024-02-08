<template>
    <!--    background-color="#5CADAD"-->
    <el-menu
        :default-active="activeIndex"
        class="el-menu-demo"
        mode="horizontal"
        :ellipsis="false"

        background-color="#545c64"
        text-color="#fff"
    >
        <el-menu-item index="0" style="margin: 5px; pointer-events: none;">
            <img src="/logo.png" alt="">
        </el-menu-item>


        <a href="/" style="text-decoration: none">
            <el-menu-item >
                <el-icon ><HomeFilled /></el-icon></el-menu-item>
        </a>

        <div class="flex-grow" />
        <el-menu-item index="1">用户中心</el-menu-item>
        <el-sub-menu index="2">
            <template #title>王泽</template>
            <el-menu-item index="2-1">详细信息</el-menu-item>
            <el-menu-item index="2-2">时间</el-menu-item>
            <a href=""  @click="logout" style="text-decoration: none"><el-menu-item index="2-3">退出 </el-menu-item></a>
        </el-sub-menu>
    </el-menu>


    <el-container class="layout-container-demo" style="height: 100%">
        <el-aside width="200px" >
            <el-scrollbar>
                <el-menu >
                    <router-link to="/home/app/dashboard" style="text-decoration: none;">
                        <el-menu-item index="0">
                            <el-icon><Odometer /></el-icon>
                            趋势分析
                        </el-menu-item>
                    </router-link>


                    <el-sub-menu index="1">
                        <template #title>
                            <el-icon><message /></el-icon> 项目管理
                        </template>
                        <el-menu-item-group>
                            <router-link to="/home/app/deploy" style="text-decoration: none;"><el-menu-item index="1-1">构建部署</el-menu-item></router-link>
                            <router-link to="/home/app/namespace" style="text-decoration: none;"> <el-menu-item index="1-2">命名空间</el-menu-item></router-link>
                            <router-link to="/home/app/instance" style="text-decoration: none;"><el-menu-item index="1-3" style="text-decoration: none;">应用实例</el-menu-item></router-link>
                            <router-link to="/home/app/image" style="text-decoration: none;"><el-menu-item index="1-4" >镜像仓库</el-menu-item></router-link>
                            <router-link to="/home/app/cluster" style="text-decoration: none;"><el-menu-item index="1-4">集群管理</el-menu-item></router-link>
                            <!--                             <router-link to="/gitlab" style="text-decoration: none;"><el-menu-item index="1-5">GITLAB仓库</el-menu-item></router-link>-->
                        </el-menu-item-group>

                    </el-sub-menu>
                    <el-sub-menu index="5">
                        <template #title>
                            <el-icon><icon-menu /></el-icon>配置管理
                        </template>
                        <router-link to="/home/config/file" style="text-decoration: none;"><el-menu-item index="5-1">二进制版本管理</el-menu-item></router-link>
                        <router-link to="/home/config/script" style="text-decoration: none;"><el-menu-item index="5-2">脚本管理</el-menu-item></router-link>
                    </el-sub-menu>



                    <el-sub-menu index="3">
                        <template #title>
                            <el-icon><Avatar /></el-icon>
                            组织架构管理
                        </template>
                        <router-link to="/home/org/depart" style="text-decoration: none;">   <el-menu-item index="3-1">组织部门</el-menu-item> </router-link>
                        <router-link to="/home/org/user" style="text-decoration: none;"> <el-menu-item index="3-2">用户</el-menu-item></router-link>
                        <router-link to="/home/org/permission" style="text-decoration: none;"><el-menu-item index="3-3">角色和权限</el-menu-item> </router-link>
                    </el-sub-menu>

                    <el-sub-menu index="4">
                        <template #title>
                            <el-icon><setting /></el-icon>系统管理
                        </template>
                        <el-menu-item index="4-1">在运项目</el-menu-item>
                        <el-menu-item index="4-2">建设状态</el-menu-item>

                    </el-sub-menu>



                </el-menu>
            </el-scrollbar>
        </el-aside>

        <el-container style="width:100%">
            <router-view></router-view>
        </el-container>
    </el-container>

</template>

<script lang="ts" setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import {ElMessage} from 'element-plus'

const activeIndex = ref('1')

const handleSelect = (key: string, keyPath: string[]) => {
    console.log(key, keyPath)
}
import { Menu as IconMenu, Message, Setting } from '@element-plus/icons-vue'
const router = useRouter()
const item = {
    date: '2016-05-02',
    name: 'Tom',
    address: 'No. 189, Grove St, Los Angeles',
}

const logout = () => {
    const router = useRouter()
    localStorage.removeItem('loginUser')

    router.push('/login')
    ElMessage({
            message: '退出登录',
            type: 'success',
        })
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
