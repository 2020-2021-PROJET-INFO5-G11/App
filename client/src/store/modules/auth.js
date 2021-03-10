//store/modules/auth.js

import axios from 'axios';
const state = {
    user: null,
    sorties: null,
};
const getters = {
    isAuthenticated: state => !!state.user,    
    StateSorties: state => state.sorties,
    StateUser: state => state.user,
};
const actions = {
    async Register({dispatch}, form) {
        await axios.post('register', form)
        let UserForm = new FormData()
        UserForm.append('username', form.username)
        UserForm.append('password', form.password)
        await dispatch('LogIn', UserForm)
      },
      async LogIn({commit}, User) {
        await axios.post('login', User)
        await commit('setUser', User.get('username'))
      },      
      async LogOut({commit}){
        let user = null
        commit('logout', user)
      }      
};
const mutations = {
    setUser(state, username){
        state.user = username
    },
    setSorties(state, sorties){
        state.sorties = sorties
    },
    LogOut(state){
        state.user = null
        state.sorties = null
    },
};
export default {
  state,
  getters,
  actions,
  mutations
};
