<template>
  <div>
    <!-- Inline block list -->
    <ul class="headBand">

      <!-- Left block -->

      <li class="left">
        <div style="text-align: center;" class="col-md-auto">
          <img class="fit-picture" src="../logo_blanc.png"  >
          <h5 style="padding-left: 5px;"> Osons sortir </h5>  
        </div>
      </li>

      <!-- Center block -->

      <li class="center">
        <br><br>
        <h1> L'application d'organisation de vos évènements </h1>
        
      </li>

      <!-- Right block -->

      <li class="right">
        <br>
        <div class="row connexion">
          <b-form-group style="width: 400px" id="input-group-1" label="Adresse email:">
            <b-form-input id="input-1" required></b-form-input>
          </b-form-group>
          
          <b-form-group style="width: 300px; padding-left: 20px;" id="input-group-2" label="Mot de passe:"  aria-describedby="password-help-block">
            <b-form-input id="input-2" type="password" required></b-form-input>
          </b-form-group>   

          <b-form-group style="padding-left: 20px;" id="input-group-1" label="Connexion">
            <b-button @click="$router.push({path: `/accueil`})" variant=primary>
              Se connecter
            </b-button>
          </b-form-group>   
          <b-form-group style="padding-left: 50px;" id="input-group-1" label=""> <br>
            <b-button @click="$bvModal.show('inscription-modal')" variant="secondary">S'inscrire</b-button>
          </b-form-group>   
        </div>   
      </li>

    </ul>

    <b-modal ref="inscription"
              id="inscription-modal"
              size="xl"
              title="Page d'inscription "
              hide-footer>

      <Inscription/>
    </b-modal>

    <b-container>
      <img class="background" src="../reception.jpg"/>
    </b-container>

    <Footer/>

    </div>
</template>



<script>

import Footer from './footer2.vue';
import Inscription from './inscription.vue'

export default {
  
  components: { Footer, Inscription },

  }

</script>


<style>

.fit-picture {
  width: 100px;
}

.background {
    width: 100%;
    height: auto;
  }

.headBand {
  background-color: rgb(65, 192, 171);
  color: rgb(245, 245, 245);
  height: 150px;
}

li {
  display: inline-block;
}

.connexion {
  font-size: 25px;  
}

/* Modal */

.modal-backdrop
{
    opacity:0.5 !important;
}

/* blocs */

.left,
.center,
.right {
  padding-top: 10px;
}

.right {
  float: right;
  padding-right: 80px;
}

.center {
  padding-left: 1%;
}

.left {
  float: left;
}
</style>