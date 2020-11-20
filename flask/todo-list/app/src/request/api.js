import { get, post, del, put } from './http'

const user = {
    currentUser: () => get('/currentUser'),
    login: (params) => post('/login', params),
    regeister: (params) => post('/register', params),
    logout: () => get('/logout')
}

const todoItem = {
    get: (id) => get(`/todoItem/${id}`),
    page: (params) => get(`/todoItem`, params),
    add: (params) => post('/todoItem', params),
    update: (id, params) => put(`/todoItem/${id}`, params),
    del: (id) => del(`/todoItem/${id}`),
}

export default {
    user: user,
    todoItem: todoItem
}