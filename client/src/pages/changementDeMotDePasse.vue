<template>
    <div>
        <q-form :style="$q.platform.is.desktop ? 'width:55%;margin: auto;' : 'margin: auto;'"
        class="q-gutter-md">
                  <span class="text-subtitle1 text-weight-bold text-grey-7">
                    Changement de mot de passe</span>
                  <q-input
                    dense
                    outlined
                    v-model="username"
                    label="Pseudo"
                    lazy-rules
                  />

                  <q-input
                    dense
                    type="password"
                    outlined
                    v-model="password"
                    label="Mot de passe"
                    lazy-rules
                  />
                  <div>
                    <q-btn class="text-capitalize" size="sm" style="width:75px" dense
                     label="Mettre à jour" to="/home" type="button"
                           color="primary"/>
                  </div>
        </q-form>
    </div>
</template>
