<template>
  <div class="stats" v-if="playerExists">

    <img class="stats__image" :src="player.profile_picture.url" :alt="player.captain[0].text">
    <div class="stats__basic_info">
      <div class="stats__name">{{ player.captain[0].text }}</div>
      <div class="stats__info">Bat: {{player.batting_direction}} | Throw: {{player.throw_direction}} | height: {{player.height}}" | Age: {{player.age}}</div>

      <div class="stats__bio">
        <div class="stats__bio_category">Status: <span class="stats__bio_data">{{player.status}}</span></div>
        <div class="stats__bio_category">Debut: <span class="stats__bio_data">{{ parseInt(player.debut)}}</span></div>
        <div class="stats__bio_category">Awards: <span class="stats__bio_data">{{player.awards}}</span></div>
        <div class="stats__bio_category">championships: <span class="stats__bio_data">{{player.championship_titles}}</span></div>
      </div>
    </div>

   

    <div class="tab">
      <input class="tab__input tab__input--hitting" id="tab-hitting" type="radio" name="tabs" checked>
      <label class="tab__label" for="tab-hitting">Hitting</label>

      <input class="tab__input tab__input--pitching" id="tab-pitching" type="radio" name="tabs">
      <label class="tab__label" for="tab-pitching">Pitching</label>

      <input class="tab__input tab__input--analytics" id="tab-analytics" type="radio" name="tabs">
      <label class="tab__label" for="tab-analytics">Analytics</label>

      <!-- hitting tab -->
      <div class="tab__content tab__content--hitting">
        <table class="table stats__table stats__condensed-data">
          <thead class="table__head">
            <tr class="table__row">
              <th>H</th>
              <th>AB</th>
              <th>HR</th>
              <th>RBI</th>
              <th>K</th>
            </tr>
          </thead>
          <tbody class="table__body">
            <tr class="table__row">
              <td>{{ player.h }}</td>
              <td>{{ player.ab }}</td>
              <td>{{ player.hr }}</td>
              <td>{{ player.rbi }}</td>
              <td>{{ player.k }}</td>
            </tr>
          </tbody>
        </table>

        <table class="table stats__table stats__full-data">
          <thead class="table__head">
            <tr class="table__row">
              <th>H</th>
              <th>AB</th>
              <th>1B</th>
              <th>2B</th> 
              <th>3B</th>
              <th>HR</th>
              <th>HBP</th>
              <th>BB</th>
              <th>RBI</th>
              <th>K</th>
              <th>SB</th>
              <th>OUTS</th>
            </tr>
          </thead>
          <tbody class="table__body">
            <tr class="table__row">
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

        <table class="table stats__table">
          <thead class="table__head">
            <tr class="table__row">
              <th>AVG</th>
              <th>OBP</th>
              <th>SLG</th>
              <th>OPS</th>
            </tr>
          </thead>
          <tbody class="table__body">
            <tr class="table__row">
              <td v-html="calcAVG"></td>
              <td v-html="calcOBP"></td>
              <td v-html="calcSLG"></td>
              <td v-html="calcOPS"></td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- pitching tab -->
      <div class="tab__content tab__content--pitching">
        <table class="table stats__table stats__condensed-data">
          <thead class="table__head">
            <tr class="table__row">
              <th>IP</th>
              <th>ER</th>
              <th>R</th>
              <th>K</th>
              <th>BB</th>
            </tr>
          </thead>
          <tbody class="table__body">
            <tr class="table__row">
              <td>{{ player.ip }}</td>
              <td>{{ player.er }}</td>
              <td>{{ player.r }}</td>
              <td>{{ player.pitching_k }}</td>
              <td>{{ player.pitching_bb }}</td>
            </tr>
          </tbody>
        </table>

        <table class="table stats__table stats__condensed-data">
          <thead class="table__head">
            <tr class="table__row">
              <th>ERA</th>
              <th>W</th>
              <th>L</th>
              <th>SV</th>
            </tr>
          </thead>
          <tbody class="table__body">
            <tr class="table__row">
              <td v-html="calcERA"></td>
              <td>{{ player.pitching_wins }}</td>
              <td>{{ player.pitching_losses }}</td>
              <td>{{ player.sv }}</td>
            </tr>
          </tbody>
        </table>

        <table class="table stats__table stats__full-data">
          <thead class="table__head">
            <tr class="table__row">
              <th>IP</th>
              <th>ER</th>
              <th>R</th>
              <th>ERA</th>
              <th>K</th>
              <th>BB</th>
              <th>W</th>
              <th>L</th>
              <th>SV</th>
            </tr>
          </thead>
          <tbody class="table__body">
            <tr class="table__row">
              <td>{{ player.ip }}</td>
              <td>{{ player.er }}</td>
              <td>{{ player.r }}</td>
              <td v-html="calcERA"></td>
              <td>{{ player.pitching_k }}</td>
              <td>{{ player.pitching_bb }}</td>
              <td>{{ player.pitching_wins }}</td>
              <td>{{ player.pitching_losses }}</td>
              <td>{{ player.sv }}</td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- analytics tab -->
      <div class="tab__content tab__content--analytics">
        Analytics will becoming soon!
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