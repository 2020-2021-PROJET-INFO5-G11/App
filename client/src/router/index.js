import Vue from 'vue';
import Router from 'vue-router';
import Sorties from '../pages/sorties.vue';

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      name: 'login',
      path: '/',
      component: () => import('../pages/login.vue'),
    },
    {
      path: '/sorties',
      name: 'sorties',
      component: Sorties,
    },
    {
      path: '/accueil',
      name: 'accueil',
      component: () => import('../pages/home.vue'),
    },
    {
      path: '/groupes',
      name: 'groupes',
      component: () => import('../pages/groupes.vue'),
    },
    {      
      path: '/creation-sortie',
      name: 'creation de sortie',
      component: () => import('../pages/creation-sortie.vue'),
    },
    {  
      path: '/sortie/:nom',
      name: 'sortie',
      component: () => import('../pages/viewSortie.vue'),
      meta: {
        reload: true,
      },
    },
  ],
});
