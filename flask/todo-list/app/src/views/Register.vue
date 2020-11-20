<template>
  <div>
    <input type="text" v-model="registerForm.username" />
    <input type="text" v-model="registerForm.password" />
    <button @click="register">Register</button>
  </div>
</template>

<script>
import Api from '@/request/api.js'
export default {
  name: 'Register',
  data () {
    return {
      registerForm: {
        username: '',
        password: ''
      }
    }
  },
  methods: {
    register: function () {
      Api.user.register(registerForm).then(res => {
        this.$route.next('/login')
      })
    }
  }
}
</script>

<style scoped>

</style>
