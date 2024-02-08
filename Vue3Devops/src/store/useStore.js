import { defineStore } from 'pinia'

export const useStore = defineStore("main", {
    state: () => {
    return {
        account: "小猪课堂",
        age: 25,
        level: 5,
        nickname: "男",
    };
    // 共享的数据
  },
    getters: () => {
      // 通过计算共享的数据

    },
    actions: () => {
        // 共享的函数
}
});