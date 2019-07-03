<template>
  <div class="stats" v-if="playerExists">
    <div class="row">
      <div class="col-3">
        <img class="stats__image card-img-top" :src="player.profile_picture.url" :alt="player.captain[0].text">
      </div>
      <div class="col-9" style="padding-top: 3rem">
        <h1>{{ player.captain[0].text }}</h1>
        <h4 style="color: gray">Bat: {{player.batting_direction}} | Throw: {{player.throw_direction}} | height: {{player.height}}" | Age: {{player.age}}</h4>
      </div>
    </div>
    <div class="row">
      <div class="stats__bio col-3">
        <h6>Status: <span style="color: gray">{{player.status}}</span></h6>
        <h6>Debut: <span style="color: gray">{{player.debut}}</span></h6>
        <h6>Awards: <span style="color: gray">{{player.awards}}</span></h6>
        <h6>championships: <span style="color: gray">{{player.championship_titles}}</span></h6>
      </div>
      <div class="col-9">
        <ul class="nav nav-tabs">
          <li class="nav-item">
            <a class="nav-link active" data-toggle="tab" href="#stats">Stats</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" data-toggle="tab" href="#analytics">Analytics</a>
          </li>
        </ul>

        <!-- Content for the nav -->
       <div class="tab-content">
          <div id="stats" class="tab-pane fade show active">
            <table class="stats__table table table-striped table-bordered">
              <thead>
                  <tr>
                      <th scope="col" class="text-center">Wins</th>
                      <th scope="col" class="text-center">Losses</th>
                      <th scope="col" class="text-center">completion %</th>
                      <th scope="col" class="text-center">pass td</th>
                      <th scope="col" class="text-center">thrown int</th>
                      <th scope="col" class="text-center">receptions</th>
                      <th scope="col" class="text-center">receiving td</th>
                      <th scope="col" class="text-center">rushing td</th>
                      <th scope="col" class="text-center">caught int</th>
                      <th scope="col" class="text-center">sacks</th>
                      <th scope="col" class="text-center">games played</th>
                  </tr>
              </thead>
              <tbody>
                <tr>
                  <td>{{ player.wins }}</td>
                  <td>{{ player.losses }}</td>
                  
                </tr>
              </tbody>
          </table>
          </div>
          <div id="analytics" class="tab-pane fade">
            <h3>Coming soon to a theater near you</h3>
          </div>
        </div>
      </div>
    </div> 
  </div> 
</template>

<script>
  import { GETWBLPLAYER, cleanCollection } from '../../data/graphql.js';

  export default {
    data() {
      return {
        uid: '',
        player: null,
        variables: {}
      }
    },
    computed: {
      playerExists() {
        return this.player;
      }
    },
    apollo: {
      player: {
        query: GETWBLPLAYER,
        variables() {
          return { uid: this.$route.params.player }
        },
        update: function(data) {
          return cleanCollection(data.allWbl_players)[0];
        }
      }   
    }
  } 
</script>