import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import Projects from "../views/Projects.vue";
import Login from "../views/Login.vue";
import Mentors from "../views/Mentors.vue"


const routes = [
  {
    path: "/",

    component: HomeView,
    meta: {
      enterClass: "animate__animated animate__slideInRight animate__faster",
      leaveClass: "animate__animated animate__slideOutLeft animate__faster",
    }
  },
  {
    path: "/projects",

    component: Projects,
    meta: {
      enterClass: "animate__animated animate__slideInRight animate__faster",
      leaveClass: "animate__animated animate__slideOutLeft animate__faster",
    }
  },

  {
    path: "/mentors",

    component: Mentors,
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
  {
    path: "/SignUP",
    name: "SignUP",
    component: () =>
      import("../views/Registration.vue"),

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
