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
              <div class="rect" v-b-modal.sortie-modal>
                <img class="fit-picture" :src="getImgUrl(image)">
              </div>
            </div>

            <b-modal ref="addSortieModal"
                     id="sortie-modal"
                     title="Choisir une photo de couverture pour l'activité"
                     hide-footer>

              <div v-b-modal.sortie-modal>
                <div class="veritcal" style="text-align: center;" v-for="i in images" v-bind:key="i">
                  {{i}}
                  <br>
                  <img class="fit-picture" :src="getImgUrl(i)"
                       @click="setImage(i)" />
                  <br><br>
                </div>
              </div>

            </b-modal>

            <br><br><br>
            <label> Description </label>
            <div>
              <textarea cols="40" rows="5" style="width:300px; height:220px;" required/>
            </div>
          </li>

          <!-- center -->
          <li class="horizontal">

            <br><br><br><br>

            <div>
              <input v-model="nom" type="text" style="width: 500px;" placeholder="Nom" required/>
            </div>
            <br><br>
            <div>
              <input v-model="lieu" type="text" style="width: 500px;" placeholder="Lieu" required/>
            </div>
            <br><br>
            <div>
              <input v-model="rdv" type="text" style="width: 500px;"
                     placeholder="Point de rendez-vous" required/>
            </div>
            <br><br>
            <div>
              <span> Date et heure </span>
              <input  v-model="date" type="date" required/>
              <input  v-model="heure" type="time" required/>
            </div>
            <br><br>
            <div>
              <span> Date limite d'inscription </span>
              <input  v-model="limite" type="date" required/>
            </div>
            <br><br>
            <div>
              <span> Capacité minimum </span>
              <input  v-model="min" type="number" style="width:70px;" required/>
              <br><br>
              <span> Capacité maximum </span>
              <input  v-model="max" type="number" style="width:70px;" required/>
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
          <input class="submit" type="submit" value="Submit"> &ensp;
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
import Header from './header.vue';
import NavBar from './navBar.vue';
import Footer from './footer.vue';


export default {
  components: { Header, NavBar, Footer },
  data() {
    return {
      username: 'Vernet Maxime',
      nom: null,
      lieu: null,
      rdv: null,
      date: null,
      heure: null,
      limite: null,
      min: null,
      max: null,
      organisateurs: ['ElJraidi Rim', 'Sajide Idriss', 'Manissadjian Gabriel'],
      image: 'pas-de-photo',
      images: ['randonnée', 'cinema', 'musée'],
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
      this.nom = null;
      this.lieu = null;
      this.rdv = null;
      this.date = null;
      this.heure = null;
      this.limite = null;
      this.min = null;
      this.max = null;
      this.image = 'pas-de-photo';
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
      this.image = i;
      this.$refs.addSortieModal.hide();
    },
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

</style>
