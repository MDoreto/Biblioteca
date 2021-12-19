import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Book',
    component: () => import( '../views/Book.vue')
  },
  {
    path: '/Users',
    name: 'User',
    component: () => import( '../views/User.vue')
  },
  {
    path: '/Loans',
    name: 'Loan',
    component: () => import( '../views/Loan.vue')
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
