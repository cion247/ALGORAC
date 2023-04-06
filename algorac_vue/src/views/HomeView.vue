<template>
  <div class="home">
    <NavBar />

    <section class="text-gray-600 body-font">
      <div
        class="container mx-auto flex px-10 py-5 md:flex-row flex-col items-center"
      >
        <div
          class="lg:flex-grow md:w-1/2 lg:pr-24 md:pr-16 flex flex-col md:items-start md:text-left mb-16 md:mb-0 items-center text-center"
        >
          <h1
            class="title-font sm:text-4xl text-3xl mb-4 font-medium text-gray-900"
          >
            ALGORAC <br class="hidden lg:inline-block" />coding club
          </h1>
          <p class="mb-8 leading-relaxed">
            welcome to the algorac coding club <br />where we give you hope for
            a better future
          </p>
        </div>
        <NoticeBoard />
      </div>
    </section>

    <gallery />
    <AboutUs />
    <Footer />
  </div>
</template>

<script >
import NoticeBoard from "@/components/NoticeBoard.vue";
import Gallery from "@/components/Gallery.vue";
import AboutUs from "@/components/AboutUs.vue";
import NavBar from "@/components/NavBar.vue";
import Footer from "@/components/Footer.vue";

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
    Footer,
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