import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import Projects from "../views/Projects.vue";
import Login from "../views/Login.vue";
import Mentors from "../views/Mentors.vue";


const routes = [
  {
    path: "/",
    name: "home",
    component: HomeView,
  },
  {
    path: "/projects",
    name: "projects",
    component: () =>
    import(/* webpackChunkName: "about" */ "../views/Projects.vue"),
  },
  {
    path: "/login",
    name: "Login",
    component: () =>
    import(/* webpackChunkName: "about" */ "../views/Login.vue")

  },
  {
    path: "/mentors",
    name: "Mentors",

    component: () =>
    import(/* webpackChunkName: "about" */ "../views/Mentors.vue"),
  },
  {
    path: "/about",
    name: "about",
    component: () =>
      import("../views/AboutView.vue"),
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
