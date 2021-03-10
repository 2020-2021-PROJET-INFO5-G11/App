<template>  
    <div class="container" >
      <body>
      <b-form-group
        id="input-group-1" label="Adresse email:">
        <b-form-input
          id="input-1"
          required
          v-model="form.username"
        ></b-form-input>
      </b-form-group>

      <b-form-group
        id="input-group-2" label="Mot de passe:">
        <b-form-input
          id="input-2"
          required
          v-model="form.password"
        ></b-form-input>
      </b-form-group>

      <b-button variant="primary">Connexion</b-button>

  <b-button v-b-modal.modal-1 variant="primary">Inscription</b-button>
  <b-modal id="modal-1" hide-footer>
    <Inscription/>
  </b-modal>

      </body>


  </div>
</template>

<script>
import { mapActions } from "vuex";
import Inscription from './inscription.vue';

export default {
  name: "Login",
  components: { Inscription },
  data() {
    return {
      form: {
        userName: '',
        password: '',
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
    ...mapActions(["LogIn"]),
    async submit() {
      const User = new FormData();
      User.append("username", this.form.username);
      User.append("password", this.form.password);
      try {
          await this.LogIn(User);
          this.$router.push("/accueil");
          this.showError = false
      } catch (error) {
        this.showError = true
      }
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