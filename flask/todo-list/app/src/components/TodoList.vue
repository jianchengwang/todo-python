<template>
    <div id="todo-list">
    <div v-for="item in todoItemList" :key="item.id">
      {{ item.id }} - {{ item.title }} - <button v-on:click="edit(item.id)">edit</button> <button v-on:click="del(item.id)">del</button>
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
export default {
  name: 'TodoList',
  data () {
    return {
      todoItemList: [{
        id: '1',
        title: 'td1',
        descs: ''
      }, {
        id: '2',
        title: 'td2',
        descs: ''
      }],
      todoItem: {
        id: '',
        title: '',
        descs: ''
      },
      isUpdate: false
    }
  },
   methods: {
    edit: function(id) {
      this.isUpdate = true;
      this.todoItem = {...this.todoItemList.find(td => td.id == id)};
    },
    del: function(id) {
      this.todoItemList.splice(this.todoItemList.findIndex(td => td.id == id), 1);
    },
    add: function () {
      this.todoItemList.push(this.todoItem);
      this.todoItem = {
        id: '',
        title: '',
        descs: ''
      }
    },
    update: function () {
      let index = this.todoItemList.findIndex(td => td.id == this.todoItem.id)
      this.todoItemList[index] = this.todoItem
      this.todoItem = {
        id: '',
        title: '',
        descs: ''
      }
      this.isUpdate = false
    }
   }
}
</script>

<style scoped>

</style>
