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
              <tr v-for="player in players">
                <td>{{ player.captain }}</td>
                <td>{{ player.wins }}-{{ player.losses }}</td>
                <td>{{ player.differential }}</td>
              </tr>
            </tbody>
          </table>
      </div>
  </div>
</template>

<script>
  import { STANDINGS } from '../../data/graphql.js';

  export default {
    data() {
      return {
        players: []
      }
    },
    apollo: {
      players: {
        query: STANDINGS,
        update: function(data) {
          return data.allFblPlayers.sort((a, b) => (a.wins < b.wins) ? 1 : (a.wins === b.wins)
          ? ((a.differential < b.differential) ? 1 : -1) : -1); 
        }
      }   
    }
  }
</script>