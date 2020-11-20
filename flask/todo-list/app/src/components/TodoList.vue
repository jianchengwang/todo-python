<template>
    <div id="todo-list">
    <div v-for="item in todoItemList" :key="item.id">
      {{ item.id }} - {{ item.title }} - {{ item.descs }}
      | <button v-on:click="edit(item.id)">edit</button> <button v-on:click="del(item.id)">del</button>
    </div>
    <hr/>
    <div>
      id: <input type="text" v-model="todoItem.id" v-bind:readonly="isUpdate" >
      title: <input type="text" v-model="todoItem.title">
      descs: <input type="text" v-model="todoItem.descs">
      <button v-show="!isUpdate" v-on:click="add">add</button>
      <button v-show="isUpdate" v-on:click="update">update</button>
    </div>
  </div>
</template>

<script>
import Api from '@/request/api.js'
export default {
  name: 'TodoList',
  mounted () {
    this.fetch()
  },
  data () {
    return {
      todoItemList: [],
      todoItem: {
        id: '',
        title: '',
        descs: ''
      },
      isUpdate: false
    }
  },
  methods: {
    fetch: function() {
      Api.todoItem.page().then(res => {
        this.todoItemList = res.data
      })
    },
    edit: function(id) {
      this.isUpdate = true;
      this.todoItem = {...this.todoItemList.find(td => td.id == id)};
    },
    del: function(id) {
      // this.todoItemList.splice(this.todoItemList.findIndex(td => td.id == id), 1);
      Api.todoItem.del(id).then(res => {
        this.fetch()
      })
    },
    add: function () {
      // this.todoItemList.push(this.todoItem);
      Api.todoItem.add(this.todoItem).then(res => {
         this.todoItem = {
          id: '',
          title: '',
          descs: ''
        }
        this.fetch()
      })
    },
    update: function () {
      // let index = this.todoItemList.findIndex(td => td.id == this.todoItem.id)
      // this.todoItemList[index] = this.todoItem
      Api.todoItem.update(this.todoItem.id, this.todoItem).then(res => {
        this.todoItem = {
          id: '',
          title: '',
          descs: ''
        }
        this.isUpdate = false
        this.fetch()
      })
    }
   }
}
</script>

<style scoped>

</style>
