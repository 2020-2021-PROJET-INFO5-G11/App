<template>
  <div>
    <!-- Header -->
    <Header title="Recherche de sortie par ID ou mots clés"/>
    <!-- NavBar -->
    <NavBar> </NavBar>

    <!-- Title -->
    <!-- Boutton créer une sortie -->
    <br>
    <i class="right fa fa-plus-circle fa-3x"
      @click="$router.push('/creation-sortie')"> Créer une sortie</i> <br>

    <!-- Title -->
    <h1> Résultats de la recherche : {{$route.params.search}}</h1>
    <hr>

    <!-- Activities -->
    <ul class="scrollmenu">
      <!-- -->
      <li v-for="(sortie) in sorties" :key="sortie">
        <!-- Image -->
        <div class="rect img-container" @click="$router.push({path: `/sortie/${sortie.id_sortie}`})">
          <img class="fit-picture" :src="getImgUrl(sortie.photo)"  >
          <img v-if="sortie.capaciteMax - sortie.nbInscrits == 0" class="overlay-img fit-picture" src="../complet.png"  >
          {{sortie.nbInscrits}} inscrits
        </div> <br>

        <!-- Name -->
        <div class="data">
          <span @click="$router.push({path: `/sortie/${sortie.id_sortie}`})" class="date"> {{sortie.date}} </span>
          <span @click="$router.push({path: `/sortie/${sortie.id_sortie}`})" class="nom"> {{sortie.nom}} </span><br> 
        </div>

        <!-- Buttons -->
        <div style="text-align: center;">
          <!-- View activity-->
          <button type="button"
                  class="bouton btn-sm"
                  v-b-modal.sortie-view-modal
                  @click="$router.push({path: `/sortie/${sortie.id_sortie}`})">
              Voir sortie
          </button>&ensp;
          <!-- Edit activity -->
          <button type="button"
                  class="btn btn-warning btn-sm"
                  v-b-modal.sortie-update-modal
                  @click="$router.push({path: `/modification-sortie/${sortie.id_sortie}`})">
              Modifier
          </button>&ensp;
          <!-- Delete activity -->
          <button type="button"
                  class="btn btn-danger btn-sm"
                  @click="onDeleteSortie(sortie)">
              Supprimer
          </button>
        </div>
      </li>
    </ul>

    <!-- Sorties 
    <div class="row">
      <div class="col-sm-10">
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">Nom</th>
              <th scope="col">Type</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(sortie, index) in sorties" :key="index">
              <td>{{ sortie.nom }}</td>
              <td>{{ sortie.typeSortie }}</td>
              <td>
              </td>
            </tr>
          </tbody>
        </table>
    </div> 
    </div>-->
    <!-- Footer -->
    <Footer />
  </div>
</template>

<script>
import axios from 'axios';
import Alert from './Alert.vue';
import Header from './header.vue';
import NavBar from './navBar.vue';
import Footer from './footer.vue';

export default {
  data() {
    return {
      sorties: [],
      key: 0,
    };
  },
  components: {
    alert: Alert, Header, NavBar, Footer,
  },
  methods: {
    forceRerender() {
      this.key += 1;
    },
    getSearch() {
      const path = `http://localhost:5000/api/search/${this.$route.params.search}`;
      axios.get(path)
        .then((res) => {
          this.sorties = res.data;
        })
        .catch((error) => {
          console.error(error);
        });
    },
    removeSortie(sortieID) {
      const path = `http://localhost:5000/api/sortie/${sortieID}`;
      axios.delete(path)
        .then(() => {
          this.getSorties();
          this.message = 'Sortie supprimée!';
          this.showMessage = true;
        })
        .catch((error) => {
          console.error(error);
          this.getSorties();
        });
    },
    onDeleteSortie(sortie) {
      this.removeSortie(sortie.id_sortie);
    },
     getImgUrl(image) {
      return require('../'+image+'.jpg');
    },
  },
  created() {
    this.getSearch();
  },
};
</script>

<style scoped>

h1{
  margin-left:1em;
}

.img-container {
     position: relative;
}

.overlay-img {
     position: absolute;
     top: 0;
     left: 0;
}
  
.bouton {
  background-color: rgb(65, 192, 171);
}
.right {
  float: right;
}
i  {
  font-size: 35px;
  color: rgb(65, 192, 171);
}
i:hover {
  color: rgb(15, 138, 117);
  cursor: pointer;
}
li {
  display: inline-block;
  padding: 4em;
}
.fit-picture {
  width: 320px;
  height: 210px;
}
.rect {
  border: solid;
  border-width: 5px;
  border-color: black;
  width: 328px;
  height: 219px;
}
.nom {
  height: 26px;
  word-break:break-all;
  overflow: hidden;
  text-overflow: ellipsis;
  display: -webkit-box;
  -webkit-line-clamp: 1; /* number of lines to show */
  -webkit-box-orient: vertical;
}
.data {
  width: 328px;
  font-size: 20px;
  text-align: center;
}
.nom:hover, .date:hover{
  cursor: pointer;
}
img:hover {
  opacity: 0.7;
}
.rect:hover {
  border-color: rgb(15, 138, 117);
  cursor: pointer;
}
.title {
  padding-left: 20px;
}
.filter {
  padding-left: 4em;
  font-size: 20px;
  text-align: center;
}
</style>
