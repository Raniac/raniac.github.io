import Vue from 'vue'
import Router from 'vue-router'
// import HelloWorld from '@/components/HelloWorld'
import Home from '@/components/pages/Home'
import CV from '@/components/pages/CV'
import Projects from '@/components/pages/Projects'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/CV',
      name: 'CV',
      component: CV
    },
    {
      path: '/Projects',
      name: 'CV',
      component: Projects
    }
  ]
})
