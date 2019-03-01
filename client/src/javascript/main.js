import Vue from 'vue';
import VueRouter from 'vue-router';

import '../stylesheets/main.scss';

import App from './App.vue';
import HomePage from './pages/HomePage.vue';
import Feed from './pages/Feed.vue';
import Players from './pages/Players.vue';
import Standings from './pages/Standings.vue';
import Stats from './pages/Stats.vue';

Vue.prototype.$api = 'http://localhost:5000/api';
Vue.use(VueRouter);


const routes = [
  {path: '/', component: HomePage},
  {path: '/feed', component: Feed},
  {path: '/players', component: Players},
  {path: '/standings', component: Standings},
  {path: '/stats/:player', component: Stats}
]

const router = new VueRouter({
  routes
})

new Vue({
  el: '#app',
  router: router,
  render: h => h(App)
});
