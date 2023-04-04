<template>
  <div class="home">
    <NavBar />

    <section>
      <div class="intro">
        <p class="title mb-6">welcome to  ALGORAC</p>
        <p class="subtitle">the ICFAI coding club</p>
      </div>
      <NoticeBoard />
    </section>

    <gallery />
    <AboutUs />
  </div>
</template>

<script >
import NoticeBoard from "@/components/NoticeBoard.vue";
import Gallery from "@/components/Gallery.vue";
import AboutUs from "@/components/AboutUs.vue";
import NavBar from "@/components/NavBar.vue";

export default {
  name: "Home",
  data() {
    return {};
  },
  components: {
    NoticeBoard,
    Gallery,
    AboutUs,
    NavBar,
  },

  methods: {},
};
</script>

<style scoped>
.intro {
  height: 400px;
  display: inline-block;
  width: 50%;
  padding: 10px;
  color: rgb(0, 0, 0);
}
</style>