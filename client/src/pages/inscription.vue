<template>

<div class="container" >
    
   <b-form @submit="onSubmit" @reset="onReset" >

    <b-form-group
        id="input-group-1" label="Email address:" label-for="input-1" description="Le mail ne sera pas partagé aux autres utilisateurs">
        <b-form-input
          id="input-1"
          v-model="form.email"
          type="email"
          placeholder="Adresse email"
          required
        ></b-form-input>
      </b-form-group>

      <b-form-group id="input-group-2" label="Mot de passe:" label-for="input-2" aria-describedby="password-help-block">
        <b-form-input
          id="input-2"
          type="password"
          v-model="form.password"
          placeholder="Entez votre mot de passe"
          required
        ></b-form-input>
        <b-form-text id="password-help-block">
      Votre mot de passe doit contenir bla bla bla
    </b-form-text>
      </b-form-group>

      <b-form-group id="input-group-3" label="Répétez votre mot de passe:" label-for="input-3" aria-describedby="password-help-block">
        <b-form-input
          id="input-3"
          type="password"
          v-model="form.rePassword"
          placeholder="Répétez votre mot de passe"
          required
        ></b-form-input>
      </b-form-group>

      <b-button type="password" @click="switchVisibility">show / hide</b-button>
      

      <b-form-group id="input-group-4" label="Nom:" label-for="input-4" description="Ce nom sera visible par les autres utilisateurs">
        <b-form-input
          id="input-4"
          v-model="form.name"
          placeholder="Entez votre nom"
          required
        ></b-form-input>
      </b-form-group>

      
      <b-button type="submit" variant="primary">S'inscrire</b-button>
      <b-button type="reset" variant="danger">Réinitialiser</b-button>
    </b-form>
    

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
          passwordFieldType: 'password',
          name: '',
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
        // Trick to reset/clear native browser form validation state
        this.show = false
        this.$nextTick(() => {
          this.show = true
        })
      },
      passwordConfirmationRule() {
      return () => (this.password === this.rePassword) || 'Password must match'
    },
      switchVisibility() {
        this.passwordFieldType = this.passwordFieldType === 'password' ? 'text' : 'password'
      },
    }
  }
</script>

