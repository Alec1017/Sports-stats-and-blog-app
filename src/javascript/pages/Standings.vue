<template>
  <div class="standings" v-if="this.divisions">
      
    <div class="standings__heading">
      <div class="standings__title">Standings</div>
    </div>

    <div class="standings__division" v-for="division in this.divisions" >
      <div class="standings__division_heading">
        <div class="standings__division_title">Division {{ division }}</div>
      </div>

      <table class="table">
        <thead class="table__head">
          <tr class="table__row standings__row">
            <th>Captain</th>
            <th>Wins</th>
            <th>Losses</th>
          </tr>
        </thead>
        <tbody class="table__body">
          <tr class="table__row standings__row" v-for="player in filterByDivision(division)">
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
  import { WBLPLAYERS, STANDINGS, cleanCollection } from '../../data/graphql.js';

  export default {
    data() {
      return {
        players: [],
        divisions: 0
      }
    },
    methods: {
      filterByDivision(division) {
        return this.players.filter((player) => {
          return player.division === division;
        })
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
      },
      divisions: {
        query: STANDINGS,
        update: function(data) {
          return data.standings.divisions;
        }
      }   
    }
  }
</script>