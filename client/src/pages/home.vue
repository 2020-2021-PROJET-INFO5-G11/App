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
        <i class="right fa fa-plus-circle fa-3x"
         @click="$router.push('/creation-sortie')"> Créer une sortie</i> <br>

      <!-- Sorties à venir -->
      <h1> Bonjour {{current_user.prenom}} {{current_user.nom}}</h1><hr><br>

      <h1> Vos sorties à venir </h1> <br>
      <ul class="scrollmenu">
        <li v-for="sortie in current_user.sorties_a_venir" :key="sortie">
          <!-- Image -->
          <div class="rect" @click="$router.push({path: `/sortie/${sortie.id_sortie}`})">
            <img class="fit-picture" :src="getImgUrl(sortie.photo)"  >
          </div> <br>

          <!-- Name -->
          <div class="data">
            <span @click="$router.push({path: `/sortie/${sortie.id_sortie}`})" class="date"> {{sortie.date}} </span>
            <span @click="$router.push({path: `/sortie/${sortie.id_sortie}`})" class="nom"> {{sortie.nom}} </span>
            <br>
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
                <!-- View activity-->
                <div class="switch" @click="switchSortie(sortie.id_sortie)">
                  Déplacer vers votre historique <img src="../assets/switch.png" width="20">
                </div>&ensp;
              </div>
            </div>
          </div>
        </li>
        <br><br>
      </ul>

      <br><br>

      <!-- Historique de sorties -->
      <h1> Votre historique de sorties </h1> <br>
      <ul class="scrollmenu">
        <li v-for="sortie in current_user.sorties_finies" :key="sortie">
          <!-- Image -->
          <div class="rect" @click="$router.push({path: `/sortie/${sortie.id_sortie}`})">
            <img class="fit-picture" :src="getImgUrl(sortie.photo)"  >
          </div> <br>

          <!-- Name -->
          <div class="data">
            <span @click="$router.push({path: `/sortie/${sortie.id_sortie}`})" class="date"> {{sortie.date}} </span>
            <span @click="$router.push({path: `/sortie/${sortie.id_sortie}`})" class="nom"> {{sortie.nom}} </span>
            <br> 
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
              </div>  
            </div>
          </div>
        </li>
        <br><br>
      </ul>
      <br><br>

      <!-- Suppression -->
      <b-modal ref="suppression"
        id="suppression-modal"
        size="xl"
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

    </body>

    <!-- Footer -->
    <Footer />
  </div>
</template>

<script>
import axios from 'axios';
import Header from './header.vue';
import NavBar from './navBar.vue';
import Footer from './footer.vue';


export default {
  components: { Header, NavBar, Footer },
  data() {
    return {
      selectedSortie: {},
      sorties: [],
      current_user: {},
    };
  },
  methods: {
    getCurrentUser() {
      const path = 'http://localhost:5000/api/user/current';
      axios.get(path)
        .then((res) => {
          this.current_user = res.data;
        })
        .catch((error) => {
          console.error(error);
        });
    },
    getImgUrl(image) {
      return require('../assets/'+image+'.jpg');
    },
    removeSortie(sortieID) {
      const path = `http://localhost:5000/api/sortie/${sortieID}`;
      axios.delete(path)
        .then(() => {
          this.getCurrentUser();
        })
        .catch((error) => {
          console.error(error);
          this.getCurrentUser();
        });
    },
    switchSortie(sortieID) {
      const path = `http://localhost:5000/api/user/current/${sortieID}/switch`;
      axios.put(path)
        .then(() => {
          this.getCurrentUser();
        })
        .catch((error) => {
          console.error(error);
          this.getCurrentUser();
        });
    },
    onDeleteSortie(sortie) {
      this.removeSortie(sortie.id_sortie);
    },
  },
  created() {
    this.getCurrentUser();
  }
};
</script>

<style scoped>

.bouton {
  background-color: rgb(65, 192, 171);
}

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
  cursor: pointer;
}

.fit-picture {
  width: 320px;
  height: 210px;
}

li {
  display: inline-block;
  margin-left:4em;
}

.rect {
  border: solid;
  border-width: 5px;
  border-color: black;
  width: 328px;
  height: 219px;
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

.nom {
  height: 28px;
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

.switch {
  color: rgb(9, 94, 79);
}

.justify-center {
  display: grid;
  justify-content: center;
}

</style>
