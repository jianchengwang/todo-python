import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

import router from '@/router/index';
import Api from '@/request/api'

export default new Vuex.Store({
  state: {
    user: null,
    token: null
  },
  getters: {
    token: state => {
      if(state.token) {
        return state.token
      }
      return localStorage.getItem('token')      
    }
  },
  mutations: {
    setToken (state, token) {
      state.token = token
      if(token) {
        localStorage.setItem('token', token)   
      } else {
        state.user = null
        localStorage.removeItem('token')      
      }
    },
    setCurrentUser (state, user) {
      state.user = user
    }
  },
  actions: {
    loginSuccess ({ commit, state }, token, redirect) {
      commit('setToken', token)              
      if(token) {
        Api.user.currentUser().then(res => {
          commit('setCurrentUser', res.data) 
          if(!redirect) {
            redirect = '/'
          }
          router.replace({                            
            path: redirect                  
          });                   
        })
      }           
    }
  }
})