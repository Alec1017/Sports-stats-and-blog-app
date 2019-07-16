<template>
  <div class="navbar">
    <div class="navbar__inner">
      <div class="navbar__logo">
        <router-link to="/">WBL</router-link>
      </div>
      <input class="navbar__toggle" id="navbar-toggle" type="checkbox">
      <label class="navbar__hamburger" for="navbar-toggle">
        <span></span>
      </label>
      <ul class="navbar__list">
        <li>
          <div class="navbar__link">
            <router-link to="/feed">Feed</router-link>
          </div>
        </li>
        <li>
          <div class="navbar__link">
            <router-link to="/players">Players</router-link>
          </div>
        </li>
        <li>
          <div class="navbar__link">
            <router-link to="/standings">Standings</router-link>
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
    components: {
      TwitterSVG
    }
  }
</script>
