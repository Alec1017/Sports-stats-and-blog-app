<template>
  <div class="players">
    <div class="players__heading row">
        <div class="players__title col-md-8 text-center">
	        <h1>Players <small>2019 Season</small></h1>
        </div>
    </div>
    <div class="players__grid">
        <!-- eslint-disable-next-line vue/require-v-for-key -->
        <div class="players__player card" v-for="team in teams">
          <img class="players__image card-img-top" :src="team.image" :alt="team.captain" height="215">
          <div class="players__content card-body">
              <h5 class="players__card__title card-title">{{ team.captain }}</h5>
              <p class="players__card__text card-text"><b>{{ team.role }}</b><br/>{{ team.description }}</p>
          </div>
          <div class="players__card__footer card-footer">
              <router-link class="btn btn-primary" :to="`/stats/${team.captain.split(' ').join('-')}`">2019 stats</router-link>
          </div>
        </div>
      
    </div>
  </div>
</template>

<script>
  import axios from 'axios';

  export default {
    data() {
      return {
        teams: []
      }
    },
    created() {
      this.getTeams();
    },
    methods: {
      getTeams() {
        axios.get(this.$api + '/players')
          .then((res) => {
            this.teams = res.data;
          })
          .catch((error) => {
            console.error(error);
          });
      }
    }
  }
</script>
