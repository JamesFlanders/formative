import App from "@/App.vue";
import {createApp} from "vue";
import {createRouter, createWebHashHistory} from "vue-router";
import Home from "@/views/Home.vue";
import Form from "@/views/Form.vue";

import "bootstrap/dist/css/bootstrap.min.css"
import "bootstrap"

const routes = [
    {path: "/", component: Home, meta: {title: 'Home'}},
    {path: "/form/:formId", component: Form, meta: {title: 'Form'}},
]

const router = createRouter({
    history: createWebHashHistory(),
    routes
})


const app = createApp(App)

app.use(router)
app.mount('#app')
