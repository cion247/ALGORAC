<template>
  <section class="text-gray-50 body-font w-full h-full">
    <div class="container mx-auto flex p-5 md:flex-row flex-col items-center">
      <div
        class="lg:flex-grow md:w-1/2 lg:pr-24 md:pr-16 flex flex-col md:items-start md:text-left mb-16 md:mb-0 items-center text-center"
      >
        <img
          class="h-52 py-4 mx-auto md:h-64 lg:h-72 lg:mx-0"
          src="../assets/ICFAIlogo.png"
          alt="icfai_logo"
        />
        <h1
          class="title-font sm:text-4xl text-8xl mb-4 font-medium text-red-50"
        >
          ALGORAC <br class="hidden lg:inline-block" />coding club
        </h1>
        <p class="mb-8 leading-relaxed text-xl font-semibold">
          welcome to the algorac coding club <br />where we give you hope for a
          better future
        </p>
      </div>
      <NoticeBoard />
    </div>
    <Gallery />
    <AboutUs />
  </section>
</template>

<script >
import NoticeBoard from "@/components/NoticeBoard.vue";
import Gallery from "@/components/Gallery.vue";
import AboutUs from "@/components/AboutUs.vue";

export default {
  name: "Home",
  data() {
    return {};
  },
  components: {
    NoticeBoard,
    AboutUs,

    Gallery,
  },

  methods: {},
};
</script>


