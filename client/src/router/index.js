import Vue from 'vue';
import Router from 'vue-router';

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
      component: () => import('../pages/inscription.vue'),
    },
    {
      path: '/sorties',
      name: 'sorties',
      component: () => import('../pages/sorties.vue'),
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
      path: '/modification-sortie/:id',
      name: 'modification de sortie',
      component: () => import('../pages/modification-sortie.vue'),
    },
    {
      path: '/sortie/:id',
      name: 'sortie',
      component: () => import('../pages/viewSortie.vue'),
    },
    {
      path: '/recherche/:search',
      name: 'searchSortie',
      component: () => import('../pages/searchSortie.vue'),
    },
    {
      path: '/profil/:id',
      name: 'profil',
      component: () => import('../pages/myProfile.vue')
    },
    {
      path: '/modifier_profil/:id',
      name: 'modifier_profil',
      component: () => import('../pages/modifier_profil.vue')
    },
    {
      path: '/creation-groupe',
      name: 'creation de groupe',
      component: () => import('../pages/creation-groupe.vue'),
    },
    {
      path: '/modification-groupe/:id',
      name: 'modification de groupe',
      component: () => import('../pages/modification-groupe.vue'),
    },
    {
      path: '/groupe/:id',
      name: 'groupe',
      component: () => import('../pages/viewGroupe.vue'),
    },
  ],
});