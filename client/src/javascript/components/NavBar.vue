<template>
 <!-- <nav class="navbar navbar-expand-sm navbar-dark bg-dark">
      <div class="container">
          <a class="navbar-brand" href="/">WBL</a>
          <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbar" aria-controls="navbarText" aria-expanded="false" aria-label="Toggle navigation">
              <span class="navbar-toggler-icon"></span>
          </button>

          <div class="collapse navbar-collapse" id="navbar"> -->
              <!-- left side of the navbar -->
          <!--    <ul class="navbar-nav mr-auto">
                  <li class="nav-item">
                      <router-link class="nav-link" to="/feed">Feed</router-link>
                  </li>
                  <li class="nav-item">
                      <router-link class="nav-link" to="/players">Players</router-link>
                  </li>
                  <li class="nav-item">
                      <router-link class="nav-link" to="/standings">Standings</router-link>
                  </li>
              </ul> -->

              <!-- right side of the navbar -->
            <!--  <ul class="navbar-nav navbar-right"> -->
                <!-- only display the logout button if user is admin-->
           <!--         <li class="nav-item">
                        <a class="nav-link" href="https://twitter.com/FBLWBL2019" style="padding: 0px;">
                            <TwitterSVG />
                        </a>
                    </li>
              </ul>
          </div>
      </div> 
  </nav>  --> 

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
      </ul>
    </div>
  </div>
</template>

<script>
  import LogoSVG from '../../static/vectors/logo.svg';
  import TwitterSVG from '../../static/vectors/twitter.svg';

  export default {
    name: 'navBar',
    components: {
      LogoSVG,
      TwitterSVG
    }
  }
</script>
