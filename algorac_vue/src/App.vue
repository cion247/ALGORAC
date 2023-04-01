<template>
  <div id="wrapper">
    <nav class="navbar">
      <div class="navbar-brand">
        <router-link to="/" class="navbar-item">
          <strong>ALGORAC</strong>
        </router-link>
        <a
          class="navbar-burger"
          aria-label="menu"
          aria-expanded="false"
          data-target="navbar-menu"
          @click="showMobileMenu = !showMobileMenu"
        >
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
        </a>
      </div>
      <div
        class="navbar-menu"
        id="navbar-menu"
        :class="{ 'is-active': showMobileMenu }"
      >
        <div class="navbar-end">
          <router-link to="/projects" class="navbar-item">Projects</router-link>
          <router-link to="/mentors" class="navbar-item">Mentors</router-link>

          <div class="navbar-item">
            <div class="buttons">
              <router-link to="/log-in" class="button is-light">
                Log in
              </router-link>
            </div>
          </div>
        </div>
      </div>
    </nav>

    <section class="section">
      <router-view />
    </section>
    <footer class="footer is-dark">
      <p class="has-text-centered">Copyright (c) 2023</p>
    </footer>
  </div>
</template>

<script>
export default {
  data() {
    return {
      showMobileMenu: false,
    };
  },
};
</script>

<style lang="scss">
//@import "../node_modules/bulma";
.footer {
  background-color: #25250e;
  height: 10px;
}
</style>
