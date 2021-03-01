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
      path: '/sortie/:nom',
      name: 'sortie',
      component: () => import('../pages/viewSortie.vue')
    },
  ],
});
