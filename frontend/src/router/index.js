import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Login',
    component: () => import('../views/login/Login.vue')
  },
  {
    path: '/Home',
    name: 'Index',
    component: () => import('../views/main/index.vue'),
    children: [{
      path: '/Livros',
      name: 'Book',
      component: () => import('../views/main/components/Book.vue')
    },
    {
      path: '/Usuarios',
      name: 'User',
      component: () => import('../views/main/components/User.vue')
    },
    {
      path: '/Emprestimos',
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
router.beforeEach((toRoute, fromRoute, next) => {
  window.document.title = toRoute.meta && toRoute.meta.title ? toRoute.meta.title : 'Biblioteca ' + toRoute.path.replace('/', '- ');

  next();
})
export default router
