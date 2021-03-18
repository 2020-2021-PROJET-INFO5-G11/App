<template>
  <div>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <!-- Header -->
    <Header title="Page de création de groupe"/>
    <!-- NavBar -->
    <NavBar> </NavBar>
    <!-- Body -->
    <body>

      <!-- Formulaire -->
      <form id="app"
            @submit="submit"
            @reset="reset"
            method="post">

        <br> <h1> Créer un groupe </h1> <br>

        <!-- columns -->
        <ul>

          <!-- left -->
          <li class="horizontal" style="width:300px;">

            <h3> Champs obligatoires </h3><br>

            <div>
              <label> Photo </label>
              <div class="rect">
                <img @click="$bvModal.show('photo-modal')" class="fit-picture" :src="getImgUrl(addGroupForm.photo)">
              </div>
            </div>

            <b-modal ref="addPhoto"
                     id="photo-modal"
                     size="xl"
                     title="Choisir une photo de couverture pour l'activité"
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
              <label> Nom </label>
              <input v-model="addGroupForm.nom" type="text" style="width: 500px;" required/>
            </div>
            <br><br>

            <br>
            <label> Description </label>
            <div>
              <textarea v-model="addGroupForm.description" cols="40" rows="5" style="width:500px; height:220px;" required/>
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

        <br><br>

        <!-- submit button -->
        <div style="padding-left:800px">
          <input class="submit" type="submit" value="Envoyer"> &ensp;
          <input class="reset" type="reset" value="Reinitialiser">
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
      addGroupForm: {
        nom: '',
        capaciteMin: 1,
        capaciteMax: 50,
        typeSortie: 'Autre',
        photo: 'pas-de-photo',
        description: '',
      },
      current_user: {},
      administrators: [],
      images: ['basketball', 'cinema', 'escalade', 'escalade-sur-glace', 'football', 'foot-us', 'gymnastique', 'musée', 'parc', 'piscine', 'randonnée', 'rugby', 'salle-de-bloc', 'ski', 'tennis'],
    };
  },
  methods: {
    checkForm() {
      this.submit = true;
      if (this.addGroupForm.nom && this.addGroupForm.capaciteMin && this.addGroupForm.capaciteMax && this.addGroupForm.description) {
        return true;
      }
      return false;
    },
    reset() {
      this.addGroupForm = {
        nom: '',
        capaciteMin: 1,
        capaciteMax: 50,
        typeSortie: 'Autre',
        photo: 'pas-de-photo',
        description: '',
      }
      this.administrators = ['ElJraidi Rim', 'Sajide Idriss', 'Manissadjian Gabriel'];
      this.organisateur = null;
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
    suprimerOrganisateur(o) {
      this.administrators.forEach((value, index) => {
        if (value === o) {
          this.administrators.splice(index, 1);
        }
      });
    },
    getImgUrl(image) {
      return require('../assets/'+image+'.jpg');
    },
    setImage(i) {
      this.addGroupForm.photo = i;
    },
    onHide(evt) {
      evt.preventDefault();
      this.$refs.addPhoto.hide("photo-modal");
    },
    addGroup(payload) {
      const path = 'http://localhost:5000/api/groupe';
      axios.post(path, payload)
        .then(() => {
          this.$router.push({path: `/groupes`});
        })
        .catch((error) => {
          console.log(error);
        });
    },
    submit(evt) {
      if(this.checkForm() === true ){
        evt.preventDefault();
        const payload = {
          nom: this.addGroupForm.nom,
          photo: this.addGroupForm.photo,
          description: this.addGroupForm.description,
          nbMembres: 0,
        };
        this.addGroup(payload);
      }
    }
  },
  created() {
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
  font-size: 25px;
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
  margin-top: 20px;
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
