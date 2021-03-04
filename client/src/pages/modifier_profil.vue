<template>
  <div>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <!-- Header -->
    <Header title="Modification profil"/>
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

        <br> <h1> Modification profil </h1> <br>

        <!-- columns -->
        <ul>

          <!-- left -->
          <li class="horizontal" style="width:300px;">

            <h3> Champs obligatoires </h3><br>

            <div>
              <label> Photo </label>
              <div class="rect">
                <img @click="$bvModal.show('photo-modal')" class="fit-picture" :src="getImgUrl(editUserForm.photo)">
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
            <label> Bio </label>
            <div>
              <textarea v-model="editUserForm.bio" cols="40" rows="5" style="width:300px; height:220px;" required/>
            </div>
          </li>

          <!-- center -->
          <li class="horizontal">

            <br><br><br><br>

            <div>
              <input v-model="editUserForm.nom" type="text" style="width: 500px;" placeholder="Nom" required/>
            </div>
            <br><br>
            <div>
              <input v-model="editUserForm.prenom" type="text" style="width: 500px;" placeholder="Prenom" required/>
            </div>
            <br><br>
        </li>
        </ul>
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
      editUserForm: {
        nom: '',
        prenom: '',
        bio: '',
        photo: 'pas-de-photo',
      },
      images: ['randonnée', 'cinema', 'musée', 'parc'],
    };
  },
  methods: {
    checkForm(e) {
      if (this.nom && this.prenom) {
        return true;
      }

      this.submit = true;

      e.preventDefault();
      return false;
    },
    reset() {
      this.editUserForm = {
        nom: '',
        prenom: '',
        bio:'',
        photo: 'pas-de-photo',
      }
    },
    getImgUrl(image) {
      return require('../'+image+'.jpg');
    },
    setImage(i) {
      this.editUserForm.photo = i;
    },
    onHide(evt) {
      evt.preventDefault();
      this.$refs.addPhoto.hide("photo-modal");
    },
    submit(evt) {
      evt.preventDefault();
      const payload = {
        nom: this.editUserForm.nom,
        prenom: this.editUserForm.prenom,
        bio: this.editUserForm.bio,
        photo: this.editUserForm.photo,
      };
      this.updateUser(payload, 0);
      this.$router.push({path: `/profil/${this.$route.params.id}`});
    },
    updateUser(payload, userID) {
      const path = `http://localhost:5000/api/user/${userID}`;
      axios.put(path, payload)
        .then(() => {
          this.message = 'User mise à jour!';
        })
        .catch((error) => {
          console.error(error);
        });
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

.modal-backdrop {
    opacity:0.5 !important;
}

</style>
