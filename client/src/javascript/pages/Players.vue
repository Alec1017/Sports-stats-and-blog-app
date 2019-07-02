<template>
  <div class="players">
    <div class="players__heading row">
        <div class="players__title col-md-8 text-center">
	        <h1>Players <small>2019 Season</small></h1>
        </div>
    </div>
    <div class="players__grid">
        <!-- eslint-disable-next-line vue/require-v-for-key -->
        <div class="players__player card" v-for="player in players">
          <img class="players__image card-img-top" :src="player.image" :alt="player.captain" height="215">
          <div class="players__content card-body">
              <h5 class="players__card__title card-title">{{ player.captain }}</h5>
              <p class="players__card__text card-text"><b>{{ player.role }}</b><br/>{{ player.description }}</p>
          </div>
          <div class="players__card__footer card-footer">
              <router-link class="btn btn-primary" :to="`/stats/${player.captain.split(' ').join('-')}`">2019 stats</router-link>
          </div>
        </div>
      
    </div>
  </div>
</template>

<script>
  import { PLAYERS } from '../../data/graphql.js';

  export default {
    data() {
      return {
        players: []
      }
    },
    methods: {
      getContent() {
        this.$prismic.client.query(
          this.$prismic.Predicates.at('document.type', 'wbl_player')
        ).then((document) => {
          if (document) {
            for (const doc of document.results) {
              let player = {
                captain: '', 
                role: '',
                description: '',
                image: ''
              }

              player.captain = doc.data.captain[0].text;
              player.role = doc.data.role[0].text;
              player.description = doc.data.description[0].text;
              player.image = doc.data.profile_picture.url;
              this.players.push(player);
            }
          }
        })
      }
    },
    created() {
      this.getContent();
    }
  }
</script>
