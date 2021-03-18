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
      @click="$router.push('/creation-sortie')"> Créer une sortie</i> <br><br>

    <!-- Title -->
    <br><hr>
    <h1> Résultats de la recherche : {{$route.params.search}}</h1>
    <hr>

    <!-- Activities -->
    <ul class="scrollmenu">
      <!-- -->
      <li v-for="(sortie) in sorties" :key="sortie">
        <div v-if="sortie.archivee == false" style="padding: 4em;">
          <!-- Image -->
          <div class="rect img-container" @click="$router.push({path: `/sortie/${sortie.id_sortie}`})">
            <img class="fit-picture" :src="getImgUrl(sortie.photo)"  >
            <img v-if="sortie.capaciteMax - sortie.nbInscrits == 0" class="overlay-img fit-picture" src="../assets/complet.png"  >
            {{sortie.nbInscrits}} inscrits
          </div> <br>

          <!-- Name -->
          <div class="data">
            <span @click="$router.push({path: `/sortie/${sortie.id_sortie}`})" class="date"> {{sortie.date}} </span>
            <span @click="$router.push({path: `/sortie/${sortie.id_sortie}`})" class="nom"> {{sortie.nom}} </span><br> 
          </div>

          <div>
            <!-- Buttons -->
            <div class="data row" style="padding-left: 29px;">
              <!-- View activity-->
              <div class="view" @click="$router.push({path: `/sortie/${sortie.id_sortie}`})">
                Voir <img src="../assets/view.png" width="20">
              </div>&ensp;
              <!-- Edit button -->
              <div class="edit" @click="$router.push({path: `/modification-sortie/${sortie.id_sortie}`})">
                Modifier <img src="../assets/edit.png" width="20">
              </div>&ensp;
              <!-- Delete activity -->
              <div class="delete" v-b-modal="'suppression-modal'" @click="selectedSortie = sortie">
                Supprimer <img src="../assets/delete.png" width="20">
              </div>
              <br>
            </div>
          </div>
        </div>
      </li>
    </ul>

    <!-- Suppression -->
    <b-modal ref="suppression"
        id="suppression-modal"
        size="l"
        title="Page de suppression de sortie"
        hide-footer>

      <div style="text-align: center;">
        <span style=" font-size: 30px;"> Êtes-vous sûr de vouloir supprimer</span><br><br><br>
      </div>
      
      <div class="justify-center">

        <!-- Image -->
        <div class="rect img-container">
          <img v-if="selectedSortie.photo !== undefined" class="fit-picture" :src="getImgUrl(selectedSortie.photo)">
        </div> <br>

        <!-- Name -->
        <div class="data">
          <span class="date"> {{selectedSortie.date}} </span>
          <span class="nom"> {{selectedSortie.nom}} </span><br> 
        </div>

        <!-- Buttons -->
        <div class="data">
          <button style = "color: green" @click="$bvModal.hide('suppression-modal'); onDeleteSortie(selectedSortie); selectedSortie = {};"> Oui </button>
          &ensp;<button style = "color: red" @click="$bvModal.hide('suppression-modal'); selectedSortie = {};"> Non </button>
        </div>
      </div>
    </b-modal>
    
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
      selectedSortie: {},
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
          this.getSearch();
        })
        .catch((error) => {
          console.error(error);
          this.getSearch();
        });
    },
    onDeleteSortie(sortie) {
      this.removeSortie(sortie.id_sortie);
    },
     getImgUrl(image) {
      return require('../assets/'+image+'.jpg');
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
.view, .edit, .delete, .switch {
  padding: 4px;
  cursor: pointer;
}

.view {
  color: green;
}

.edit {
  color: rgb(204, 134, 4);
}

.delete {
  color: rgb(175, 29, 29);
}

.justify-center {
  display: grid;
  justify-content: center;
}

</style>
