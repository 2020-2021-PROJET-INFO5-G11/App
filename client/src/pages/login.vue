<template>
  
    <div fluid="xl" class="col d-flex justify-content-center">
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
  <b-modal id="modal-1" hide-footer>
    <Inscription/>
  </b-modal>

      </body>


  </div>
  
</template>

<script>

import Inscription from './inscription.vue';

export default {
  
  components: { Inscription },
  data() {
    return {
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