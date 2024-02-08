import { createStore } from 'vuex'

const store = createStore({
    state() {
        return {
            isAuthenticated: false // 用户登录状态
        }
    },
    mutations: {
        setIsAuthenticated(state, isAuthenticated) {
            state.isAuthenticated = isAuthenticated
        }
    },
    actions: {
        login({ commit }, { username, password }) {
            // 模拟登录请求
            return new Promise((resolve, reject) => {
                if (username === 'admin' && password === 'password') {
                    commit('setIsAuthenticated', true)
                    resolve()
                } else {
                    reject('Invalid username or password')
                }
            })
        },
        logout({ commit }) {
            commit('setIsAuthenticated', false)
        }
    }
})

export default store
