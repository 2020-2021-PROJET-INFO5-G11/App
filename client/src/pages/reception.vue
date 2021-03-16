<template>
    <div>

      <div class="row headBand">
        <div style="text-align: center;" class="col-md-auto">
          <img class="fit-picture" src="../logo_blanc.png"  >
        </div>
        <div class="col-md-auto">
          <br>
          <h1> Bienvenue </h1>
        </div>


        <b-form-group
          id="input-group-1" label="Adresse email:">
          <b-form-input
            id="input-1"
            required
          ></b-form-input>
        </b-form-group> 
        
        <b-form-group
        
          id="input-group-2" label="Mot de passe:"  aria-describedby="password-help-block">
          <b-form-input
            id="input-2"
            type="password"
            required
          ></b-form-input>
        </b-form-group>

        <b-button variant="primary" class="b1">Connexion</b-button>
      </div>

      <b-container>
        <img src="../reception.jpg"/>
      </b-container>

      <Footer/>

    </div>
</template>



<script>

import Footer from './footer.vue';

export default {
  
  components: { Footer },

  }

</script>


<style>
  img {
    width: 100%;
    height: auto;
  }

  .fit-picture {
    width: 33%;
    float : left;
  }

  .titre {
    float: left;
  }

 .headBand {
  padding: 100 px;
  background-color: rgb(65, 192, 171);
  color: rgb(245, 245, 245);
}

  .col-md-auto {
     text-align: center;
  }

  .connexion-1 {
     text-align: center;
     width: 50%;
     height : 100%
  }

  .b1 {
    height:100%;
  }
</style>