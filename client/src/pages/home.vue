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
      <!--  <li v-for="s in sorties" v-bind:key="s">{{ s.name }}</li> -->

      <h1> Mes sorties à venir </h1> <br>
      <ul class="scrollmenu">
        <li v-for="sortie in sorties" :key="sortie">
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
                  Voir <img src="../view.png" width="20">
                </div>&ensp;
                <!-- Edit button -->
                <div class="edit" @click="$router.push({path: `/modification-sortie/${sortie.id_sortie}`})">
                  Modifier <img src="../edit.png" width="20">
                </div>&ensp;
                <!-- Delete activity -->
                <div class="delete" @click="onDeleteSortie(sortie)">
                  Supprimer <img src="../delete.png" width="20">
                </div>
              </div>
            </div>
          </div>
        </li>
        <br><br>
      </ul>

      <br><br>

      <!-- Historique de sorties -->
      <h1> Mon historique de sorties </h1> <br>
      <ul class="scrollmenu">
        <li v-for="sortie in sorties" :key="sortie">
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
                  Voir <img src="../view.png" width="20">
                </div>&ensp;
                <!-- Edit button -->
                <div class="edit" @click="$router.push({path: `/modification-sortie/${sortie.id_sortie}`})">
                  Modifier <img src="../edit.png" width="20">
                </div>&ensp;
                <!-- Delete activity -->
                <div class="delete" @click="onDeleteSortie(sortie)">
                  Supprimer <img src="../delete.png" width="20">
                </div>
              </div>  
            </div>
          </div>
        </li>
        <br><br>
      </ul>
      <br><br>
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
      sorties: [],
      sorties_finies: [],
      sorties_a_venir: [],
    };
  },
  methods: {
    getSorties() {
      const path = 'http://localhost:5000/api/sortie';
      axios.get(path)
        .then((res) => {
          this.sorties = res.data;
        })
        .catch((error) => {
          console.error(error);
        });
    },
    getPreviousSorties() {
      const path = 'http://localhost:5000/api/user/current/finies';
      axios.get(path)
        .then((res) => {
          this.sorties_finies = res.data;
        })
        .catch((error) => {
          console.error(error);
        });
    },
    getIncomingSorties() {
      const path = 'http://localhost:5000/api/user/current/a_venir';
      axios.get(path)
        .then((res) => {
          this.sorties_a_venir = res.data;
        })
        .catch((error) => {
          console.error(error);
        });
    },
    getImgUrl(image) {
      return require('../'+image+'.jpg');
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
  },
  created() {
    this.getSorties();
    this.getIncomingSorties();
    this.getPreviousSorties();
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

.view, .edit, .delete {
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
</style>
