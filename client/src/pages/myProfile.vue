<template>
  <div>

    <link
      rel="stylesheet"
      href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css"
    />

    <!-- Header -->
    <Header title='Votre profil' />
    <!-- NavBar -->
    <NavBar />

    <!-- Body -->
    <body>
      <br />

      <!-- Title + buttons -->
      <div>
        <!-- Title : current activity's name and current activty's ID -->
        <span class="title"> {{user.nom}}  {{user.prenom}} </span>
      </div>

      <!-- view members pannel-->
      <b-modal ref="showMembers" id="show-members" hide-footer
        title="Liste des participants">
        <div>
          <div style="text-align: center; font-size: 30px;">
            <br>
            <!-- User -->
            <div v-if="is_subscribed"
                 class="user">
              {{ userName }} ( vous )
              <br>
            </div>
            <!-- Other members -->
            <div v-for="m in members" v-bind:key="m"
                 class="member">
              {{ m }}
              <br>
            </div>
            <br><br>

            <!-- Suscribe/Unsuscribe-->
            <button v-if="!is_subscribed" v-on:click="is_subscribed = true"
                    class="subscribe2">
              S'inscrire
            </button>
            <button v-if="is_subscribed" v-on:click="is_subscribed = false"
                    class="subscribe2">
              Se désinscrire
            </button>
            <br><br>
          </div>
        </div>
      </b-modal>

      <br><br>

      <!-- Photo + description -->
      <ul>
        <!-- User's photo-->

        <!-- Description -->
        <li style="height: 250px;" class="resume">
          <span class="resumeTitle">
            Bio :
          </span>
          <br><br>
          <span class="resumeContent">
            {{ user.bio }}
          </span>
        </li>
      </ul>

      <!-- Location, Date etc.. --> 
      <ul>
        <li>
          <span class="location">
            {{ user.email }}
          </span>

          <br>
          
          <span class="date">
            {{ user.sexe }} - {{ user.ville }}
          </span>

          <br>
          
          <span class="duree">
            Né(e) le : {{ user.dateNaissance }}
          </span>

          <br><br>
        </li>

        <!-- Separateur -->
        <li style="padding: 10px;">
          <div class="separator">
            <br><br><br><br><br>
          </div>
        </li>

        <li>
          <span class="rdv">
            Preferences : {{ user.preferences}}
          </span>

          <br>  

          <br><br><br>
        </li>
      </ul>

      <!-- Edit button -->
      <div @click="$router.push({path: `/modifier_profil/${user.id}`})" class="edit">
        <img src="../assets/edit.png" width="60">
        <br> <span> Modifier </span>
      </div>

      <!-- Separator -->
      <br><br><br><br>
      <div class="horizontalSeparator">
        <br>
      </div>

      <br><br><br>
    </body>
    <!-- Footer -->
    <Footer />

  </div>
</template>

<script>
import axios from "axios";
import Header from "./header.vue";
import NavBar from "./navBar.vue";
import Footer from "./footer.vue";

export default {
  name: "user",
  components: { Header, NavBar, Footer },
  data() {
    return {
      pseudo: '',
      password_hash: '',
      prenom: '',
      nom: '',
      email: '',
      photo: '',
      dateNaissance: '',
      ville: '',
      preferences: '',
      sexe: '',
      bio: '',
      activites_a_venir: '',
      activites_finies: '',
      activites_organisees: '',
      role: '',
      feedbacks: '',
      user: {},
    };
  },
  methods: {

    getUser() {
      const path = `http://localhost:5000/api/user/${this.$route.params.id}`;
      axios.get(path)
        .then((res) => {
          this.user = res.data;
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
  created() {
    this.getUser();
  },
};
</script>

<style scoped>

.edit {
  float: right; 
  padding-right: 8%;
  cursor: pointer;
  font-size: 13px;
}

.title {
  margin-left: 20px;
  font-size: 40px;
}

.showMembers {
  font-size: 30px;
  text-decoration: bold;
  background-color: rgb(61, 150, 135);
  border-color: white;
  color: whitesmoke;
}

.user:hover {
  font-size: 32px;
}

.member:hover {
  font-size: 32px;
  text-decoration: underline;
}

.subscribe {
  font-size: 30px;
  margin-left: 10px;
  margin-right: 20px;
  background-color: rgb(61, 150, 135);
  border-color: white;
  color: whitesmoke;
}

.subscribe2 {
  font-size: 25px;
  background-color: rgb(61, 150, 135);
  border-color: white;
  color: whitesmoke;
}

.button {
  font-size: 32px;
  background-color: rgb(15, 138, 117);
  cursor: pointer;
  opacity: 0.7;
}

.subscribe:hover {
  font-size: 32px;
  background-color: rgb(15, 138, 117);
  cursor: pointer;
  opacity: 0.7;
}

.subscribe2:hover {
  font-size: 27px;
  background-color: rgb(15, 138, 117);
  cursor: pointer;
  opacity: 0.7;
}

.fit-picture {
  width: 320px;
  height: 210px;
}

li {
  display: inline-block;
  vertical-align: top;
  margin-left: 30px;
}

.resume {
  max-height: 210px;
  width: 1200px;
  overflow-x: scroll;
}

.resumeTitle {
  font-size: 25px;
}

.resumeContent {
  font-size: 20px;
}

.location {
  padding-left: 70px;
  font-size: 25px;
}

.date {
  padding-left: 70px;
  font-size: 20px;
}

.duree {
  padding-left: 70px;
  font-size: 18px;
}

.capacity, .rdv {
  font-size: 20px;
}

.separator {
  border: solid; 
  width: 2px;
  border-width:1px; 
  border-color: grey;
}

.horizontalSeparator {
  border: solid; 
  height: 2px;
  width: 90%;
  margin-left: 5%;
  border-width:1px; 
  border-color: grey;
}

.comments {
  margin-left: 40%;
}

.comment {
  margin-left: 10%;
  margin-top : 10px;
  border: solid;
  border-color:  rgb(15, 138, 117);
  width: 80%;
}

.comment:hover {
  cursor: pointer;
  opacity: 0.7;
}

.modal-backdrop
{
    opacity:0.5 !important;
}

</style>
