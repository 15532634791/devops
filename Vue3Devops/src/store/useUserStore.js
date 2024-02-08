import { defineStore } from 'pinia'

export const useUserStore = defineStore("main21", {
    state: () => {
    return {
        account: "admin",
        age: 25,
        level: 5,
        nickname: "男wqe",
        login_username: 'admin',
        login_password: '123'
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