<template>
  <div class="standings">
      
    <div class="standings__heading">
      <div class="standings__title">Standings</div>
    </div>

    <table class="standings__table">
      <thead class="standings__head">
        <tr class="standings__row">
          <th>Captain</th>
          <th>Wins</th>
          <th>Losses</th>
        </tr>
      </thead>
      <tbody class="standings__body">
        <tr class="standings__row" v-for="player in players">
          <td>{{ player.captain[0].text }}</td>
          <td>{{ player.wins }}</td>
          <td>{{ player.losses }}</td>
        </tr>
      </tbody>
    </table>
    
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