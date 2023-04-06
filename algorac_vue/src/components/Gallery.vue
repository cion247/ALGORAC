<template>
  <section class="overflow-hidden text-neutral-700">
    <div class="flex flex-col text-center w-full mb-20">
      <h1 class="sm:text-3xl text-2xl font-medium title-font mb-4 text-gray-900">Gallery</h1>
      <p class="lg:w-2/3 mx-auto leading-relaxed text-base">Whatewe done a glims.</p>
    </div>
    <div class="container mx-auto px-5 py-2 lg:px-32 lg:pt-12">
      <div class="-m-1 flex flex-wrap md:-m-2">
        <div class="flex w-1/3 flex-wrap" v-for="event in latestEvents" :key="event.id">
          <div class="w-full p-1 md:p-2">
            <img alt="gallery" class="block h-full w-full rounded-lg object-cover object-center" :src="'http://127.0.0.1:8000' + event.image" />
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import axios from "axios";

export default {
  name: "Gallery",
  data() {
    return {
      latestEvents: [],
    };
  },
  components: {},
  mounted() {
    this.getLatestEvents();
  },
  methods: {
    getLatestEvents() {
      axios
        .get("/api/v1/gallery-latest/", { timeout: 10000 }) // increase timeout to 10000ms
        .then((response) => {
          this.latestEvents = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>

<style scoped>
</style>
