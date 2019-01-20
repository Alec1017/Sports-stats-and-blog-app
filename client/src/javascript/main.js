import Vue from 'vue';
import VueRouter from 'vue-router';

import '../stylesheets/main.scss';

import App from './App.vue';
import HomePage from './pages/HomePage.vue';

Vue.use(VueRouter);

const routes = [
  {path: '/', component: HomePage}
]

const router = new VueRouter({
  routes,
  mode: 'history'
})

new Vue({
  el: '#app',
  router: router,
  render: h => h(App)
});
