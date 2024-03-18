import { createApp } from 'vue'
import { createPinia } from 'pinia'
import { createRouter, createWebHistory } from 'vue-router'


// Route Components
import Home from './pages/Home.vue'
import About from './pages/About.vue'
import FAQ from './pages/FAQ.vue'
import Contact from './pages/Contact.vue'
import Convert from './pages/Convert.vue'

// Configure tailwind css
import './styles.css'

// App Component
import App from './App.vue'

const app =createApp(App)

const pinia = createPinia()

const router = createRouter({
    history: createWebHistory(),
    routes: [
        { path: '/', component: Home },
        { path: '/about', component: About },
        { path: '/faq', component: FAQ },
        { path: '/contact', component: Contact },
        { path: '/convert', component: Convert }
    ]
  })


app.use(router)
app.use(pinia)
app.mount('#app')


