<template>
    <div>

      <div class="row headBand">
        <div style="text-align: center;" class="col-md-auto">
          <img class="fit-picture" src="../logo_blanc.png"  >
          <h6 style="padding-left: 5px;"> Osons Sortir</h6>
        </div>
        <div class="col-md-auto">
          <br>
          <h1> Bienvenue !</h1>
        </div>

        <div  class="connexion-1" >
          <b-button variant=primary>
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
    padding: 100 px;
    background-color: rgb(65, 192, 171);
    color: rgb(245, 245, 245);
  }

  .connexion-1 {
    float: right;
  }
</style>