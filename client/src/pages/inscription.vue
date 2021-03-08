<template>
<div class>
  
  <b-container fluid="xl" class="col d-flex justify-content-center">
      <b-form @submit="onSubmit" @reset="onReset"  oninput='up2.setCustomValidity(up2.value != up.value ? "Passwords do not match." : "")' >

        <b-form-group
          id="input-group-1" label="Adresse email:" label-for="input-1" description="Le mail ne sera pas partagé aux autres utilisateurs">
          <b-form-input
            id="input-1"
            v-model="form.email"
            type="email"
            placeholder="Adresse email"
            required
            size="xs"
          ></b-form-input>
        </b-form-group>

        <b-form-group id="input-group-2" label="Mot de passe:" label-for="input-2" aria-describedby="password-help-block">
          <b-form-input
            id="input-2"
            type="password"
            v-model="form.password"
            placeholder="Entez votre mot de passe"
            name="up"
            required
          ></b-form-input>
          <b-form-text id="password-help-block">
            Votre mot de passe doit contenir bla bla bla
          </b-form-text>
        </b-form-group>

        <b-form-group id="input-group-3" label="Confirmation mot de passe:" label-for="input-3" aria-describedby="password-help-block">
          <b-form-input
            id="input-3"
            type="password"
            v-model="form.rePassword"
            placeholder="Répétez votre mot de passe"
            name="up2"
            required
          ></b-form-input>
        </b-form-group>
      
        <b-form-group id="input-group-4" label="Nom d'utilisateur:" label-for="input-4" description="Ce nom sera visible par les autres utilisateurs">
          <b-form-input
            id="input-4"
            v-model="form.userName"
            placeholder="Entez votre nom"
            required
          ></b-form-input>
        </b-form-group>



        <b-form-group id="input-group-5" label="Sexe:" label-for="input-5">
          <b-form-select
            id="inline-form-custom-select-pref"
            v-model="form.sexe"
            class="mb-2 mr-sm-2 mb-sm-0"
            :options="[{ text: 'Désignez votre sexe' },'Homme', 'Femme', 'Autre']"
            :value="null">
          </b-form-select>
        </b-form-group>

        <b-button type="submit" variant="primary">S'inscrire</b-button>
        <b-button type="reset" variant="danger">Réinitialiser</b-button>
        
      </b-form>
  </b-container>
  
   

</div>
</template>

<script>
  export default {
    data() {
      return {
        form: {
          email: '',
          password: '',
          rePassword: '',
          userName: '',
          sexe: this.sexe,
        },
      }
    },
    methods: {
      onSubmit(event) {
        event.preventDefault()
        alert(JSON.stringify(this.form))
      },
      onReset(event) {
        event.preventDefault()
        // Reset our form values
        this.form.email = ''
        this.form.name = ''
        this.form.password = ''
        this.form.rePassword = ''
        this.form.sexe = null
        // Trick to reset/clear native browser form validation state
        this.show = false
        this.$nextTick(() => {
          this.show = true
        })
      },
    }
  }
</script>

<style scoped>

    @media screen and (max-height: 670px) {
        .normal-screen{
            display: none;
        }
    }
  
</style>