import Vue from 'vue';
import Router from 'vue-router';
import Sorties from '../pages/sorties.vue';
import Inscription from '../pages/inscription.vue';

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
     path: '/connexion',
     name: 'connexion',
     component: () => import('../pages/login.vue'),
    },
    {
     path: '/inscription',
     name: 'inscription',
    component: Inscription,
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
      path: '/sortie/:id',
      name: 'viewSortie',
      component: () => import('../pages/viewSortie.vue'),
    },
    {
      path: '/recherche/:search',
      name: 'searchSortie',
      component: () => import('../pages/searchSortie.vue'),
    },
  ],
});
