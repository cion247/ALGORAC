<template>
  <div
    class="font-sans w-full h-full bg-one bg-fixed bg-cover bg-bottom text-white"
  >
    <NavBar />
    <router-view v-slot="{ Component, route }">
      <transition
        :enter-active-class="route.meta.enterClass"
        :leave-active-class="route.meta.leaveClass"
        mode="out-in"
        ><component :is="Component"
      /></transition>
    </router-view>
    <Footer />
  </div>
</template>

<script>
import NavBar from "@/components/NavBar.vue";
import Footer from "@/components/Footer.vue";
export default {
  data() {
    return {
      showMobileMenu: false,
    };
  },
  components: {
    NavBar,
    Footer,
  },
};
</script>
<style scoped>
</style>


