import Vue from 'vue'
import Router from 'vue-router'
Vue.use(Router)

import store from '@/store/index';
import Home from '_v/Home.vue'

const router = new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home,
      meta: {
        requireAuth: true
      }
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

// 路由拦截
router.beforeEach((to, from, next) => {
  if (to.matched.some((r) => r.meta.requireAuth)) {
    if (store.getters.token) {
      next();
    } else {
      next({
        path: '/login',
        query: {redirect: to.fullPath}
      });
    }
  } else {
    next();
  }
});

export default router
