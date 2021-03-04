<template>
  <div>

    <!-- Header -->
    <Header title="Page temporaire"/>

    <!-- NavBar -->
    <NavBar> </NavBar>

    <!-- Boutton créer une sortie -->
    <br>
    <i class="right fa fa-plus-circle fa-3x"
      @click="$router.push('/creation-sortie')"> Créer une sortie</i> <br>

    <!-- Title -->
    <h1 class="title"> Toutes les sorties </h1>
    <hr>

    <!-- Alert message -->
    <alert :message=message v-if="showMessage"></alert><br>
    
    <!-- Filter -->

    <div class="filter">
      <select style="width: 300px;" v-on:change="filter($event)">
        <option value="" disabled hidden selected>Filtrer par type de sortie</option>
        <option v-for="t in types" :key="t">
          {{ t }}
        </option>
      </select>
      <br><br>
    </div>
    
    <!-- Activities -->
    <ul class="scrollmenu">
      <!-- -->
      <li v-for="(sortie, index) in sorties" :key="index">
        <!-- Image -->
        <div class="rect" @click="$router.push({path: `/sortie/${sortie.id_sortie}`})">
          <img class="fit-picture" :src="getImgUrl(sortie.photo)"  >
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
                  @click="$router.push({path: `/sortie/${sortie.id_sortie}`})">
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

    <!-- Footer -->
    <br><br>
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
      key: 0,
      sorties: [],
      addSortieForm: {
        nom: '',
        typeSortie: '',
        privee: [],
      },
      message: '',
      showMessage: false,
      editForm: {
        id_sortie: '',
        nom: '',
        typeSortie: '',
        privee: [],
      },
      types: ['Pas de filtre', 'Autre', 'Cinéma', 'Culture', 'Musée', 'Musique', 'Repas', 'Sport'],
    };
  },
  components: {
    alert: Alert, Header, NavBar, Footer,
  },
  methods: {
    forceRerender() {
      this.key += 1;
    },
    getImgUrl(image) {
      return require('../'+image+'.jpg');
    },
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
    filter(evt) {
      if(evt.target.value == 'Pas de filtre'){
        this.getSorties();
      }
      else{
        const path = `http://localhost:5000/api/filter/${evt.target.value}`;
        axios.get(path)
          .then((res) => {
            this.sorties = res.data;
          })
          .catch((error) => {
            console.error(error);
          });
      }
    },
    addSortie(payload) {
      const path = 'http://localhost:5000/api/sortie';
      axios.post(path, payload)
        .then(() => {
          this.getSorties();
          this.message = 'Sortie créee!';
          this.showMessage = true;
        })
        .catch((error) => {
          console.log(error);
          this.getSorties();
        });
    },
    initForm() {
      this.addSortieForm.nom = '';
      this.addSortieForm.typeSortie = '';
      this.adSortieForm.privee = [];
      this.editForm.id_sortie = '';
      this.editForm.nom = '';
      this.editForm.typeSortie = '';
      this.editForm.privee = [];
    },
    onSubmit(evt) {
      evt.preventDefault();
      this.$refs.addSortieModal.hide();
      let privee = false;
      if (this.addSortieForm.privee[0]) privee = true;
      const payload = {
        nom: this.addSortieForm.nom,
        typeSortie: this.addSortieForm.typeSortie,
        privee,
      };
      this.addSortie(payload);
      this.initForm();
    },
    onReset(evt) {
      evt.preventDefault();
      this.$refs.addSortieModal.hide();
      this.initForm();
    },
    editSortie(sortie) {
      this.editForm = sortie;
    },
    onSubmitUpdate(evt) {
      evt.preventDefault();
      this.$refs.editSortieModal.hide();
      let privee = false;
      if (this.editForm.privee[0]) privee = true;
      const payload = {
        nom: this.editForm.nom,
        typeSortie: this.editForm.typeSortie,
        privee,
      };
      this.updateSortie(payload, this.editForm.id_sortie);
    },
    updateSortie(payload, sortieID) {
      const path = `http://localhost:5000/api/sortie/${sortieID}`;
      axios.put(path, payload)
        .then(() => {
          this.getSorties();
          this.message = 'Sortie mise à jour!';
          this.showMessage = true;
        })
        .catch((error) => {
          console.error(error);
          this.getSorties();
        });
    },
    onResetUpdate(evt) {
      evt.preventDefault();
      this.$refs.editSortieModal.hide();
      this.initForm();
      this.getSorties();
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
  },
};
</script>

<style scoped>
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
.scrollmenu {
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