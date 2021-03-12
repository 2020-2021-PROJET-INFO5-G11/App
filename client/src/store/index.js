import axios from 'axios'
import Vue from 'vue'
import Vuex from 'vuex'

// imports of AJAX functions will go here
import { authenticate, register } from '../api/index'
import { isValidJwt, EventBus } from '../utils/index'

Vue.use(Vuex)

const state = {
  // single source of data
  surveys: [],
  currentSurvey: {},
  user: {},
  jwt: ''
}

const actions = {
  // asynchronous operations
  login (context, userData) {
    context.commit('setUserData', { userData })
    const path = 'http://localhost:5000/api/user/login';
    axios.get(path, { params: { email: userData.email, password: userData.password } })
      .then(response => context.commit('setJwtToken', { jwt: response.data }))
      .catch(error => {
        console.log('Error Authenticating: ', error)
        EventBus.emit('failedAuthentication', error)
      })
  },
  register (context, userData) {
    context.commit('setUserData', { userData })
    return register(userData)
      .then(context.dispatch('login', userData))
      .catch(error => {
        console.log('Error Registering: ', error)
        EventBus.emit('failedRegistering: ', error)
      })
  },
}

const mutations = {
  // isolated data mutations
  setUserData (state, payload) {
    console.log('setUserData payload = ', payload)
    state.userData = payload.userData
  },
  setJwtToken (state, payload) {
    console.log('setJwtToken payload = ', payload)
    localStorage.token = payload.jwt.token
    state.jwt = payload.jwt
  }
}

const getters = {
  // reusable data accessors
  isAuthenticated (state) {
    return isValidJwt(state.jwt.token)
  }
}

const store = new Vuex.Store({
  state,
  actions,
  mutations,
  getters
})

export default store