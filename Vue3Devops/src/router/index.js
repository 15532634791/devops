import {createRouter, createWebHistory, createWebHashHistory} from 'vue-router'
import Home from '../views/Home.vue'

import LoginView from "@/views/login/LoginView.vue";

import ClusterView from "@/views/AppManage/ClusterView.vue";
import ImageRepositoryView from "@/views/AppManage/ImageRepositoryView.vue";
import ScriptView from "@/views/ConfigManage/ScriptView.vue";
import FileVersionHomeView from "@/views/ConfigManage/FileVersionHomeView.vue";

import RolesAndPermissionsView from "@/views/OrgStructureManage/RolesAndPermissionsView.vue";
import UserListView from "@/views/OrgStructureManage/UserListView.vue";
import OrgDepart from "@/views/OrgStructureManage/OrgDepart.vue";
import ProjectView from "@/views/AppManage/ProjectView.vue";
import AppInstance from "@/views/AppManage/AppInstance.vue";
import DeploymentBuild from "@/views/AppManage/DeploymentBuild.vue";

import Screen from "../views/BigScreen/Screen.vue";

import OrgConfigFileManage from "../views/ConfigManage/OrgConfigFileManage.vue";
import RdsDatabaseResource from "../views/DBMonitor/RdsDatabaseResource.vue";
import RdsInstance from "../views/DBMonitor/RdsInstance.vue";
import RdsDatabaseMonitor from "../views/DBMonitor/RdsDatabaseMonitor.vue";


// 创建路由对象
const router = createRouter({
    history: createWebHashHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: '/',
            redirect: '/login'
        },
        {
            path: '/home',
            name: 'home',
            component: Home,
            children: [
                {
                    path: 'app/dashboard',
                    name: 'wqqwqw21-list',
                    component: Screen,
                    meta: {islogin : true}
                },
                {
                    path: 'app/namespace',
                    name: 'qw21-list',
                    component: ProjectView,
                    meta: {islogin : true}
                },
                {
                    path: 'app/instance',
                    name: 'buqwqild-history',
                    component: AppInstance,
                    meta: {islogin : true}
                },
                {
                    path: 'app/cluster',
                    name: 'buqwqi21ld-history',
                    component: ClusterView,
                    meta: {islogin : true}
                },
                {
                    path: 'app/image',
                    name: 'buqwqiqw21ld-sahistory',
                    component: ImageRepositoryView,
                    meta: {islogin : true}
                },
                {
                    path: 'app/deploy',
                    name: 'buqwqiqw21lwqd-qwhistory',
                    component: DeploymentBuild,
                    meta: {islogin : true},

                },
                {
                    path: 'config/file',
                    name: 'buqwqiqw21wqlwqd-history',
                    component: FileVersionHomeView,
                    meta: {islogin : true}
                },
                {
                    path: 'config/script',
                    name: 'buqwqiqwqw21lwqd-history',
                    component: ScriptView,
                    meta: {islogin : true}
                },
                {
                    path: 'config/manage',
                    name: 'buqwqi21312wqewqdqw1212-history',
                    component: OrgConfigFileManage,
                    meta: {islogin : true}
                },
                {
                    path: 'org/depart',
                    name: 'buqqwwqiqwqw21lwqd-history',
                    component: OrgDepart,
                    meta: {islogin : true}
                },
                {
                    path: 'org/user',
                    name: 'buqqwwqiqwqw11',
                    component: UserListView,
                    meta: {islogin : true}
                },
                {
                    path: 'org/permission',
                    name: 'buqqwwqiqwqw1asd1',
                    component: RolesAndPermissionsView,
                    meta: {islogin : true}
                },
                {
                    path: 'db/resource',
                    name: 'dbresource',
                    component: RdsDatabaseResource,
                    meta: {islogin : true}
                },
                {
                    path: 'db/instance',
                    name: 'dbrinstance',
                    component: RdsInstance,
                    meta: {islogin : true}
                },
                {
                    path: 'db/monitor',
                    name: 'dbrmonitor',
                    component: RdsDatabaseMonitor,
                    meta: {islogin : true}
                }

            ]
        },
        {
            path: '/login',
            name: 'login1',
            component: LoginView
        },

    ]
})


router.beforeEach((to, from, next) => {
      console.log(to)
      console.log(from)
    if (to.meta.islogin){
        let token = localStorage.getItem('token') //获取存储对象
        if (token == null){
            return  next({path: '/login'})
        }

    }
      return next()
    }
)

export default router
