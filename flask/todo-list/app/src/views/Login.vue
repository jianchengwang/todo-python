<template>
  <div>
    <input type="text" v-model="loginForm.username" />
    <input type="text" v-model="loginForm.password" />
    <button @click="login">Login</button>
  </div>
</template>

<script>
import API from '@/request/api.js'
export default {
  name: 'Login',
  data () {
    return {
      loginForm: {
        username: '',
        password: ''
      }
    }
  },
  methods: {
    login: function () {
      API.user.login(this.loginForm).then(res => {
        this.$store.dispatch('loginSuccess', res.data, this.$route.query.redirect);
      })
    }
  }
}
</script>

<style scoped>

</style>
