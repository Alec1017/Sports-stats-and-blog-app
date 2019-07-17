<template>
  <div class="players">
    <div class="players__heading">
        <div class="players__title">Players</div>
    </div>
    <div class="players__grid">
        <!-- eslint-disable-next-line vue/require-v-for-key -->
        <div class="card" v-for="player in this.players">
          <img class="card__image" :src="player.profile_picture.url" :alt="player.captain[0].text" height="215">
          <div class="card__title">{{ player.captain[0].text }}</div>
          <div class="card__role">{{ player.role[0].text }}</div>
          <div class="card__description">{{ player.description[0].text }}</div>
          <router-link class="card__button" :to="`/stats/${player._meta.uid}`">2019 stats</router-link>
          <ul class="card__social_media">
            <li><a href="#"><i class="fab fa-facebook-square"></i></a></li>
            <li><a href="#"><i class="fab fa-twitter-square"></i></a></li>
            <li><a href="#"><i class="fab fa-instagram"></i></a></li>
          </ul>
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
