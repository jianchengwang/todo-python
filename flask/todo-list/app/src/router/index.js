import Vue from 'vue'
import Router from 'vue-router'
import Home from '_v/Home.vue'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/login',
      name: 'login',
      component: () => import('_v/Login.vue')
    },
    {
      path: '/register',
      name: 'register',
      component: () => import('_v/Register.vue')
    }
  ]
})
