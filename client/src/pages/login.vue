<template>
  
    <div class="container" >
      <body>
      <b-form-group
        id="input-group-1" label="Adresse email:">
        <b-form-input
          id="input-1"
          required
        ></b-form-input>
      </b-form-group>

      <b-form-group
        id="input-group-2" label="Mot de passe:">
        <b-form-input
          id="input-2"
          required
        ></b-form-input>
      </b-form-group>

      <b-button variant="primary">Connexion</b-button>

  <b-button v-b-modal.modal-1 variant="primary">Inscription</b-button>
  <b-modal id="modal-1">
    <Inscription/>
  </b-modal>

      </body>
<Footer />


  </div>
  
</template>

<script>

import Footer from './footer.vue';
import Inscription from './inscription.vue';

export default {
  
  components: { Footer, Inscription },
  data() {
    return {
      username: 'mayu',
      password: 'mayur@qu',
      remember_me: false,
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
};
</script>

<style>
</style>
