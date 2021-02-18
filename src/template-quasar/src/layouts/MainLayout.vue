<template>
  <q-layout view="lHh LpR lFf" style="font-family: Lato"
    >

    <q-header reveal elevated style="background-color: #1f509e">
      <q-toolbar v-if="!$q.platform.is.desktop" class="q-py-sm">
        <div class="row">
          <div class="col-sm-12 col-xs-12">
            <q-toolbar-title>
              <img
                @click="$router.push({ name: 'home' })"
                class="cursor-pointer float-left"
                src="statics/images/logo.png"
                style="width: 12%"
              />
              <span
                class="float-left q-mt-xs q-ml-md text-h6 text-weight-bold"
                style="font-size: 17px"
                >Osons Sortir</span>
            </q-toolbar-title>
          </div>
          <div class="col-sm-12 col-xs-12 q-mt-md">
            <q-input
              class="float-left q-mx-md full-width"
              square
              bg-color="white"
              dense
              outlined
              v-model="text"
              label="Search for products, brands and more"
            />
          </div>
          <div class="col-sm-12 col-xs-12 q-mt-md">
            <div>
              <q-btn class="q-mr-md" dense round flat icon="shopping_cart">
                <q-badge color="red" class="text-bold" floating transparent> 4 </q-badge>
              </q-btn>
              <q-btn flat round dense icon="settings" class="q-mr-md" />
              <q-btn flat round dense icon="fas fa-sign-out-alt" to="/" />
            </div>
          </div>
        </div>
</q-toolbar>


         


      
      <q-toolbar v-if="$q.platform.is.desktop" class="q-py-sm">
        <!--          <q-btn @click="left = !left" flat round dense icon="menu" class="q-mr-sm" />-->
        <img
          @click="$router.push('/home')"
          class="cursor-pointer"
          src="statics/images/logo.png"
          style="width: 3%"
        />
        <q-toolbar-title>
          <span
            class="float-left q-mt-xs text-h6 text-weight-bold"
            style="font-size: 17px"
            >Osons Sortir</span
          >
          <q-input
            class="float-left q-ml-xl"
            style="width: 650px"
            square
            bg-color="white"
            dense
            outlined
            v-model="text"
            label="Search for products, brands and more"
          />
        </q-toolbar-title>

        <q-btn color="primary" label="Menu Principal">
        <q-menu>
          <q-list style="min-width: 100px">

            <q-item clickable v-close-popup>
              <q-item-section>Mes sorties</q-item-section>
            </q-item>

            <q-item clickable v-close-popup>
              <q-item-section>Mes groupes</q-item-section>
            </q-item>
          
          </q-list>
        </q-menu> 
      </q-btn>



      <q-btn color="primary" label="Menu Principal2">
        <q-menu>
          <q-list style="min-width: 100px">
          
            <q-item clickable v-close-popup>
              <q-item-section>Mes sorties</q-item-section>
            </q-item>

          <q-item clickable v-close-popup>
          <img
          @click="$router.push('/')"
          class="cursor-pointer"
          src="https://cdn0.iconfinder.com/data/icons/pinpoint-interface/48/profile-512.png"
          style="width: 3%"
        />
        </q-item>


          
          </q-list>
        </q-menu> 
          </q-btn>



        <q-btn flat round dense icon="settings" class="q-mr-md" />
        <img
          @click="$router.push('/')"
          class="cursor-pointer"
          src="https://cdn0.iconfinder.com/data/icons/pinpoint-interface/48/profile-512.png"
          style="width: 3%"
        />

      </q-toolbar>


    </q-header>

    <q-page-container style="background-color: #f1f2f6">
      <router-view />
      <div class="q-mt-sm">
        <div class="row q-pa-md bg-primary">
          <div class="col-lg-1 col-md-1 col-sm-12 col-xs-12"></div>
          <div class="col-lg-2 col-md-2 col-sm-12 col-xs-12 text-white">
            <div class="text-subtitle1 text-weight-bold">About</div>
            <div class="text-caption hover_underline_white q-mt-sm">Contact us</div>
            <div class="text-caption hover_underline_white">About Us</div>
            <div class="text-caption hover_underline_white">Careers</div>
            <div class="text-caption hover_underline_white">Our Stories</div>
            <div class="text-caption hover_underline_white">Press</div>
          </div>
          <div class="col-lg-2 col-md-2 col-sm-12 col-xs-12 text-white">
            <div class="text-subtitle1 text-weight-bold">Connect with Us</div>
            <div class="text-caption hover_underline_white q-mt-sm">Facebook</div>
            <div class="text-caption hover_underline_white">Instagram</div>
            <div class="text-caption hover_underline_white">Twitter</div>
          </div>
          <div class="col-lg-2 col-md-2 col-sm-12 col-xs-12 text-white">
            <div class="text-subtitle1 text-weight-bold">Policy</div>
            <div class="text-caption hover_underline_white q-mt-sm">Return Policy</div>
            <div class="text-caption hover_underline_white">Terms Of Use</div>
            <div class="text-caption hover_underline_white">Security</div>
            <div class="text-caption hover_underline_white">Privacy</div>
            <div class="text-caption hover_underline_white">Sitemap</div>
          </div>
          <div class="col-lg-2 col-md-2 col-sm-12 col-xs-12 text-white">
            <div class="text-subtitle1 text-weight-bold">Help</div>
            <div class="text-caption hover_underline_white q-mt-sm">Payments</div>
            <div class="text-caption hover_underline_white">Shipping</div>
            <div class="text-caption hover_underline_white">Cancellation & Returns</div>
            <div class="text-caption hover_underline_white">FAQ</div>
          </div>
          <div
            class="col-lg-3 col-md-3 col-sm-12 col-xs-12 text-white"
            :class="$q.platform.is.desktop ? 'q-pl-xl' : ''"
            :style="$q.platform.is.desktop ? 'border-left: 1px solid grey;' : ''"
          >
            <div class="text-subtitle1 text-weight-bold">Registered Office Address:</div>
            <div class="text-caption q-mt-sm">335, Gokhale Wadi, Grant Road</div>
            <div class="text-caption">Mumbai, Maharashtra</div>
            <div class="text-caption">412207</div>
            <div class="text-caption">India</div>
          </div>
        </div>
        <div style="background-color: #163758">
          <div class="q-mr-md text-right q-py-xs text-weight-bold text-grey-6" style="">
            Made with
            <span style="color: #e25555; font-size: 16px">&#9829;</span> using
            <a
              target="_blank"
              class="text-blue-1 hover_underline_white"
              style="text-decoration: none"
              href="https://quasar-framework.org"
              >&nbsp;Quasar&nbsp;</a
            >
            by
            <a
              target="_blank"
              class="text-blue-1 hover_underline_white"
              style="text-decoration: none"
              href="https://github.com/mayur091193"
              >Mayur</a
            >.
          </div>
        </div>
      </div>
    </q-page-container>
  </q-layout>
</template>

<script>
export default {
  data() {
    return {
      left: false,
      menu_cat_elc: false,
      menu_cat_tvs: false,
      menu_cat_men: false,
      text: "",
    };
  },
};
</script>

<style>
.q-drawer {
  /*background-image: url(https://demos.creative-tim.com/vue-material-dashboard/img/sidebar-2.32103624.jpg) !important;*/
  background-image: url("/statics/images/lake.jpg") !important;
  background-size: cover !important;
}

.q-drawer__content {
  background-color: rgba(1, 1, 1, 0.75);
}

.navigation-item {
  border-radius: 5px;
}

.tab-active {
  background-color: green;
}

.hover-blue:hover {
  color: #1f509e;
}

.hover_underline_white:hover {
  text-decoration: underline !important;
  cursor: pointer;
}

.hover_border_grey:hover {
  border: 1px solid lightgrey;
  cursor: pointer;
  border-radius: 3px;
}
</style>
