<template>
   <h1 class="title-message">{{ message }}</h1>
</template>
<script>
  export default {
    name: 'app',
    data() {
      return {
        message: 'Hello Vue!'
      };
    }
   }
</script>