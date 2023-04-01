<template>
  <div class="home">
    <header class="text-gray-600 body-font">
      <div
        class="container mx-auto flex flex-wrap p-5 flex-col md:flex-row items-center"
      >
        <a
          class="flex title-font font-medium items-center text-gray-900 mb-4 md:mb-0"
        >
          <span class="ml-3 text-xl">ALGORAC</span>
        </a>
        <nav
          class="md:ml-auto flex flex-wrap items-center text-base justify-center"
        >
          <a class="mr-5 hover:text-gray-900">First Link</a>
          <a class="mr-5 hover:text-gray-900">Second Link</a>
          <a class="mr-5 hover:text-gray-900">Third Link</a>
          <a class="mr-5 hover:text-gray-900">Fourth Link</a>
        </nav>
        <button
          class="inline-flex items-center bg-gray-100 border-0 py-1 px-3 focus:outline-none hover:bg-gray-200 rounded text-base mt-4 md:mt-0"
        >
          Button
          <svg
            fill="none"
            stroke="currentColor"
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            class="w-4 h-4 ml-1"
            viewBox="0 0 24 24"
          >
            <path d="M5 12h14M12 5l7 7-7 7"></path>
          </svg>
        </button>
      </div>
    </header>
    <section>
      <div class="intro">
        <p class="title mb-6">welcome to ALGORAC</p>
        <p class="subtitle">the ICFAI coding club</p>
      </div>
      <NoticeBoard />
    </section>
    <section>
      <gallery></gallery>
    </section>
    <section>
      <AboutUs />
    </section>
  </div>
</template>

<script >
// @ is an alias to /src
import NoticeBoard from "@/components/NoticeBoard.vue";
import Gallery from "@/components/Gallery.vue";
import AboutUs from "@/components/AboutUs.vue";
import axios from "axios";

export default {
  name: "Home",
  data() {
    return {};
  },
  components: {
    NoticeBoard,
    Gallery,
    AboutUs,
  },

  methods: {},
};
</script>

<style scoped>
section {
}
.intro {
  height: 400px;
  display: inline-block;
  width: 50%;
  padding: 10px;
  color: white;
}
</style>