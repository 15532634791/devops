<template>
  <div style="width: 100%">
    <el-menu
      default-active="2"
      class="el-menu-vertical-demo"
      :collapse="isCollapse"
      @open="handleOpen"
      @close="handleClose"
    >
      <el-sub-menu v-for="menu in menus" :key="menu.index" :index="menu.index">
        <template #title>
          <el-icon>
            <component :is="getIconComponent(menu.icon)" />
          </el-icon>
          <span>{{ menu.title }}</span>
        </template>
        <el-menu-item-group v-for="group in menu.groups" :key="group.title" :title="group.title">
          <router-link
            v-for="item in group.items"
            :key="item.index"
            :to="item.route"
            style="text-decoration: none"
          >
            <el-menu-item :index="item.index">{{ item.title }}</el-menu-item>
          </router-link>
        </el-menu-item-group>
      </el-sub-menu>
    </el-menu>

    <router-view></router-view>
  </div>
</template>

<script lang="ts" setup>
import { ref, computed } from 'vue'
import {
  Document,
  Menu as IconMenu,
  Location,
  Setting,
  Odometer
} from '@element-plus/icons-vue'

const isCollapse = ref(false)
const handleOpen = (key: string, keyPath: string[]) => {
  console.log(key, keyPath)
}
const handleClose = (key: string, keyPath: string[]) => {
  console.log(key, keyPath)
}


const menus = [
    {
        index: '0',
        title: '趋势分析',
        icon: "Odometer",
        route: '#/',
    },
    {
        index: '1',
        title: '项目管理',
        icon: "Location",
        groups: [
            {
                // title: 'Group One',
                items: [
                    {index: '1-1', title: '部署构建', route: '/login'},
                    {index: '1-2', title: '命名空间', route: '/item-two'},
                    {index: '1-3', title: '镜像仓库', route: '/item-three'},
                    {index: '1-4', title: '应用实例', route: '/item-three'},
                    {index: '1-5', title: '集群管理', route: '/item-three'},
                ],
            },
            // {
            //   // title: 'Group Two',
            //   items: [{ index: '1-3', title: 'item three', route: '/item-three' }],
            // },
        ],
    },
    {
        index: '2',
        title: '配置管理',
        icon: "IconMenu",
        groups: [
            {
                items: [
                    {index: '2-1', title: '测试', route: '/login'},
                    {index: '2-2', title: '自动化工具', route: '/item-two'},
                    {index: '2-3', title: '命名空间配置管理', route: '/item-three'},
                ],
            },
        ],
    },
    {
        index: '3',
        title: '组织架构管理',
        icon: "Document",
        groups: [
            {
                items: [
                    {index: '3-1', title: '组织部门', route: '/login'},
                    {index: '3-2', title: '用户', route: '/item-two'},
                    {index: '3-3', title: '角色和权限', route: '/item-three'},
                ],
            },
        ],
    },
    {
        index: '4',
        title: 'Navigator Four',
        icon: "Setting",
        route: '/navigator-four',
    },
]

// 根据 iconType 返回对应的图标组件
const getIconComponent = (iconType: string) => {
  switch (iconType) {
    case 'Odometer':
      return Odometer
    case 'Location':
      return Location
    case 'IconMenu':
      return IconMenu
    case 'Document':
      return Document
    case 'Setting':
      return Setting
    default:
      // 默认返回一个空的 div 组件
      return {
        render: () => null
      }
  }
}

</script>

<style>
.el-menu-vertical-demo:not(.el-menu--collapse) {
    width: 200px;
    min-height: 400px;
}
</style>