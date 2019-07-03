<template>
  <div class="players">
    <div class="players__heading row">
        <div class="players__title col-md-8 text-center">
	        <h1>Players <small>2019 Season</small></h1>
        </div>
    </div>
    <div class="players__grid">
        <!-- eslint-disable-next-line vue/require-v-for-key -->
        <div class="players__player card" v-for="player in this.players">
          <img class="players__image card-img-top" :src="player.profile_picture.url" :alt="player.captain[0].text" height="215">
          <div class="players__content card-body">
              <h5 class="players__card__title card-title">{{ player.captain[0].text }}</h5>
              <p class="players__card__text card-text"><b>{{ player.role[0].text }}</b><br/>{{ player.description[0].text }}</p>
          </div>
          <div class="players__card__footer card-footer">
              <router-link class="btn btn-primary" :to="`/stats/${player.captain[0].text.split(' ').join('-').toLowerCase()}`">2019 stats</router-link>
          </div>
        </div>
      
    </div>
  </div>
</template>

<script>
  import { WBLPLAYERS, cleanCollection } from '../../data/graphql.js';

  export default {
    data() {
      return {
        players: []
      }
    },
    apollo: {
      players: {
        query: WBLPLAYERS,
        update: function(data) {
          return cleanCollection(data.allWbl_players);
        }
      }   
    }
  }
</script>
