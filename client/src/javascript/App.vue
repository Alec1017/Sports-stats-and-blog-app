<template>
  <div class="wrapper">
    <navBar />
    <div class="main">
      <router-view></router-view>
    </div>
  </div>
</template>
<script>
  import NavBar from './components/NavBar.vue';

  export default {
    name: 'app',
    components: {
      navBar: NavBar
    }
  }
</script>