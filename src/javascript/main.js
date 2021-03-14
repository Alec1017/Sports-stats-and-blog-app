import Vue from 'vue';
import VueRouter from 'vue-router';
import VueApollo from 'vue-apollo';
import { ApolloClient } from 'apollo-boost';
import { InMemoryCache } from 'apollo-boost';
import { PrismicLink } from 'apollo-link-prismic';

import '../stylesheets/main.scss';

import App from './App.vue';
import HomePage from './pages/HomePage.vue';
import Feed from './pages/Feed.vue';
import Players from './pages/Players.vue';
import Standings from './pages/Standings.vue';
import Stats from './pages/Stats.vue';

console.log('hello')
Vue.use(VueRouter);
Vue.use(VueApollo);

const apolloClient = new ApolloClient({
  link: PrismicLink({
    uri: 'https://wbl-fbl-site.prismic.io/graphql'
  }),
  cache: new InMemoryCache()
});

const apolloProvider = new VueApollo({
  defaultClient: apolloClient
});

const routes = [
  {path: '/', component: HomePage},
  {path: '/feed', component: Feed},
  {path: '/players', component: Players},
  {path: '/standings', component: Standings},
  {path: '/stats/:player', component: Stats}
];

const router = new VueRouter({
  routes
});

new Vue({
  el: '#app',
  router: router,
  apolloProvider: apolloProvider,
  render: h => h(App)
});
