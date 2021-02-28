<template>
  <div>
    <!-- Header -->
    <Header title="Page temporaire"/>
    <!-- NavBar -->
    <NavBar> </NavBar>
    <!-- Sorties -->
    <div class="row">
      <div class="col-sm-10">
        <h1>Sorties</h1>
        <hr><br><br>
        <alert :message=message v-if="showMessage"></alert>
        <button type="button" class="btn btn-success btn-sm" v-b-modal.sortie-modal>
          Créer une nouvelle Sortie
        </button>
        <br><br>
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">Nom</th>
              <th scope="col">Type</th>
              <th scope="col">Privée ?</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(sortie, index) in sorties" :key="index">
              <td>{{ sortie.nom }}</td>
              <td>{{ sortie.typeSortie }}</td>
              <td>
                <span v-if="sortie.privee">Oui</span>
                <span v-else>Non</span>
              </td>
              <td>
                <div class="btn-group" role="group">
                  <button
                          type="button"
                          class="bouton"
                          v-b-modal.sortie-view-modal
                          @click="$router.push({path: `/sortie/${sortie.id_sortie}`})">
                      Voir sortie
                  </button>
                  <button
                          type="button"
                          class="btn btn-warning btn-sm"
                          v-b-modal.sortie-update-modal
                          @click="editSortie(sortie)">
                      Modifier
                  </button>
                  <button
                          type="button"
                          class="btn btn-danger btn-sm"
                          @click="onDeleteSortie(sortie)">
                      Supprimer
                  </button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    <b-modal ref="addSortieModal"
            id="sortie-modal"
            title="Créer une nouvelle sortie"
            hide-footer>
      <b-form @submit="onSubmit" @reset="onReset" class="w-100">
      <b-form-group id="form-title-group"
                    label="Nom:"
                    label-for="form-title-input">
          <b-form-input id="form-title-input"
                        type="text"
                        v-model="addSortieForm.nom"
                        required
                        placeholder="Enter title">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-author-group"
                      label="Type:"
                      label-for="form-author-input">
            <b-form-input id="form-author-input"
                          type="text"
                          v-model="addSortieForm.typeSortie"
                          required
                          placeholder="Enter author">
            </b-form-input>
          </b-form-group>
        <b-form-group id="form-read-group">
          <b-form-checkbox-group v-model="addSortieForm.privee" id="form-checks">
            <b-form-checkbox value="true">Privée?</b-form-checkbox>
          </b-form-checkbox-group>
        </b-form-group>
        <b-button-group>
          <b-button type="submit" variant="primary">Submit</b-button>
          <b-button type="reset" variant="danger">Reset</b-button>
        </b-button-group>
      </b-form>
    </b-modal>
    <b-modal ref="editSortieModal"
            id="sortie-update-modal"
            title="Update"
            hide-footer>
      <b-form @submit="onSubmitUpdate" @reset="onResetUpdate" class="w-100">
      <b-form-group id="form-title-edit-group"
                    label="Title:"
                    label-for="form-title-edit-input">
          <b-form-input id="form-title-edit-input"
                        type="text"
                        v-model="editForm.nom"
                        required
                        placeholder="Enter title">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-author-edit-group"
                      label="Author:"
                      label-for="form-author-edit-input">
            <b-form-input id="form-author-edit-input"
                          type="text"
                          v-model="editForm.typeSortie"
                          required
                          placeholder="Enter author">
            </b-form-input>
          </b-form-group>
        <b-form-group id="form-read-edit-group">
          <b-form-checkbox-group v-model="editForm.privee" id="form-checks">
            <b-form-checkbox value="true">Privée?</b-form-checkbox>
          </b-form-checkbox-group>
        </b-form-group>
        <b-button-group>
          <b-button type="submit" variant="primary">Update</b-button>
          <b-button type="reset" variant="danger">Cancel</b-button>
        </b-button-group>
      </b-form>
    </b-modal>

    <!-- Footer -->
    <Footer />
    <div :key="key"></div>
  </div>
</template>

<script>
import axios from 'axios';
import Alert from './Alert.vue';
import Header from './header.vue';
import NavBar from './navBar.vue';
import Footer from './footer.vue';

export default {
  data() {
    return {
      key: 0,
      sorties: [],
      addSortieForm: {
        nom: '',
        typeSortie: '',
        privee: [],
      },
      message: '',
      showMessage: false,
      editForm: {
        id_sortie: '',
        nom: '',
        typeSortie: '',
        privee: [],
      },
    };
  },
  components: {
    alert: Alert, Header, NavBar, Footer,
  },
  methods: {
    forceRerender() {
      this.key += 1;
    },
    getSorties() {
      const path = 'http://localhost:5000/api/sorties/get_all';
      axios.get(path)
        .then((res) => {
          this.sorties = res.data;
        })
        .catch((error) => {
          console.error(error);
        });
    },
    addSortie(payload) {
      const path = 'http://localhost:5000/api/sortie/create';
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
    initForm() {
      this.addSortieForm.nom = '';
      this.addSortieForm.typeSortie = '';
      this.adSortieForm.privee = [];
      this.editForm.id_sortie = '';
      this.editForm.nom = '';
      this.editForm.typeSortie = '';
      this.editForm.privee = [];
    },
    onSubmit(evt) {
      evt.preventDefault();
      this.$refs.addSortieModal.hide();
      let privee = false;
      if (this.addSortieForm.privee[0]) privee = true;
      const payload = {
        nom: this.addSortieForm.nom,
        typeSortie: this.addSortieForm.typeSortie,
        privee,
      };
      this.addSortie(payload);
      this.initForm();
    },
    onReset(evt) {
      evt.preventDefault();
      this.$refs.addSortieModal.hide();
      this.initForm();
    },
    editSortie(sortie) {
      this.editForm = sortie;
    },
    onSubmitUpdate(evt) {
      evt.preventDefault();
      this.$refs.editSortieModal.hide();
      let privee = false;
      if (this.editForm.privee[0]) privee = true;
      const payload = {
        nom: this.editForm.nom,
        typeSortie: this.editForm.typeSortie,
        privee,
      };
      this.updateSortie(payload, this.editForm.id);
    },
    updateSortie(payload, sortieID) {
      const path = `http://localhost:5000/api/sorties/get_one/${sortieID}`;
      axios.put(path, payload)
        .then(() => {
          this.getSorties();
          this.message = 'Sortie updated!';
          this.showMessage = true;
        })
        .catch((error) => {
          console.error(error);
          this.getSorties();
        });
    },
    onResetUpdate(evt) {
      evt.preventDefault();
      this.$refs.editSortieModal.hide();
      this.initForm();
      this.getSorties();
    },
    removeSortie(sortieID) {
      const path = `http://localhost:5000/api/sorties/get_one/${sortieID}`;
      axios.delete(path)
        .then(() => {
          this.getSorties();
          this.message = 'Sortie removed!';
          this.showMessage = true;
        })
        .catch((error) => {
          console.error(error);
          this.getSorties();
        });
    },
    onDeleteSortie(sortie) {
      this.removeSortie(sortie.id_sortie);
    },
  },
  created() {
    this.getSorties();
  },
};
</script>

<style>
  .bouton {
    background-color: rgb(65, 192, 171);
  }
</style>
