import Vue from 'vue';

import '../stylesheets/main.scss';

import App from './components/App.vue';

new Vue({
  el: '#app',
  render: h => h(App)
});
