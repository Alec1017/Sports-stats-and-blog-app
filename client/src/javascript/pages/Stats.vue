<template>
  <div class="stats">
    <div class="row">
      <div class="col-3">
        <img class="stats__image card-img-top" :src="team.image" :alt="team.captain" height="215">
      </div>
      <div class="col-9" style="padding-top: 3rem">
        <h1>{{ team.captain }}</h1>
        <h4 style="color: gray">Bat: R | Throw: R | height | Age: 20</h4>
      </div>
    </div>
    <div class="row">
      <div class="stats__bio col-3">
        <h6>Status: <span style="color: gray">Active</span></h6>
        <h6>Debut: <span style="color: gray">Some Date</span></h6>
        <h6>Awards: <span style="color: gray">MVP</span></h6>
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
                      <th scope="col" class="text-center">completions</th>
                      <th scope="col" class="text-center">attempts</th>
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
                  <td>{{ team.completions }}</td>
                  <td>{{ team.attempts }}</td>
                  <td>{{ team.completionPercentage }}</td>
                  <td>{{ team.passTouchdowns }}</td>
                  <td>{{ team.thrownInterceptions }}</td>
                  <td>{{ team.receptions }}</td>
                  <td>{{ team.receivingTouchdowns }}</td>
                  <td>{{ team.rushingTouchdowns }}</td>
                  <td>{{ team.caughtInterceptions }}</td>
                  <td>{{ team.sacks }}</td>
                  <td>{{ team.gamesPlayed }}</td>
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
  import axios from 'axios';

  export default {
    data() {
      return {
        team: {}
      }
    },
    created() {
      this.getTeam();
    },
    methods: {
      getTeam() {
        axios.get(this.$api + `/stats/${this.$route.params.player.split(' ').join('-')}`)
          .then((res) => {
            this.team = res.data;
          })
          .catch((error) => {
            console.error(error);
          });
      }
    }
  } 
</script>