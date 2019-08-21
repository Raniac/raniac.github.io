import Vue from 'vue'
import Router from 'vue-router'
// import HelloWorld from '@/components/HelloWorld'
import Home from '@/components/pages/Home'
import Portfolio from '@/components/pages/Portfolio'
import Blog from '@/components/pages/Blog'
import BlogDetail from '@/components/pages/BlogDetail'
import Contact from '@/components/pages/Contact'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/Portfolio',
      name: 'Portfolio',
      component: Portfolio
    },
    {
      path: '/Blog',
      name: 'Blog',
      component: Blog
    },
    {
      path: '/BlogDetail',
      name: 'BlogDetail',
      component: BlogDetail
    },
    {
      path: '/Contact',
      name: 'Contact',
      component: Contact
    }
  ]
})
