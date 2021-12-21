import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Index',
    component: () => import('../views/main/index.vue'),
    children: [{
      path: '/Books',
      name: 'Book',
      component: () => import('../views/main/components/Book.vue')
    },
    {
      path: '/Users',
      name: 'User',
      component: () => import('../views/main/components/User.vue')
    },
    {
      path: '/Loans',
      name: 'Loan',
      component: () => import('../views/main/components/Loan.vue')
    },]
  },

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
