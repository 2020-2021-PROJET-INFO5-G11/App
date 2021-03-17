<template>
  <div>

    <link
      rel="stylesheet"
      href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css"
    />

    <!-- Header -->
    <Header :title='groupe.nom' />
    <!-- NavBar -->
    <NavBar />

    <!-- Body -->
    <body>
      <br />

      <!-- Title + buttons -->
      <div>
        <!-- Title : current activity's name and current activty's ID -->
        <span class="nom"> {{groupe.nom}} &ensp;-&ensp; </span>
        <span class="id">ID: {{id}} </span>

        <!-- Buttons : show members and accept/refuse-->
        <div style="float: right; margin-right: 1%;">
          <button @click="$bvModal.show('show-members')" class="showMembers">
            Voir les membres
          </button>
          <button v-if="is_invited"
            @click="accept(id)"
            :disabled="!is_invited" class="subscribe">
            Accepter l'invitation
          </button>
          <button v-if="is_invited"
            @click="refuse(id)"
            :disabled="!is_invited" class="subscribe">
            Refuser l'invitation
          </button>
          <button v-if="is_member"
            @click="$bvModal.show('invite-member')"
            :disabled="!is_invited" class="inviteMember">
            Inviter à rejoindre
          </button>
          <br>
        </div>
      </div>

      <!-- view members pannel-->
      <b-modal ref="showMembers" id="show-members" hide-footer
        title="Liste des membres">
        <div>
          <div style="text-align: center; font-size: 30px;">
            <br>
            <!-- User -->
            <div v-if="is_member"
                 class="user">
              {{ current_user.prenom }} {{ current_user.nom }} ( vous )
              <br>
            </div>
            <!-- Other members -->
            <div v-for="m in groupe.membres" v-bind:key="m"
                 class="member">
              <div v-if="m.userName !== current_user.userName">
                {{ m.prenom }} {{ m.nom }}
              </div>
              <br>
            </div>
            <br><br>

            <br><br>
          </div>
        </div>
      </b-modal>

      <b-modal ref="inviteMember" id="invite-member" hide-footer
        title="Inviter un utilisateur">
        <div>
          <div style="text-align: center; font-size: 30px;">
            <br>
            <div v-for="u in utilisateurs" v-bind:key="u"
                 class="user">
              <div v-if="u.userName !== current_user.userName">
                <span @click="invite(this.id, u.id)" class="user"> {{u.nom }} {{u.prenom}} </span>
              </div>
              <br>
            </div>
            <br><br>

            <br><br>
          </div>
        </div>
      </b-modal>

      <br><br>

      <!-- Photo + type + description -->
      <ul>
        <!-- Activity's photo-->
        <li style="height: 250px;">
          <div class="rect img-container" @click="$router.push({path: `/groupe/${groupe.id_groupe}`})">
          </div> <br>
        </li>

        <!-- Type + Description -->
        <li style="height: 250px;" class="resume">
          <span class="resumeTitle">
            Nom : 
          </span>
          <span class="resumeContent">
            {{groupe.nom}}
          </span><br><br>
          <span class="resumeTitle">
            Description :
          </span>
          <br><br>
          <span class="resumeContent">
            {{ groupe.description }}
          </span>
        </li>
      </ul>
      
      <!-- Edit button -->
      <div @click="$router.push({path: `/modification-groupe/${id}`})" class="edit">
        <img src="../edit.png" width="60">
        <br> <span> Modifier </span>

      </div>

      <br><br>

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
  name: "groupe",
  components: { Header, NavBar, Footer },
  data() {
    return {
      current_user: {},
      id: '0',
      is_invited: false,
      accepted: false,
      is_member: false,
      groupe: {},
      utilisateurs: [],
    };
  },
  methods: {

    getGroupe() {
      const path = `http://localhost:5000/api/groupe/${this.$route.params.id}`;
      axios.get(path)
        .then((res) => {
          this.id = this.$route.params.id;
          this.groupe = res.data;
          this.getCurrentUser();
        })
        .catch((error) => {
          console.error(error);
        });
    },
    getUtilisateurs() {
      const path = 'http://localhost:5000/api/user';
      axios.get(path)
        .then((res) => {
          this.utilisateurs = res.data;
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
          // Is invited
          for(const p in this.groupe.demandes){
            if(p.userName === this.current_user.userName)
              this.is_invited = true;
              break;
          }
          // Is member
          for(const p in this.groupe.membres){
            if(p.userName === this.current_user.userName)
              this.is_member = true;
              break;
          }
        })
        .catch((error) => {
          console.error(error);
        });
    },
    accept(groupeID) {
      const path = `http://localhost:5000/api/groupe/${groupeID}/membres`;
      axios.post(path)
        .then((res) => {
          this.accepted = true;
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
    invite(groupeID, userID) {
      const path = `http://localhost:5000/api/POST /groupe/${groupeID}/demandes`;
      axios.post(path, userID)
        .then((res) => {
          this.$router.go();
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
  async created() {
    this.getGroupe();
    this.getUtilisateurs();
  },
};
</script>

<style scoped>

.nom {
  margin-left: 20px;
  font-size: 40px;
}

.id {
  font-size: 45px;
  font-family:'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
}

.id:hover {
  font-size: 50px;
  cursor: copy;
}

.edit {
  float: right; 
  padding-right: 8%;
  cursor: pointer;
  font-size: 13px;
}

.showMembers {
  width: 350px;
  height: 60px;
  font-size: 30px;
  text-decoration: bold;
  background-color: rgb(61, 150, 135);
  border-color: white;
  color: whitesmoke;
}

.inviteMember {
  width: 350px;
  height: 60px;
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

.membersCount {
  padding-left: 50px;
  text-align: center;
  width: 350px;
  height: 60px;
  font-size: 20px;
}

.remainingPlaces {
  padding-left: 50px;
  text-align: center;
  width: 250px;
  height: 60px;
  font-size: 20px;
}

.subscribe {
  width: 300px;
  height: 60px;
  font-size: 30px;
  margin-left: 10px;
  margin-right: 20px;
  background-color: rgb(61, 150, 135);
  border-color: white;
  color: whitesmoke;
}

.subscribe2 {
  padding: 10px;
  font-size: 25px;
  background-color: rgb(61, 150, 135);
  border-color: white;
  color: whitesmoke;
}

.showMembers:hover {
  font-size: 32px;
  background-color: rgb(15, 138, 117);
  cursor: pointer;
  opacity: 0.7;
}

.inviteMember:hover {
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
  width: 600px;
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

.img-container {
     position: relative;
}

.overlay-img {
     position: absolute;
     top: 0;
     left: 0;
}

</style>
