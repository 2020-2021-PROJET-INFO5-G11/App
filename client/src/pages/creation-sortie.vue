<template>
  <div>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <!-- Header -->
    <Header title="Page de création de sortie"/>
    <!-- NavBar -->
    <NavBar> </NavBar>
    <!-- Body -->
    <body>

      <!-- Formulaire -->
      <form id="app"
            @submit="checkForm"
            @reset="reset"
            action="https://vuejs.org/"
            method="post">

        <br> <h1> Créer une sortie </h1> <br>

        <!-- columns -->
        <ul>

          <!-- left -->
          <li class="horizontal" style="width:300px;">

            <h3> Champs obligatoires </h3><br>

            <div>
              <label> Photo </label>
              <div class="rect">
                <img @click="$bvModal.show('photo-modal')" class="fit-picture" :src="getImgUrl(addSortieForm.photo)">
              </div>
            </div>

            <b-modal ref="addPhoto"
                     id="photo-modal"
                     title="Choisir une photo de couverture pour l'activité"
                     hide-footer>

              <div>
                <div class="veritcal" style="text-align: center;" v-for="i in images" v-bind:key="i">
                  {{i}}
                  <br>
                  <img class="fit-picture" :src="getImgUrl(i)" @click="$bvModal.hide('photo-modal')"
                       v-on:click="setImage(i)"/>
                  <br><br>
                </div>
              </div>

            </b-modal>

            <br><br><br>
            <label> Description </label>
            <div>
              <textarea v-model="addSortieForm.description" cols="40" rows="5" style="width:300px; height:220px;" required/>
            </div>
          </li>

          <!-- center -->
          <li class="horizontal">

            <br><br><br><br>

            <div>
              <span> Préciser le type de la sortie </span>
              <select v-model="addSortieForm.typeSortie">
                <option v-for="t in types" :key="t">
                  {{ t }}
                </option>
              </select>
              <br><br>
            </div>

            <div>
              <input v-model="addSortieForm.nom" type="text" style="width: 500px;" placeholder="Nom" required/>
            </div>
            <br><br>
            <div>
              <input v-model="addSortieForm.lieu" type="text" style="width: 500px;" placeholder="Lieu" required/>
            </div>
            <br><br>
            <div>
              <input v-model="addSortieForm.point_rdv" type="text" style="width: 500px;"
                     placeholder="Point de rendez-vous" required/>
            </div>
            <br><br>
            <div>
              <span> Date et heure </span>
              <input  v-model="addSortieForm.date" type="date" required/>
              <input  v-model="addSortieForm.heure" type="time" required/>
              <span style="margin-left: 10px;"> Durée </span>
              <input v-model="addSortieForm.duree" type="time" required/> 
            </div>
            <br><br>
            <div>
              <span> Date limite d'inscription </span>
              <input  v-model="addSortieForm.dateLimite" type="date" required/>
            </div>
            <br><br>
            <div>
              <span> Capacité minimum </span>
              <input  v-model="addSortieForm.capaciteMin" type="number" style="width:70px;" required/>
              <span style="margin-left: 10px;"> Capacité maximum </span>
              <input  v-model="addSortieForm.capaciteMax" type="number" style="width:70px;" required/>
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
                <span class="vertical"> {{username}} (vous) </span>
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
          <input class="submit" @click="submit" type="submit" value="Submit"> &ensp;
          <input class="reset" type="reset" value="Reset">
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
      username: 'Vernet Maxime',
      addSortieForm: {
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
      },
      types: ['Autre', 'Cinéma', 'Culture', 'Musée', 'Musique', 'Repas', 'Sport'],
      organisateurs: ['ElJraidi Rim', 'Sajide Idriss', 'Manissadjian Gabriel'],
      images: ['randonnée', 'cinema', 'musée', 'parc'],
      organisateur: null,
    };
  },
  methods: {
    checkForm(e) {
      if (this.nom && this.lieu && this.rdv && this.date
      && this.heure && this.limite && this.min && this.max) {
        return true;
      }

      this.submit = true;

      e.preventDefault();
      return false;
    },
    reset() {
      this.addSortieForm = {
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
        commentaires: [],
      }
      this.organisateurs = ['ElJraidi Rim', 'Sajide Idriss', 'Manissadjian Gabriel'];
      this.organisateur = null;
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
      this.addSortieForm.photo = i;
    },
    onHide(evt) {
      evt.preventDefault();
      this.$refs.addPhoto.hide("photo-modal");
    },
    addSortie(payload) {
      const path = 'http://localhost:5000/api/sortie';
      axios.post(path, payload)
        .then(() => {
          this.getSorties();
          this.message = 'Sortie added!';
          this.showMessage = true;
        })
        .catch((error) => {
          console.log(error);
          this.getSorties();
        });
    },
    submit(evt) {
      evt.preventDefault();
      const payload = {
        nom: this.addSortieForm.nom,
        lieu: this.addSortieForm.lieu,
        date: this.addSortieForm.date,
        heure: this.addSortieForm.heure,
        duree: this.addSortieForm.duree,
        point_rdv: this.addSortieForm.point_rdv,
        nbInscrits: 1,
        capaciteMin: parseInt(this.addSortieForm.capaciteMin),
        capaciteMax: parseInt(this.addSortieForm.capaciteMax),
        privee: this.addSortieForm.privee,
        id_groupe: this.addSortieForm.id_groupe,
        typeSortie: this.addSortieForm.typeSortie,
        photo: this.addSortieForm.photo,
        nbInscrits: this.addSortieForm.nbInscrits,
        description: this.addSortieForm.description,
        dateLimite: this.addSortieForm.dateLimite,
        //commentaires: this.addSortieForm.commentaires,
      };
      this.addSortie(payload);
      this.$router.push({path: `/sorties`});
    }
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
