import Vue from 'vue';
import Router from 'vue-router';
import Sorties from '../pages/sorties.vue';

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/sorties',
      name: 'sorties',
      component: Sorties,
    },
  ],
});
