import BootstrapVue from 'bootstrap-vue';
import Vue from 'vue';
import App from './App.vue';
import router from './router';
import store from './store'
import 'bootstrap/dist/css/bootstrap.css';

Vue.use(BootstrapVue);

Vue.config.productionTip = false;

new Vue({
  router,
  store,
  render: (h) => h(App),
  watch:{
    '$route' (to) {
       if(to.currentRoute.meta.reload==true){window.location.reload()}
   }
  }
}).$mount('#app');
