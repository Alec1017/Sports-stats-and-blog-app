<template>
  <div class="standings row">
      <div class="standings__inner col-md-8 text-center">
          <h1>Standings <small>2019 Season</small></h1>
          <table class="standings__table table table-striped table-bordered">
            <thead>
              <tr>
                <th>Captain</th>
                <th>Record</th>
                <th>plus/minus</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="team in teams">
                <td>{{ team.captain }}</td>
                <td>{{ team.wins }}-{{ team.losses }}</td>
                <td>{{ team.differential }}</td>
              </tr>
            </tbody>
          </table>
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
        axios.get(this.$api + '/standings')
          .then((res) => {
            this.teams = res.data;
            console.log(this.teams);
          })
          .catch((error) => {
            console.error(error);
          });
      }
    }
  }
</script>