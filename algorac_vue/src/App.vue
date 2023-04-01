<template>
  <div id="wrapper">
    <section class="section">
      <router-view />
    </section>
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
.footer {
  background-color: #25250e;
  height: 10px;
}
</style>
