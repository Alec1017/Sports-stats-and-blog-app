<template>
  <div class="navbar">
    <div class="navbar__inner">
      <div class="navbar__logo">
        <router-link v-on:click.native="closeNav" to="/">WBL</router-link>
      </div>
      <div class="navbar__hamburger" @click="toggleNav">
        <span></span>
      </div>
      <ul class="navbar__list" v-bind:class="{ isOpen: this.navOpen }">
        <li>
          <div class="navbar__link">
            <router-link v-on:click.native="closeNav" to="/feed">Feed</router-link>
          </div>
        </li>
        <li>
          <div class="navbar__link">
            <router-link v-on:click.native="closeNav" to="/players">Players</router-link>
          </div>
        </li>
        <li>
          <div class="navbar__link">
            <router-link v-on:click.native="closeNav" to="/standings">Standings</router-link>
          </div>
        </li>
        <li>
          <div class="navbar__link navbar__link--twitter_text">
            <a href="https://twitter.com/FBLWBL2019">Twitter</a>
          </div>
          <div class="navbar__link navbar__link--twitter_logo">
            <a href="https://twitter.com/FBLWBL2019"><TwitterSVG /></a>
          </div>
        </li>
      </ul>
    </div>
  </div> 
</template>

<script>
  import TwitterSVG from '../../static/vectors/twitter.svg';

  export default {
    name: 'navBar',
    data() {
      return {
        navOpen: false
      }
    },
    components: {
      TwitterSVG
    },
    methods: {
      toggleNav() {
        this.navOpen = !this.navOpen;
      },
      closeNav() {
        this.navOpen = false;
      }
    }
  }
</script>
