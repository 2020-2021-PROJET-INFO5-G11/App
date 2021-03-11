<template>  
    <div class="container" >
      <body>
      <b-form-group
        id="input-group-1" label="Adresse email:">
        <b-form-input
          id="input-1"
          required
          v-model="email"
        ></b-form-input>
      </b-form-group>

      <b-form-group
        id="input-group-2" label="Mot de passe:">
        <b-form-input
          id="input-2"
          required
          v-model="password"
        ></b-form-input>
      </b-form-group>

      <b-button variant="primary" @click="login">Connexion</b-button>

  <b-button v-b-modal.modal-1 variant="primary">Inscription</b-button>
  <b-modal id="modal-1" hide-footer>
    <Inscription/>
  </b-modal>

      </body>


  </div>
</template>

<script>
import axios from 'axios'
import Vuex from 'vuex'
import Inscription from './inscription.vue';

export default {
  name: 'login',
  components: { Inscription },
  data() {
    return {
      email: '',
      password: '',
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
    login(){
      var email_login = this.email
      var password_login = this.password
      const path = 'http://localhost:5000/api/user/login'
      return new Promise((resolve, reject) => {
            axios.get(path, {
              params: { email: email_login, password: password_login }
            },{
            headers: {
              'Access-Control-Allow-Origin': '*',
              'Content-Type': 'application/json',
            },
            })
            .then(response => {
                const token = response.data.access_token
                localStorage.setItem('access_token', token)
                resolve(response);
                this.$router.push('/accueil');
            })
            .catch(error => {
                reject(error)
            })
        })
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