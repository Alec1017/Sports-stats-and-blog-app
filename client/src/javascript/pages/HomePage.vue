<template>
  <div class="homepage">
    <div class="homepage__hero">
      <div class="homepage__background">
        <img :src="this.background">
      </div>
      <div class="homepage__content"> 
        <div class="homepage__title">Welcome to the official WBL website</div>
        <router-link class="homepage__button" to="/players">See our members</router-link>
      </div>
    </div>

    <div class="about">
      <div class="about__textbox">
        <div class="about__title">Who we are</div>
        <div class="about__text about__text--first" v-html="this.about_section_one"></div>
        <div class="about__text about__text--second" v-html="this.about_section_two"></div>
      </div>
    </div>

    <div class="pictures">
      <div class="pictures__title"></div>
      <figure class="pictures__item" v-for="image in this.featuredImages">
        <img class="pictures__image" :src="image.url" />
        <figcaption class="pictures__description"> 
          <div class="pictures__title" v-html="image.caption"></div>
        </figcaption>
      </figure>
    </div>

    <div class="promo">
      <div class="promo__title">Like what you see?</div>
      <div class="promo__subtitle">Check out one of our livestreams!</div>
      <a class="promo__button" :href="this.livestream_link">Visit</a>
    </div> 
  </div>
</template>

<script>
  import { HOMEPAGE } from '../../data/graphql.js';

  export default {
    name: 'HomePage',
    data() {
      return {
        about_section_one: '',
        about_section_two: '',
        featuredImages: [],
        livestream_link: '',
        background: ''
      }
    },
    apollo: {
      featuredImages: {
        query: HOMEPAGE,
        update: function(data) {
          let images = [];
          for (const doc of data.homepage.images) {
            images.push({
              url: doc.featured_image.url,
              caption: doc.caption[0].text
            });
          }
          return images;
        }
      },
      background: {
        query: HOMEPAGE,
        update: function(data) {
          return data.homepage.background.url;
        }
      },
      about_section_one: {
        query: HOMEPAGE,
        update: function(data) {
          return data.homepage.about_section_one[0].text;
        }
      },
      about_section_two: {
        query: HOMEPAGE,
        update: function(data) {
          return data.homepage.about_section_two[0].text;
        }
      },
      livestream_link: {
        query: HOMEPAGE,
        update: function(data) {
          return data.homepage.livestream_link[0].text;
        }
      }   
    }
  }
</script>
