// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import clipper from '../static/clipper'
import store from './store'
import 'lib-flexible/flexible'

Vue.config.productionTip = false
Vue.use(clipper)

/* eslint-disable no-new */
new Vue({
  el: '#app',
  store,
  router,
  components: { App },
  template: '<App/>'
})
