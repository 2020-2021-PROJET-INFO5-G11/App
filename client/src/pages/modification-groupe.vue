<template>
  <div>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <!-- Header -->
    <Header title="Page de modification de groupe"/>
    <!-- NavBar -->
    <NavBar> </NavBar>
    <!-- Body -->
    <body>

      <!-- Formulaire -->
      <form id="app"
            @submit="edit"
            action="https://vuejs.org/"
            method="post">

        <br> <h1> ID groupe : {{ this.$route.params.id }} - {{ this.nom }}  </h1> <br>

        <!-- columns -->
        <ul>

          <!-- left -->
          <li class="horizontal" style="width:300px;">

            <h3> Champs obligatoires </h3><br>

            <div>
              <label> Photo </label>
              <div class="rect">
                <img @click="$bvModal.show('photo-modal')" class="fit-picture" :src="getImgUrl(photo)">
              </div>  
            </div>

            <b-modal ref="addPhoto"
                     id="photo-modal"
                     size="xl"
                     title="Choisir une photo de couverture pour le groupe"
                     hide-footer>

              <ul style="overflow-y: scroll; height: 700px; width: 1200px;">
                <li class="horizontal2" v-for="i in images" v-bind:key="i">
                  {{i}}
                  <br>
                  <img class="fit-picture" :src="getImgUrl(i)" @click="$bvModal.hide('photo-modal')"
                       v-on:click="setImage(i)"/>
                </li>
              </ul>

            </b-modal>
          </li>

          <!-- center -->
          <li class="horizontal">

            <br><br><br><br>

            <div>
              <input v-model="nom" @input="onChange()" type="text" style="width: 500px;" placeholder="Nom" required/>
            </div>
            <br><br>

            <br>
            <label> Description </label>
            <div>
              <textarea v-model="description" cols="40" rows="5" style="width:500px; height:220px;" required/>
            </div>

          </li>

          <!-- Separateur -->
          <li style="padding: 10px; width: 2px;
                    display: inline-table;  margin-left:4em;">
            <div style="border: solid; width: 1px; border-width:1px; border-color: grey;">
              <br><br><br><br><br><br><br><br><br><br><br><br><br>
              <br><br><br><br><br><br><br><br><br><br><br><br><br>
            </div>
          </li>

          <!-- right -->
          <li class="horizontal">

            <h3> Administrateurs </h3><br>

            <br>
            <div>
              <span> Ajouter un administrateur </span><br>
              <input type="text" style="width: 450px;"
                     v-model="organisateur" placeholder="ID ou nom"/>
              &ensp; <i class="add fa fa-user" @click="ajouterOrganisateur()"></i>
            </div>
            <br><br>
            <span> Liste des administrateurs </span><br>
            <ul class = "scrollmenu">
              <br>
              <li class="veritcal">
                <span class="vertical"> {{current_user.nom}} {{current_user.prenom}} (vous) </span>
              </li>

              <li class="veritcal" v-for="o in administrators" v-bind:key="o">
                <span class="vertical"> {{o}} </span>
                <i class="fa fa-trash-o fa-1x" @click="suprimerOrganisateur(o)"></i>
              </li>
            </ul>
          </li>
        </ul>        

        <!-- submit button -->
        <div style="padding-left:800px">
          <input class="submit" type="submit" value="Modifier le groupe"> &ensp;
          <br>
        </div>
        <br><br>

      </form>
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
      nom: '',
      description: '',
      current_user: {},
      editForm: {}, 
      groupe: {},
      photo: 'pas-de-photo',
      administrators: [],
      images: ['basketball', 'cinema', 'escalade', 'escalade-sur-glace', 'football', 'foot-us', 'gymnastique', 'musée', 'parc', 'piscine', 'randonnée', 'rugby', 'salle-de-bloc', 'ski', 'tennis'],
    };
  },
  methods: {
    checkForm() {
      this.submit = true;
      if (this.nom && this.description && this.photo) {
        return true;
      }
      return false;
    },
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
    accept(groupeID) {
      const path = `http://localhost:5000/api/groupe/${groupeID}/membres`;
      axios.post(path)
        .then((res) => {
          this.$router.go();
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
    ajouterOrganisateur() {
      let exist = false;
      if (this.organisateur) {
        this.administrators.forEach((value) => {
          if (value === this.organisateur) {
            exist = true;
          }
        });
        if (!exist) {
          this.administrators.push(this.organisateur);
        }
      }
    },
    getGroupe() {
      const path = `http://localhost:5000/api/groupe/${this.$route.params.id}`;
      axios.get(path)
        .then((res) => {
          this.id = this.$route.params.id;
          this.nom = res.data.nom,
          this.editForm.nom = res.data.nom,
          this.description = res.data.description,
          this.editForm.description = res.data.description,
          this.editForm.photo = res.data.photo,
          this.photo = res.data.photo
        })
        .catch((error) => {
          console.error(error);
        });
    },
    inviterMembre(id_user) {
      const path = `http://localhost:5000/api/groupe/${groupeID}/demandes`;
      axios.post(path, id_user)
        .then((res) => {
          this.$router.go();
        })
        .catch((error) => {
          console.error(error);
        });
    },
    supprimerMembre(o) {
      
    },
    getImgUrl(image) {
      return require('../assets/'+image+'.jpg');
    },
    setImage(i) {
      this.photo = i;
      this.editForm.photo = i;
    },
    onHide(evt) {
      evt.preventDefault();
      this.$refs.addPhoto.hide("photo-modal");
    },
    onChange() {
      this.editForm.nom = this.nom;
      this.editForm.description = this.description;
      this.editForm.photo = this.photo;
    },
    updateGroupe(payload, groupeID) {
      const path = `http://localhost:5000/api/groupe/${groupeID}`;
      axios.put(path, payload)
        .then(() => {
          this.$router.go(-1);
        })
        .catch((error) => {
          console.error(error);
        });
    },
    edit(evt) {
      if(this.checkForm() === true){
        evt.preventDefault();
        const payload = {
          nom: this.editForm.nom,
          description: this.editForm.description,
          photo: this.editForm.photo,
        };
        this.updateGroupe(payload, this.$route.params.id);
      }
    }
  },
  created() {
      this.getGroupe();
      this.getCurrentUser();
  },
};
</script>

<style scoped>

i  {
  font-size: 20px;
  color: rgb(156, 26, 26);
}

i:hover {
  cursor: pointer;
  font-size: 22px;
  color: rgb(119, 20, 20);
}

i.add {
  color: rgb(65, 192, 171);
  font-size: 28px;
}

i.add:hover {
  color: rgb(15, 138, 117);
  font-size: 30px;
}

.fit-picture {
  width: 291px;
  height: 210px;
}

.rect {
  border: solid;
  border-width: 5px;
  border-color: black;
  width: 300px;
  height: 219px;
}

img:hover {
  opacity: 0.7;
}

.rect:hover {
  border-color: rgb(15, 138, 117);
  border-width: 5px;
  cursor: pointer;
}

.submit, .reset {
  width: 300px;
  font-size: 35px;
  color: whitesmoke;
  border-color: rgb(15, 138, 117);
  background-color: rgb(65, 192, 171);
  cursor: pointer;
}

li.horizontal {
  padding: 50px;
  width: 600px;
  display: inline-table;
  margin-left:4em;
}

li.horizontal2 {
  padding: 5px;
  display: inline-table;
  text-align: center;
  margin-top: 10px;
  text-transform: uppercase;
}

li.veritcal {
  display: table;
  font-size: 20px;
  height: 40px;
}

.vertical:hover {
  padding-top: 50em;
  color: rgb(15, 138, 117);
  cursor: pointer;
  font-size: 22px;
}

h1{
  margin-left:1em;
}

.title {
  width: 300px;
  text-align: center;
}

.left {
  width: 400px;
}

.scrollmenu {
  overflow-y: scroll;
  white-space: nowrap;
  width: 500px;
  height: 250px;
  border: 2px inset #EBE9ED;
  text-align: left;
}

.modal-backdrop {
    opacity:0.5 !important;
}

</style>
