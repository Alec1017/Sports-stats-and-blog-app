<template>
  <div class="homepage">
    <div class="homepage__wrapper container">
      <div class="homepage__inner jumbotron text-center">
        <h1>Welcome to the WBL</h1>
        <div id="carousel" class="homepage__carousel carousel slide" data-ride="carousel">
          <ol class="carousel-indicators">
            <li data-target="#carousel" data-slide-to="0" class="active"></li>
            <li data-target="#carousel" data-slide-to="1"></li>
            <li data-target="#carousel" data-slide-to="2"></li>
          </ol>
          <div class="carousel-inner">
            <div class="carousel-item active">
              <img class="d-block w-100" :src="this.images.miniGolf" alt="First slide">
            </div>
            <div class="carousel-item">
              <img class="d-block w-100" :src="this.images.fblChamps" alt="Second slide">
            </div>
            <div class="carousel-item">
              <img class="d-block w-100" :src="this.images.wblChamps" alt="Third slide">
            </div>
          </div>
          <a class="carousel-control-prev" href="#carousel" role="button" data-slide="prev">
            <span class="carousel-control-prev-icon" aria-hidden="true"></span>
            <span class="sr-only">Previous</span>
          </a>
          <a class="carousel-control-next" href="#carousel" role="button" data-slide="next">
            <span class="carousel-control-next-icon" aria-hidden="true"></span>
            <span class="sr-only">Next</span>
          </a>
        </div>
      </div> 
    </div>

    <Footer />

  </div>
</template>

<script>
  import Footer from '../components/Footer.vue';

  export default {
    name: 'HomePage',
    data() {
      return {
        images: {
          miniGolf: "https://upload.wikimedia.org/wikipedia/commons/b/ba/Mini_Golf_Tournament_Pic.jpg",
          fblChamps: "https://upload.wikimedia.org/wikipedia/commons/0/0a/FBL_Champs.jpg",
          wblChamps: "https://upload.wikimedia.org/wikipedia/commons/f/fd/WBL_Champs_Yard.jpg"
        }
      }
    },
    components: {
      Footer
    }
  }
</script>
