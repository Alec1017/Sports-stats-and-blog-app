import Vue from 'vue';
import VueRouter from 'vue-router';

import '../stylesheets/main.scss';

import App from './App.vue';
import HomePage from './pages/HomePage.vue';
import Feed from './pages/Feed.vue';

Vue.use(VueRouter);

const routes = [
  {path: '/', component: HomePage},
  {path: '/feed', component: Feed}
]

const router = new VueRouter({
  routes
})

new Vue({
  el: '#app',
  router: router,
  render: h => h(App)
});
