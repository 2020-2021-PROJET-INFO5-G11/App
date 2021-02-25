import Vue from 'vue';
import Router from 'vue-router';
import Sorties from '../pages/sorties.vue';
import Home from '../pages/home.vue';
import Inscription from '../pages/inscription.vue';
import routes from './routes';
Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
  // routes: [
  //   {
  //     path: '/sorties',
  //     name: 'sorties',
  //     component: Sorties,
  //   },
  //   {
  //     path: '/home',
  //     name: 'home',
  //     component: Home,
  //   },
  //   {
  //     path: '/inscription',
  //     name: 'inscription',
  //     component: Inscription,
  //   },
  //   {
  //     path: '/accueil',
  //     name: 'accueil',
  //     component: () => import('../pages/home.vue'),
  //   },
  //   {
  //     path: '/groupes',
  //     name: 'groupes',
  //     component: () => import('../pages/groupes.vue'),
  //   },
  //   {
  //     path: '/connexion',
  //     name: 'connexion',
  //     component: () => import('../pages/login.vue'),
  //   },
  // ],
});