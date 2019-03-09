import Vue from 'vue'
import VueRouter from 'vue-router'
import App from './App'
import router from './routes'

Vue.use(VueRouter)
Vue.config.productionTip = false

/* eslint-disable-next-line no-new */
new Vue({
  router,
  el: '#app',
  render: h => h(App)
})
