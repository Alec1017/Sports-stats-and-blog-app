<template>
  <div class="standings row">
      <div class="standings__inner col-md-8 text-center">
          <h1>Standings <small>2019 Season</small></h1>
          <table class="standings__table table table-striped table-bordered">
            <thead>
              <tr>
                <th>Captain</th>
                <th>Wins</th>
                <th>Losses</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="player in players">
                <td>{{ player.captain[0].text }}</td>
                <td>{{ player.wins }}</td>
                <td>{{ player.losses }}</td>
              </tr>
            </tbody>
          </table>
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
          let cleanedPlayers = cleanCollection(data.allWbl_players);

          return cleanedPlayers.sort((a, b) => (a.wins < b.wins) ? 1 : (a.wins === b.wins)
          ? ((a.losses > b.losses) ? 1 : -1) : -1); 
        }
      }   
    }
  }
</script>