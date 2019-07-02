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
        fields: null,
        images: {
          miniGolf: null,
          fblChamps: null,
          wblChamps: null
        }
      }
    },
    methods: {
      getContent() {
        this.$prismic.client.getByUID('homepage', 'homepage')
          .then((document) => {
            if (document) {
              this.images.miniGolf = document.data.images[0].featured_image.url;
              this.images.fblChamps = document.data.images[1].featured_image.url;
              this.images.wblChamps = document.data.images[2].featured_image.url;
            }
          });
      }
    },
    created() {
      this.getContent();
    },
    components: {
      Footer
    }
  }
</script>
