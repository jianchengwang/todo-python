<template>
  <div>
    <input type="text" v-model="loginForm.username" />
    <input type="text" v-model="loginForm.password" />
    <button @click="login">Login</button>
  </div>
</template>

<script>
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

    }
  }
}
</script>

<style scoped>

</style>
