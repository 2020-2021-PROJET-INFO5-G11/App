<template>
    <div>

      <div class="row headBand">
        <div style="text-align: center;" class="col-md-auto">
          <img class="fit-picture" src="../logo_blanc.png">
          <h6 class="titre" > Osons Sortir</h6> <!--style="padding-left: 50px;"-->
        </div>
        <div class="col-md-auto">
          <br>
          <h1> Bienvenue !</h1>
        </div>

        <div class="connexion-1" >
          <b-button variant=primary>
            Connexion
          </b-button>
        </div>
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

  .headBand {
    background-color: rgb(65, 192, 171);
    color: rgb(245, 245, 245);
  }

  .col-md-auto {
     text-align: center;
  }

  .titre {
  }
  .connexion-1 {
    float : right;
     text-align: center;
  }
</style>