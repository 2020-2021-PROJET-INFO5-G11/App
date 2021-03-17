<template>
  <div>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <!-- Header -->
    <Header title="Groupes"/>
    <!-- NavBar -->
    <NavBar/>
    <!-- Body -->
    <!-- Boutton créer un groupe -->
    <br>
        <i class="right fa fa-plus-circle fa-3x"
         @click="$router.push('/creation-groupe')"> Créer un groupe</i> <br><br><br>

      <h1> Vos groupes </h1>
      <ul class="scrollmenu">
        <li v-for="groupe in current_user.groupes" :key="groupe">

          <!-- Name -->
          <div class="data">
            <span @click="$router.push({path: `/groupe/${groupe.id_groupe}`})" class="nom"> {{groupe.nom}} </span>
            <span @click="$router.push({path: `/groupe/${groupe.id_groupe}`})" class="nbMembres"> Nb. membres : {{groupe.nbMembres}} </span>
            <br>
            <div>
              <!-- Buttons -->
              <div class="data row" style="padding-left: 29px;">
                <!-- View activity-->
                <div class="view" @click="$router.push({path: `/groupe/${groupe.id_groupe}`})">
                  Voir <img src="../view.png" width="20">
                </div>&ensp;
                <!-- Edit button -->
                <div class="edit" @click="$router.push({path: `/modification-groupe/${groupe.id_groupe}`})">
                  Modifier <img src="../edit.png" width="20">
                </div>&ensp;
                <br>
                &ensp;
              </div>
            </div>
          </div>
        </li>
        <br><br>
      </ul>

      <br><br>
      <h1> Invitations à des groupes </h1> <br>
      <ul class="scrollmenu">
        <li v-for="demande in current_user.demandes" :key="demande">

          <!-- Name -->
          <div class="data">
            <span class="invitation"> {{demande.id_groupe}} </span>
            <br> 
            <div>
            <!-- Buttons -->
              <div class="data row" style="padding-left: 29px;">
                <!-- View activity-->
                <div class="accept" @click="accept(demande.id_groupe)">
                  Accepter <img src="../view.png" width="20">
                </div>&ensp;
                <!-- Edit button -->
                <div class="refuse" @click="refuse(demande.id_groupe)">
                  Refuser <img src="../edit.png" width="20">
                </div>&ensp;
              </div>  
            </div>
          </div>
        </li>
        <br><br>
      </ul>
      <br><br>


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
      groupes: [],
      invitation_groupe: {},
      demandes: [],
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
    getGroupe(groupeID) {
      const path = `http://localhost:5000/api/groupe/${groupeID}`;
      axios.get(path)
        .then((res) => {
          this.invitation_groupe = res.data;
        })
        .catch((error) => {
          console.error(error);
        });
    },
    accept(groupeID) {
      const path = `http://localhost:5000/api/groupe/${groupeID}/membres`;
      axios.post(path)
        .then((res) => {
          
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
      return require('../'+image+'.jpg');
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

</style>
