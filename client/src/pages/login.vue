<template>  
    <div class="container" >
      <body>
      <b-form-group
        id="input-group-1" label="Adresse email:" v-model="username">
        <b-form-input
          id="input-1"
          required
        ></b-form-input>
      </b-form-group>

      <b-form-group
        id="input-group-2" label="Mot de passe:" v-model="password">
        <b-form-input
          id="input-2"
          required
        ></b-form-input>
      </b-form-group>

      <b-button variant="primary" @click="login()">Connexion</b-button>

  <b-button v-b-modal.modal-1 variant="primary" >Inscription</b-button>
  <b-modal id="modal-1" hide-footer>
    <Inscription/>
  </b-modal>

      </body>


  </div>
</template>

<script>

import axios from 'axios';
import Inscription from './inscription.vue';

export default {
  
  components: { Inscription },
  data() {
    return {
      user: {
        username: '',
        password: '',
        pseudo: '',
        gender: '',
      },
    };
  },
  mounted() {},
  computed: {
    win_width() {
      return this.$q.screen.width - 59;
    },
    win_height() {
      return this.$q.screen.height - 0;
    },
  },
  methods: {
    login() {
      console.log(this.username);
      const path = 'http://localhost:5000/api/user/login';
      const params = {username : this.username, password : this.password};
      axios.get(path, { params })
        .then((res) => {
          this.user = res.data;
        })
        .catch((error) => {
          console.error(error);
        });
    },
    subscribe() {
      const path = 'http://localhost:5000/api/user';
      const params = {username : this.username, password : this.password};
      axios.post(path, { params })
        .then((res) => {
          this.user = res.data;
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
};
</script>

<style>
.modal-backdrop
{
    opacity:0.5 !important;
}

    @media screen and (max-height: 670px) {
        .normal-screen{
            display: none;
        }
    }

</style>