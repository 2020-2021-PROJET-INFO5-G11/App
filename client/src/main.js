import BootstrapVue from 'bootstrap-vue';
import Vue from 'vue';
import App from './App.vue';
import router from './router';
import 'bootstrap/dist/css/bootstrap.css';
import store from './store';
import axios from 'axios';

Vue.use(BootstrapVue);
axios.defaults.withCredentials = true;
Vue.config.productionTip = false;

router.beforeEach((to, from, next) => {
  if (to.matched.some((record) => record.meta.requiresAuth)) {
    if (store.getters.isAuthenticated) {
      next();
      return;
    }
    next("/login");
  } else {
    next();
  }
});

router.beforeEach((to, from, next) => {
  if (to.matched.some((record) => record.meta.guest)) {
    if (store.getters.isAuthenticated) {
      next("/accueil");
      return;
    }
    next();
  } else {
    next();
  }
});

new Vue({
  store,
  router,
  render: (h) => h(App),
  watch:{
    '$route' (to) {
       if(to.currentRoute.meta.reload==true){window.location.reload()}
   }
  }
}).$mount('#app');
