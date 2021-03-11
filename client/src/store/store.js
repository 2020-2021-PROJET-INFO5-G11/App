import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)
axios.defaults.baseURL = process.env.BASE_URL;

export const store = new Vuex.Store({
  state: {
    token: localStorage.getItem('access_token') || null,
    filter: 'all',
    sorties: [],
  },
  getters: {
    loggedIn(state) {
      return state.token !== null
    },
  },
  mutations: {
    retrieveToken(state, token) {
      state.token = token
    },
    destroyToken(state) {
      state.token = null
    },
  },
  actions: {
    destroyToken(context) {
        const path = 'http://localhost:5000/api/user/logout'
        axios.defaults.headers.common['Authorization'] = 'Bearer ' + context.state.token
    
        if (context.getters.loggedIn) {
            return new Promise((resolve, reject) => {
            axios.post(path)
                .then(response => {
                localStorage.removeItem('access_token')
                context.commit('destroyToken')
                resolve(response)
                })
                .catch(error => {
                localStorage.removeItem('access_token')
                context.commit('destroyToken')
                reject(error)
                })
            })
        }
    },
    retrieveToken(context, credentials) {
        const path = 'http://localhost:5000/api/user/login'
        return new Promise((resolve, reject) => {
            axios.post(path, {
            email: credentials.email,
            password: credentials.password,
            })
            .then(response => {
                const token = response.data.access_token

                localStorage.setItem('access_token', token)
                context.commit('retrieveToken', token)
                resolve(response)
            })
            .catch(error => {
                console.log(error)
                reject(error)
            })
        })
    },
  }
})