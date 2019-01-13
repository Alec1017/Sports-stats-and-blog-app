import Vue from 'vue';

import '../stylesheets/main.scss';

import AppComponent from './components/AppComponent.vue';

new Vue({
  el: '#app',
  render: h => h(AppComponent)
});