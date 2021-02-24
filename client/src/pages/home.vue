<template>
  <div>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <!-- Header -->
    <Header title="Page d'accueil"/>
    <!-- NavBar -->
    <NavBar> </NavBar>
    <!-- Body -->
    <body>
      <br>

      <!-- Boutton créer une sortie -->
      <i class="right fa fa-plus-circle fa-3x"> Créer une sortie</i> <br>

      <!-- Sorties à venir -->
      <h1> Mes sorties à venir </h1> <br>
      <ul class="scrollmenu">
        <li style="margin-left:0em;">
          <div class="rect">
            <img class="fit-picture" src="../cinema.jpg"  >
          </div>
          <div class="title"> Sortie 7</div><br><br>
        </li>
        <li>
          <div class="rect">
            <img class="fit-picture" src="../randonnée.jpg">
          </div>
          <div class="title"> Sortie 8</div><br><br>
        </li>

      </ul>

      <!-- Historique de sorties -->
      <h1> Mon historique de sorties </h1> <br>
      <ul class="scrollmenu">
        <li style="margin-left:0em;">
          <div class="rect">
            <img class="fit-picture" src="../cinema.jpg">
          </div>
          <div class="title"> Sortie 6</div><br><br>
        </li>
        <li>
          <div class="rect">
            <img class="fit-picture" src="../cinema.jpg">
          </div>
          <div class="title"> Sortie 5</div><br><br>
        </li>
        <li>
          <div class="rect">
            <img class="fit-picture" src="../musée.jpg">
          </div>
          <div class="title"> Sortie 4</div><br><br>
        </li>
         <li>
          <div class="rect">
            <img class="fit-picture" src="../cinema.jpg">
          </div>
          <div class="title"> Sortie 3</div><br><br>
        </li>
         <li>
          <div class="rect">
            <img class="fit-picture" src="../randonnée.jpg">
          </div>
          <div class="title"> Sortie 2</div><br><br>
        </li>
         <li>
          <div class="rect">
            <img class="fit-picture" src="../musée.jpg">
          </div>
          <div class="title"> Sortie 1</div><br><br>
        </li>

        <li>
        </li>
      </ul>
      <br><br>
    </body>
    <!-- Footer -->
    <Footer />
  </div>
</template>

<script>
import Header from './header.vue';
import NavBar from './navBar.vue';
import Footer from './footer.vue';


export default {
  components: { Header, NavBar, Footer },
  data() {
    return {
    };
  },
  methods: {
  },
};
</script>

<style scoped>

i  {
  font-size: 35px;
  color: rgb(65, 192, 171);
}

i:hover {
  color: rgb(15, 138, 117);
  cursor: pointer;
}

.right {
  float: right;
  padding-right: 70px;
}

img:hover {
  opacity: 0.7;
}

.fit-picture {
  width: 291px;
  height: 191px;
}

li {
  display: inline-block;
  margin-left:4em;
}

.rect {
  border: solid;
  border-width: 5px;
  border-color: rgb(65, 192, 171);
  width: 300px;
  height: 200px;
}

.rect:hover {
  border-color: rgb(15, 138, 117);
  cursor: pointer;
}

.scrollmenu {
  overflow: auto;
  white-space: nowrap;
}

h1{
  margin-left:1em;
}

.title {
  width: 300px;
  text-align: center;
}

</style>
