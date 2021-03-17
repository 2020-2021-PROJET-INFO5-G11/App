<template>
  <div>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <!-- Header -->
    <Header title="Page de modification de sortie"/>
    <!-- NavBar -->
    <NavBar> </NavBar>
    <!-- Body -->
    <body>

      <!-- Formulaire -->
      <form id="app"
            @submit="edit"
            action="https://vuejs.org/"
            method="post">

        <br> <h1> ID sortie : {{ id }}  </h1> <br>

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

            <br><br><br>
            <label> Description </label>
            <div>
              <textarea v-model="description" @input="onChange()" cols="40" rows="5" style="width:300px; height:220px;" required/>
            </div>
          </li>

          <!-- center -->
          <li class="horizontal">

            <br><br><br><br>

            <div>
              <span> Préciser le type de la sortie </span>
              <select v-model="typeSortie" @change="onChange()">
                <option v-for="t in types" :key="t">
                  {{ t }}
                </option>
              </select>
              <br><br>
            </div>

            <div>
              <input v-model="nom" @input="onChange()" type="text" style="width: 500px;" placeholder="Nom" required/>
            </div>
            <br><br>
            <div>
              <input v-model="lieu" @input="onChange()" type="text" style="width: 500px;" placeholder="Lieu" required/>
            </div>
            <br><br>
            <div>
              <input v-model="point_rdv" @input="onChange()" type="text" style="width: 500px;"
                     placeholder="Point de rendez-vous" required/>
            </div>
            <br><br>
            <div>
              <span> Date et heure </span>
              <input  v-model="date" @input="onChange()" type="date" required/>
              <input  v-model="heure" @input="onChange()" type="time" required/>
              <span style="margin-left: 10px;"> Durée </span>
              <input v-model="duree" @input="onChange()" type="time" required/> 
            </div>
            <br><br>
            <div>
              <span> Date limite d'inscription </span>
              <input  v-model="dateLimite" @input="onChange()" type="date" required/>
            </div>
            <br><br>
            <div>
              <span> Capacité minimum </span>
              <input  v-model="capaciteMin" @input="onChange()" type="number" style="width:70px;" required/>
              <span style="margin-left: 10px;"> Capacité maximum </span>
              <input  v-model="capaciteMax" @input="onChange()" type="number" style="width:70px;" required/>
            <br><br>
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

            <h3> Champs optionnels </h3><br>

            <br>
            <div>
              <span> Restreindre à un groupe </span><br>
              <input type="text" style="width: 450px;" placeholder="ID du groupe"/>
              &ensp; <i class="add fa fa-group"></i>
            </div>
            <br><br>
            <div>
              <span> Ajouter un organisateur </span><br>
              <input type="text" style="width: 450px;"
                     v-model="organisateur" placeholder="ID ou nom de l'organisateur"/>
              &ensp; <i class="add fa fa-user" @click="ajouterOrganisateur()"></i>
            </div>
            <br><br>
            <span> Liste des organisateurs </span><br>
            <ul class = "scrollmenu">
              <br>
              <li class="veritcal">
                <span class="vertical"> {{current_user.prenom}} {{current_user.nom}} (vous) </span>
              </li>

              <li class="veritcal" v-for="o in organisateurs" v-bind:key="o">
                <span class="vertical"> {{o}} </span>
                <i class="fa fa-trash-o fa-1x" @click="suprimerOrganisateur(o)"></i>
              </li>
            </ul>
          </li>

        </ul>

        <br><br>

        <!-- submit button -->
        <div style="padding-left:800px">
          <input class="submit" type="submit" value="Modifier la sortie"> &ensp;
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
      lieu: '',
      date: '',
      heure: '',
      duree: '',
      point_rdv: '',
      capaciteMin: 1,
      capaciteMax: 50,
      privee: false,
      id_groupe: 0,
      typeSortie: 'Autre',
      photo: 'pas-de-photo',
      nbInscrits: 0,
      description: '',
      dateLimite: '',
      commentaires: '',
      //sortie: this.getSortie(),
      sortie: {},
      editForm: {}, 
      types: ['Autre', 'Cinéma', 'Culture', 'Musée', 'Musique', 'Repas', 'Sport'],
      current_user: {},
      organisateurs: [],
      images: ['cinema', 'escalade', 'escalade-sur-glace', 'football', 'foot-us', 'gymnastique', 'musée', 'parc', 'piscine', 'randonnée', 'rugby', 'salle-de-bloc', 'ski', 'tennis'],
      organisateur: null,
    };
  },
  methods: {
    checkForm() {
      this.submit = true;
      if (this.nom && this.lieu && this.point_rdv && this.date
      && this.heure && this.dateLimite && this.capaciteMin && this.capaciteMax && this.description) {
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
    getSortie() {
      const path = `http://localhost:5000/api/sortie/${this.$route.params.id}`;
      axios.get(path)
        .then((res) => {
          this.id = this.$route.params.id;
          this.nom = res.data.nom,
          this.editForm.nom = res.data.nom,
          this.lieu = res.data.lieu,
          this.editForm.lieu = res.data.lieu,
          this.date = res.data.date,
          this.editForm.date = res.data.date,
          this.heure = res.data.heure,
          this.editForm.heure = res.data.heure,
          this.duree = res.data.duree,
          this.editForm.duree = res.data.duree,
          this.point_rdv = res.data.point_rdv,
          this.editForm.point_rdv = res.data.point_rdv,
          this.capaciteMin = res.data.capaciteMin,
          this.editForm.capaciteMin = res.data.capaciteMin,
          this.capaciteMax = res.data.capaciteMax,
          this.editForm.capaciteMax = res.data.capaciteMax,
          this.editForm.privee = res.data.privee,
          this.editForm.id_groupe = res.data.id_groupe,
          this.typeSortie = res.data.typeSortie,
          this.editForm.typeSortie = res.data.typeSortie,
          this.photo = res.data.photo,
          this.editForm.photo = res.data.photo,
          this.nbInscrits = res.data.nbInscrits,
          this.editForm.nbInscrits = res.data.nbInscrits,
          this.description = res.data.description,
          this.editForm.description = res.data.description,
          this.dateLimite = res.data.dateLimite,
          this.editForm.dateLimite = res.data.dateLimite,
          //this.editForm.commentaires = res.data.commentaires,
          this.sortie = res.data;
        })
        .catch((error) => {
          console.error(error);
        });
    },
    ajouterOrganisateur() {
      let exist = false;
      if (this.organisateur) {
        this.organisateurs.forEach((value) => {
          if (value === this.organisateur) {
            exist = true;
          }
        });
        if (!exist) {
          this.organisateurs.push(this.organisateur);
        }
      }
    },
    suprimerOrganisateur(o) {
      this.organisateurs.forEach((value, index) => {
        if (value === o) {
          this.organisateurs.splice(index, 1);
        }
      });
    },
    getImgUrl(image) {
      return require('../'+image+'.jpg');
    },
    setImage(i) {
      this.editForm.photo = i;
      this.photo = i;
    },
    onHide(evt) {
      evt.preventDefault();
      this.$refs.addPhoto.hide("photo-modal");
    },
    onChange() {
      this.editForm.nom = this.nom;
      this.editForm.lieu = this.lieu;
      this.editForm.date = this.date;
      this.editForm.heure = this.heure;
      this.editForm.duree = this.duree;
      this.editForm.point_rdv = this.point_rdv;
      this.editForm.nbInscrits = this.nbInscrits;
      this.editForm.capaciteMin = this.capaciteMin;
      this.editForm.capaciteMax = this.capaciteMax;
      this.editForm.typeSortie = this.typeSortie;
      this.editForm.photo = this.photo;
      this.editForm.description = this.description;
      this.editForm.dateLimite = this.dateLimite;      
    },
    updateSortie(payload, sortieID) {
      const path = `http://localhost:5000/api/sortie/${sortieID}`;
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
          lieu: this.editForm.lieu,
          date: this.editForm.date,
          heure: this.editForm.heure,
          duree: this.editForm.duree,
          point_rdv: this.editForm.point_rdv,
          nbInscrits: this.editForm.nbInscrits,
          capaciteMin: parseInt(this.editForm.capaciteMin),
          capaciteMax: parseInt(this.editForm.capaciteMax),
          privee: this.editForm.privee,
          // id_groupe: this.editForm.id_groupe,
          typeSortie: this.editForm.typeSortie,
          photo: this.editForm.photo,
          nbInscrits: this.editForm.nbInscrits,
          description: this.editForm.description,
          dateLimite: this.editForm.dateLimite,
          //commentaires: this.editForm.commentaires,
        };
        this.updateSortie(payload, this.id);
      }
    }
  },
  created() {
      this.getSortie();
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
