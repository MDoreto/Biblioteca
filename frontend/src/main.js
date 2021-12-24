import Vue from 'vue'
import App from './App.vue'
import './registerServiceWorker'
import router from './router'
import vuetify from './plugins/vuetify'
import { VueMaskDirective } from 'v-mask'
import store from './store'
Vue.directive('mask', VueMaskDirective);

Vue.prototype.$colorStatus = { Disponível: "green", Emprestado: "orange", Removido: "red" },

  Vue.config.productionTip = false
new Vue({
  router,
  vuetify,
  store,
  render: h => h(App)
}).$mount('#app')
