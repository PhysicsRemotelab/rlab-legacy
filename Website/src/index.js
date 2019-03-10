import Vue from 'vue'
import Vuetify from 'vuetify'
import App from './App'
import router from './router'
import store from './store/store'

Vue.use(Vuetify)

Vue.config.productionTip = false

const app = new Vue({
  router,
  store,
  el: '#app',
  render: h => h(App)
})

export default app
