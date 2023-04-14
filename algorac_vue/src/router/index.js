import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import Projects from "../views/Projects.vue";
import Login from "../views/Login.vue";
import Mentors from "../views/Mentors.vue"


const routes = [
  {
    path: "/",
    name: "home",
    component: HomeView,
    meta: {
      enterClass: "animate__animated animate__slideInRight animate__fast",
      leaveClass: "animate__animated animate__slideOutLeft animate__fast",
    }
  },
  {
    path: "/projects",
    name: "projects",
    component: Projects,
    meta: {
      enterClass: "animate__animated animate__slideInRight animate__faster",
      leaveClass: "animate__animated animate__slideOutLeft animate__faster",
    }
  },

  {
    path: "/mentors",
    name: "Mentors",
    component: () =>
      import("../views/Mentors.vue"),
    meta: {
      enterClass: "animate__animated animate__slideInRight animate__faster",
      leaveClass: "animate__animated animate__slideOutLeft animate__faster",
    }

  },
  {
    path: "/login",
    name: "Login",
    component: () =>
      import("../views/Login.vue"),

    meta: {
      enterClass: "animate__animated animate__backInUp animate__faster",
      leaveClass: "animate__animated animate__slideOutLeft animate__faster",
    }

  },

];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
