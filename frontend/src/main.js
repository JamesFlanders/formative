import App from "@/App.vue";
import {createApp} from "vue";
import {createRouter, createWebHistory} from "vue-router";
import Home from "@/views/Home.vue";
import Form from "@/views/Form.vue";

import 'material-icons/iconfont/material-icons.css';
import '@/css/main.scss'

const routes = [
    {path: "/", component: Home, meta: {title: 'Home'}},
    {path: "/form/:formId", component: Form, meta: {title: 'Form'}},
]

const router = createRouter({
    history: createWebHistory(),
    routes
})


const app = createApp(App)

app.use(router)
app.mount('#app')
