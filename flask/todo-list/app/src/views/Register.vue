<template>
  <div>
    <input type="text" v-model="registerForm.username" />
    <input type="text" v-model="registerForm.password" />
    <button @click="register">Register</button>
  </div>
</template>

<script>
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

    }
  }
}
</script>

<style scoped>

</style>
