<template>
  <div class="wrapper">
   <navBar></navBar>
   <homePage></homePage>
  </div>
</template>
<script>
  import NavBar from './NavBar.vue';
  import HomePage from './HomePage.vue';

  export default {
    name: 'app',
    data() {
      return {
        message: 'Hello Vue!'
      };
    },
    components: {
      navBar: NavBar,
      homePage: HomePage
    },
  }
</script>