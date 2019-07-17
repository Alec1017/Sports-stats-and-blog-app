<template>
  <div class="homepage">
    <div class="homepage__hero">
      <div class="homepage__content"> 
        <div class="homepage__title">Welcome to the official WBL website</div>
        <router-link class="homepage__button" to="/players">See our members</router-link>
      </div>
    </div>

    <div class="about">
      <div class="about__textbox">
        <div class="about__title">Who we are</div>
        <div class="about__text about__text--first">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis pellentesque lorem ornare felis luctus, at cursus lorem faucibus. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Mauris interdum a ex in euismod. Quisque ultrices aliquet eros, fermentum dignissim enim tempus ornare.</div>
        <div class="about__text about__text--second">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis pellentesque lorem ornare felis luctus, at cursus lorem faucibus. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Mauris interdum a ex in euismod. Quisque ultrices aliquet eros, fermentum dignissim enim tempus ornare.</div>
      </div>
    </div>

    <div class="pictures">
      <div class="pictures__title"></div>
      <figure class="pictures__item" v-for="image in this.slideImages">
        <img class="pictures__image" :src="image" />
        <figcaption class="pictures__description"> 
          <div class="pictures__title">project title</div>
        </figcaption>
      </figure>
    </div>
   
   
   
   
   
   
   
   <!-- <Carousel class="carousel" :autoplay="true" :perPage="1" :autoplayTimeout="6000" :loop="true" :autoplayHoverPause="false" :paginationEnabled="false">
      <Slide class="carousel__slide" v-for="slide in this.slideImages">
        <img class="carousel__image" :src="slide">
      </Slide>
    </Carousel>

    <Footer /> -->

  </div>
</template>

<script>
  import {Carousel, Slide } from 'vue-carousel';

  import Footer from '../components/Footer.vue';
  import { HOMEPAGE } from '../../data/graphql.js';

  export default {
    name: 'HomePage',
    data() {
      return {
        slideImages: []
      }
    },
    apollo: {
      slideImages: {
        query: HOMEPAGE,
        update: function(data) {
          let images = [];
          for (const doc of data.homepage.images) {
            images.push(doc.featured_image.url);
          }
          return images;
        }
      }   
    },
    components: {
      Carousel,
      Slide, 
      Footer
    }
  }
</script>
