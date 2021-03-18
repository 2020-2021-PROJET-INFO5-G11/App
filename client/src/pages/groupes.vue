<template>
  <div>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <!-- Header -->
    <Header title="Tous vos groupes"/>
    <!-- NavBar -->
    <NavBar/>
    <!-- Body -->
    <!-- Boutton créer un groupe -->
    <br>
        <i class="right fa fa-plus-circle fa-3x"
         @click="$router.push('/creation-groupe')"> Créer un groupe</i> <br><br>

      <h1> Vos groupes </h1><br> 
      <ul class="scrollmenu">
        <li v-for="groupe in current_user.groupes" :key="groupe">

          <!-- Name -->
          <div class="data">
            <!-- Image -->
            <div class="rect img-container" @click="$router.push({path: `/groupe/${groupe.id_groupe}`})">
              <img class="fit-picture" v-bind:src="getImgUrl(groupe.photo)"><br><br>
              <span class="nom"> Nom : {{groupe.nom}} </span>
              <span class="nbMembres"> Nombre de membres : {{groupe.nbMembres}} </span>
            </div> <br><br>
            <br>
            <div>
              <!-- Buttons -->
              <div class="data row" style="justify-content: center;">
                <!-- View activity-->
                <div class="view" @click="$router.push({path: `/groupe/${groupe.id_groupe}`})">
                  Voir <img src="../assets/view.png" width="20">
                </div>&ensp;
                <!-- Edit button -->
                <div class="edit" @click="$router.push({path: `/modification-groupe/${groupe.id_groupe}`})">
                  Modifier <img src="../assets/edit.png" width="20">
                </div>&ensp;
                <!-- Delete activity -->
                <div class="delete" v-b-modal="'suppression-modal'" @click="selectedGroupe = groupe">
                  Supprimer <img src="../assets/delete.png" width="20">
                </div>
                <br>
                &ensp;
              </div>
            </div>
          </div>
        </li>
      </ul>

      <br><br>
      <h1> Invitations à des groupes </h1> <br>
      <ul class="scrollmenu">
        <li v-for="(demande, index) in current_user.demandes" :key="demande">
          <!-- Nom + Image -->
          <div class="data">
            <div class="rect img-container" @click="$router.push({path: `/groupe/${demande.id_groupe}`})">
              <img class="fit-picture" v-bind:src="getImgUrl(getDemande(index).photo)"><br><br>
              <span class="nom"> Nom : {{getDemande(index).nom}} </span>
              <span class="id"> Id : {{demande.id_groupe}} </span>
            </div>
          </div> <br><br><br><br>
          <!-- Buttons -->
          <div class="data row" style="justify-content: center;">
            <!-- View activity-->
            <div class="accept" @click="accept(demande.id_groupe)">
              Accepter <img src="../assets/accept.png" width="20">
            </div>&ensp;
            <!-- Edit button -->
            <div class="refuse" @click="refuse(demande.id_groupe)">
              Refuser <img src="../assets/refuse.png" width="20">
            </div>&ensp;
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
            <img v-if="selectedGroupe.photo !== undefined" class="fit-picture" :src="getImgUrl(selectedGroupe.photo)">
          </div> <br>

          <!-- Name -->
          <div class="data">
            <span class="date"> {{selectedGroupe.date}} </span>
            <span class="nom"> {{selectedGroupe.nom}} </span><br> 
          </div>

          <!-- Buttons -->
          <div class="data">
            <button style = "color: green" @click="$bvModal.hide('suppression-modal'); onDeleteGroupe(selectedGroupe); selectedGroupe = {};"> Oui </button>
            &ensp;<button style = "color: red" @click="$bvModal.hide('suppression-modal'); selectedGroupe = {};"> Non </button>
          </div>
        </div>
      </b-modal>


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
      selectedGroupe: {},
      groupes: [],
      invitation_groupe: [],
      demandes: [],
      current_user: {},
    };
  },
  methods: {
    getGroupe(groupeID) {
      const path = `http://localhost:5000/api/groupe/${groupeID}`;
      axios.get(path)
        .then((res) => {
          this.invitation_groupe.push(res.data);
          console.log(this.invitation_groupe);
        })
        .catch((error) => {
          console.error(error);
        });
    },
    getCurrentUser() {
      const path = 'http://localhost:5000/api/user/current';
      axios.get(path)
        .then((res) => {
          this.current_user = res.data;
          for(const d of this.current_user.demandes){
            this.getGroupe(d.id_groupe);
          };
        })
        .catch((error) => {
          console.error(error);
        });
    },
    getDemande(index) {
      return this.invitation_groupe[index];
    },
    getGroupePhoto : function(groupeID) {
      const path = `http://localhost:5000/api/groupe/${groupeID}`;
      axios.get(path)
        .then((res) => {
          const result = res.data;
          console.log("photo");
          console.log(result.photo);
          return result.photo;
        })
        .catch((error) => {
          console.error(error);
          return "pas-de-photo";
        });
    },
    getGroupeNom(groupeID){
      const path = `http://localhost:5000/api/groupe/${groupeID}`;
      axios.get(path)
        .then((res) => {
          const result = res.data;
          console.log("nom");
          console.log(result.nom);
          return result.nom;       
        })
        .catch((error) => {
          console.error(error);
          return "null";
        });
    },
    accept(groupeID) {
      const path = `http://localhost:5000/api/groupe/${groupeID}/membres`;
      axios.post(path)
        .then((res) => {
          this.getCurrentUser();
          this.invitation_groupe= [];
        })
        .catch((error) => {
          console.error(error);
        });
    },
    refuse(groupeID) {
      const path = `http://localhost:5000/api/groupe/${groupeID}/demandes`;
      axios.delete(path)
        .then((res) => {
          
        })
        .catch((error) => {
          console.error(error);
        });
    },
    getImgUrl(image) {
      return require('../assets/'+image+'.jpg');
    },
    removeGroupe(groupeID) {
      const path = `http://localhost:5000/api/groupe/${groupeID}`;
      axios.delete(path)
        .then(() => {
          this.getCurrentUser();
        })
        .catch((error) => {
          console.error(error);
          this.getCurrentUser();
        });
    },
    onDeleteGroupe(groupe) {
      this.removeGroupe(groupe.id_groupe);
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

.view, .edit, .delete, .switch, .accept, .refuse {
  padding: 4px;
  cursor: pointer;
}

.view, .accept {
  color: green;
}

.edit {
  color: rgb(204, 134, 4);
}

.delete, .refuse {
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
