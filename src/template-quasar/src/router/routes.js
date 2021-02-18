const routes = [
  { path: "/", component: () => import("pages/login.vue") },
  {
    path: "/",
    component: () => import("layouts/NavBar.vue"),
    children: [
      {
        name: "home",
        path: "/home",
        component: () => import("pages/home.vue")
      },
      {
        name: "customer_management",
        path: "/customer_management",
        component: () => import("pages/customer_management.vue")
      },
      {
        name: "my_profile",
        path: "/my_profile",
        component: () => import("pages/my_profile.vue")
      },
      {
        name: "sorties",
        path: "/sorties",
        component: () => import("pages/sorties.vue")
      }
    ]
  }
];

// Always leave this as last one
if (process.env.MODE !== "ssr") {
  routes.push({
    path: "*",
    component: () => import("pages/Error404.vue")
  });
}

export default routes;
