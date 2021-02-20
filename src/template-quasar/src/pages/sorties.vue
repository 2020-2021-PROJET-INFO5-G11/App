<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>Sorties</h1>
        <hr><br><br>
        <alert :message=message v-if="showMessage"></alert>
        <button type="button" class="btn btn-success btn-sm" v-b-modal.sortie-modal>Add Sortie</button>
        <br><br>
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">Name</th>
              <th scope="col">Type</th>
              <th scope="col">Priv?</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(sortie, index) in sorties" :key="index">
              <td>{{ sortie.name }}</td>
              <td>{{ sortie.type }}</td>
              <td>
                <span v-if="sortie.priv">Yes</span>
                <span v-else>No</span>
              </td>
              <td>
                <div class="btn-group" role="group">
                  <button
                          type="button"
                          class="btn btn-warning btn-sm"
                          v-b-modal.sortie-update-modal
                          @click="editSortie(sortie)">
                      Update
                  </button>
                  <button
                          type="button"
                          class="btn btn-danger btn-sm"
                          @click="onDeleteSortie(sortie)">
                      Delete
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
            title="Add a new sortie"
            hide-footer>
      <b-form @submit="onSubmit" @reset="onReset" class="w-100">
      <b-form-group id="form-name-group"
                    label="Name:"
                    label-for="form-name-input">
          <b-form-input id="form-name-input"
                        type="text"
                        v-model="addSortieForm.name"
                        required
                        placeholder="Enter name">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-type-group"
                      label="Type:"
                      label-for="form-type-input">
            <b-form-input id="form-type-input"
                          type="text"
                          v-model="addSortieForm.type"
                          required
                          placeholder="Enter type">
            </b-form-input>
          </b-form-group>
        <b-form-group id="form-priv-group">
          <b-form-checkbox-group v-model="addSortieForm.priv" id="form-checks">
            <b-form-checkbox value="true">Priv?</b-form-checkbox>
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
      <b-form-group id="form-name-edit-group"
                    label="Name:"
                    label-for="form-name-edit-input">
          <b-form-input id="form-name-edit-input"
                        type="text"
                        v-model="editForm.name"
                        required
                        placeholder="Enter name">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-type-edit-group"
                      label="Type:"
                      label-for="form-type-edit-input">
            <b-form-input id="form-type-edit-input"
                          type="text"
                          v-model="editForm.type"
                          required
                          placeholder="Enter type">
            </b-form-input>
          </b-form-group>
        <b-form-group id="form-priv-edit-group">
          <b-form-checkbox-group v-model="editForm.priv" id="form-checks">
            <b-form-checkbox value="true">Priv?</b-form-checkbox>
          </b-form-checkbox-group>
        </b-form-group>
        <b-button-group>
          <b-button type="submit" variant="primary">Update</b-button>
          <b-button type="reset" variant="danger">Cancel</b-button>
        </b-button-group>
      </b-form>
    </b-modal>
  </div>
</template>

<script>
import axios from 'axios';
import Alert from './alert.vue';
export default {
  data() {
    return {
      sorties: [],
      addSortieForm: {
        name: '',
        type: '',
        priv: [],
      },
      message: '',
      showMessage: false,
      editForm: {
        id: '',
        name: '',
        type: '',
        priv: [],
      },
    };
  },
  components: {
    alert: Alert,
  },
  methods: {
    getSorties() {
      const path = 'http://localhost:5000/sorties';
      axios.get(path)
        .then((res) => {
          this.sorties = res.data.sorties;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    addSortie(payload) {
      const path = 'http://localhost:5000/sorties';
      axios.post(path, payload)
        .then(() => {
          this.getSorties();
          this.message = 'Sortie added!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
          this.getSorties();
        });
    },
    initForm() {
      this.addSortieForm.name = '';
      this.addSortieForm.type = '';
      this.addSortieForm.priv = [];
      this.editForm.id = '';
      this.editForm.name = '';
      this.editForm.type = '';
      this.editForm.priv = [];
    },
    onSubmit(evt) {
      evt.preventDefault();
      this.$refs.addSortieModal.hide();
      let priv = false;
      if (this.addSortieForm.priv[0]) priv = true;
      const payload = {
        name: this.addSortieForm.name,
        type: this.addSortieForm.type,
        priv, // property shorthand
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
      let priv = false;
      if (this.editForm.priv[0]) priv = true;
      const payload = {
        name: this.editForm.name,
        type: this.editForm.type,
        priv,
      };
      this.updateSortie(payload, this.editForm.id);
    },
    updateSortie(payload, sortieID) {
      const path = `http://localhost:5000/sorties/${sortieID}`;
      axios.put(path, payload)
        .then(() => {
          this.getSorties();
          this.message = 'Sortie updated!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getSortiess();
        });
    },
    onResetUpdate(evt) {
      evt.preventDefault();
      this.$refs.editSortieModal.hide();
      this.initForm();
      this.getSorties(); // why?
    },
    removeSortie(sortieID) {
      const path = `http://localhost:5000/sorties/${sortieID}`;
      axios.delete(path)
        .then(() => {
          this.getSorties();
          this.message = 'Sortie removed!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getSortiess();
        });
    },
    onDeleteSortie(sortie) {
      this.removeSortie(sortie.id);
    },
  },
  created() {
    this.getSortiess();
  },
};
</script>