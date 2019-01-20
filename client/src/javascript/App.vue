<template>
  <div class="main">
    <navBar />
    <div class="container">
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