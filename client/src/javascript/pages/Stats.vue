<template>
  <div class="stats" v-if="playerExists">

    <img class="stats__image" :src="player.profile_picture.url" :alt="player.captain[0].text">
    <div class="stats__name">{{ player.captain[0].text }}</div>
    <div class="stats__info">Bat: {{player.batting_direction}} | Throw: {{player.throw_direction}} | height: {{player.height}}" | Age: {{player.age}}</div>

    <div class="stats__bio">
      <div class="stats__bio_category">Status: <span class="stats__bio_data">{{player.status}}</span></div>
      <div class="stats__bio_category">Debut: <span class="stats__bio_data">{{ parseInt(player.debut)}}</span></div>
      <div class="stats__bio_category">Awards: <span class="stats__bio_data">{{player.awards}}</span></div>
      <div class="stats__bio_category">championships: <span class="stats__bio_data">{{player.championship_titles}}</span></div>
    </div>

    <div class="tab">
      <input class="tab__input tab__input--hitting" id="tab-hitting" type="radio" name="tabs" checked>
      <label class="tab__label" for="tab-hitting">Hitting</label>

      <input class="tab__input tab__input--pitching" id="tab-pitching" type="radio" name="tabs">
      <label class="tab__label" for="tab-pitching">Pitching</label>

      <div class="tab__content tab__content--hitting">Hitting coming soon to a theater near you</div>
      <div class="tab__content tab__content--pitching">Pitching coming soon to a theater near you</div>
    </div>
     





   <!-- <div class="row">
      <div class="stats__bio col-3">
        <h6>Status: <span style="color: gray">{{player.status}}</span></h6>
        <h6>Debut: <span style="color: gray">{{player.debut}}</span></h6>
        <h6>Awards: <span style="color: gray">{{player.awards}}</span></h6>
        <h6>championships: <span style="color: gray">{{player.championship_titles}}</span></h6>
      </div>
      <div class="col-9">
        <ul class="nav nav-tabs">
          <li class="nav-item">
            <a class="nav-link active" data-toggle="tab" href="#hitting">Hitting</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" data-toggle="tab" href="#pitching">Pitching</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" data-toggle="tab" href="#analytics">Analytics</a>
          </li>
        </ul>

       
       <div class="tab-content">

          <div id="hitting" class="tab-pane fade show active">
            <table class="stats__table table table-striped table-bordered">
              <thead>
                <tr>
                  <th scope="col" class="text-center">H</th>
                  <th scope="col" class="text-center">AB</th>
                  <th scope="col" class="text-center">1B</th>
                  <th scope="col" class="text-center">2B</th>
                  <th scope="col" class="text-center">3B</th>
                  <th scope="col" class="text-center">HR</th>
                  <th scope="col" class="text-center">HBP</th>
                  <th scope="col" class="text-center">BB</th>
                  <th scope="col" class="text-center">RBI</th>
                  <th scope="col" class="text-center">K</th>
                  <th scope="col" class="text-center">SB</th>
                  <th scope="col" class="text-center">OUTS</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td>{{ player.h }}</td>
                  <td>{{ player.ab }}</td>
                  <td>{{ player.one_b }}</td>
                  <td>{{ player.two_b }}</td>
                  <td>{{ player.three_b }}</td>
                  <td>{{ player.hr }}</td>
                  <td>{{ player.hbp }}</td>
                  <td>{{ player.bb }}</td>
                  <td>{{ player.rbi }}</td>
                  <td>{{ player.k }}</td>
                  <td>{{ player.sb }}</td>
                  <td>{{ player.outs }}</td>
                </tr>
              </tbody>
            </table>

            <table class="stats__table table table-striped table-bordered">
                <thead>
                    <tr>
                        <th scope="col" class="text-center">AVG</th>
                        <th scope="col" class="text-center">OBP</th>
                        <th scope="col" class="text-center">SLG</th>
                        <th scope="col" class="text-center">OPS</th>
                    </tr>
                </thead>
                <tbody>
                  <tr>
                    <td v-html="calcAVG"></td>
                    <td v-html="calcOBP"></td>
                    <td v-html="calcSLG"></td>
                    <td v-html="calcOPS"></td>
                  </tr>
                </tbody>
            </table>
          </div>

          <div id="pitching" class="tab-pane fade">
            <table class="stats__table table table-striped table-bordered">
              <thead>
                <tr>
                  <th scope="col" class="text-center">IP</th>
                  <th scope="col" class="text-center">ER</th>
                  <th scope="col" class="text-center">R</th>
                  <th scope="col" class="text-center">K</th>
                  <th scope="col" class="text-center">BB</th>
                  <th scope="col" class="text-center">SV</th>
                  <th scope="col" class="text-center">W</th>
                  <th scope="col" class="text-center">L</th>
                  <th scope="col" class="text-center">ERA</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td>{{ player.ip }}</td>
                  <td>{{ player.er }}</td>
                  <td>{{ player.r }}</td>
                  <td>{{ player.pitching_k }}</td>
                  <td>{{ player.pitching_bb }}</td>
                  <td>{{ player.sv }}</td>
                  <td>{{ player.pitching_wins }}</td>
                  <td>{{ player.pitching_losses }}</td>
                  <td v-html="calcERA"></td>
                </tr>
              </tbody>
            </table>
          </div>
          <div id="analytics" class="tab-pane fade">
            <h3>Coming soon to a theater near you</h3>
          </div>
        </div>
      </div> 
    </div> -->
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
      },
      calcAVG() {
        if (this.player.ab > 0) {
          let avg = this.player.h / this.player.ab;
          return avg.toFixed(3);
        } else {
          return 'undefined';
        }
      },
      calcOBP() {
        const bases = this.player.h + this.player.bb + this.player.hbp;
        const denom = this.player.ab + this.player.bb + this.player.hbp;

        if (denom > 0) {
          let obp = bases / denom;
          return obp.toFixed(3);
        } else {
          return 'Undefined';
        }
      },
      calcSLG() {
        const totalBases = this.player.one_b + (2 * this.player.two_b) + (3 * this.player.three_b) + (4 * this.player.hr);

        if (this.player.ab > 0) {
          let slg = totalBases / this.player.ab;
          return slg.toFixed(3);
        } else {
          return 'Undefined';
        }
      },
      calcOPS() {
        if (isNaN(this.calcOBP) || isNaN(this.calcSLG)) {
          return 'Undefined';
        } else {
          let ops = parseFloat(this.calcOBP) + parseFloat(this.calcSLG);
          return ops.toFixed(3);
        }
      },
      calcERA() {
        if (this.player.ip > 0) {
          let era = 3 * this.player.er / this.player.ip;
          return era.toFixed(2);
        } else {
          return 'Undefined';
        }
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