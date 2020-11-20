import axios from 'axios'
import QS from 'qs'

import store from '@/store/index';
import router from '@/router/index';

// 基本配置
if(process.env.VUE_APP_BASE_URL) {
    axios.defaults.baseURL = process.env.VUE_APP_BASE_URL
}
axios.defaults.timeout = 10000
axios.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded;charset=UTF-8'

// 请求拦截器
axios.interceptors.request.use(
    config => {        
        // 每次发送请求之前判断vuex中是否存在token        
        // 如果存在，则统一在http请求的header都加上token，这样后台根据token判断你的登录情况
        // 即使本地存在token，也有可能token是过期的，所以在响应拦截器中要对返回状态进行判断 
        const token = store.getters.token;  
        token && (config.headers.Authorization = 'Bearer ' + token); 
        return config;    
    },    
    error => {        
        return Promise.error(error); 
    }
)

// 响应拦截器
axios.interceptors.response.use(    
    response => {   
        // 如果返回的状态码为200，说明接口请求成功，可以正常拿到数据     
        // 否则的话抛出错误
        if (response.status === 200) {            
            return Promise.resolve(response);        
        } else {            
            return Promise.reject(response);        
        }    
    },    
    // 服务器状态码不是2开头的的情况
    // 这里可以跟你们的后台开发人员协商好统一的错误状态码    
    // 然后根据返回的状态码进行一些操作，例如登录过期提示，错误提示等等
    // 下面列举几个常见的操作，其他需求可自行扩展
    error => {            
        if (error.response.status) {  
            response_msg = error.response.data.msg   
            switch (error.response.status) {  
                // 401: 未登录
                // 未登录则跳转登录页面，并携带当前页面的路径
                // 在登录成功后返回当前页面，这一步需要在登录页操作。                
                case 401:   
                    alert(response_msg? response_msg: '未登录或者token失效，将跳转到登录页面')     
                    store.dispatch('loginSuccess', null);
                    //  跳转登录页面，并将要浏览的页面fullPath传过去，登录成功后跳转需要访问的页面 
                     setTimeout(() => {                        
                         router.replace({                            
                             path: '/login',                            
                             query: { 
                                redirect: router.currentRoute.fullPath 
                             }                        
                         });                    
                     }, 1000);                              
                    break;             
                case 403:
                    alert(response_msg? response_msg: '无权限访问')                         
                    break; 

                // 404请求不存在
                case 404:
                    alert(response_msg? response_msg: '网络请求不存在')                         
                    break;
                // 其他错误，直接抛出错误提示
                default:
                    alert(response_msg? response_msg: '服务端错误，请稍后再试')                         
            }
            return Promise.reject(error.response);
        }
    }    
)

/**
 * get方法，对应get请求
 * @param {String} url [请求的url地址]
 * @param {Object} params [请求时携带的参数]
 */
export function get(url, params) {    
    return new Promise((resolve, reject) => {        
        axios.get(url, {            
            params: params        
        }).then(res => {
            resolve(res.data);
        }).catch(err =>{
            reject(err.data)        
        })    
    });
}

/** 
 * post方法，对应post请求 
 * @param {String} url [请求的url地址] 
 * @param {Object} params [请求时携带的参数] 
 */
export function post(url, params) {
    return new Promise((resolve, reject) => {
         axios.post(url, QS.stringify(params))
        .then(res => {
            resolve(res.data);
        })
        .catch(err =>{
            reject(err.data)
        })
    });
}

/**
 * delete方法，对应delete请求
 * @param {String} url [请求的url地址]
 * @param {Object} params [请求时携带的参数]
 */
export function del(url, params) {   
    return new Promise((resolve, reject) => {        
        axios.delete(url, params).then(res => {
            resolve(res.data);
        }).catch(err =>{
            reject(err.data)        
        })    
    });
}

/**
 * put方法，对应put请求
 * @param {String} url [请求的url地址]
 * @param {Object} params [请求时携带的参数]
 */
export function put(url, params) {   
    return new Promise((resolve, reject) => {        
        axios.put(url, QS.stringify(params)).then(res => {
            resolve(res.data);
        }).catch(err =>{
            reject(err.data)        
        })    
    });
}


