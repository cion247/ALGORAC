<template>
<div class="max-w-2xl mx-auto">

	<div id="default-carousel" class="relative" data-carousel="static">
        <!-- Slider controls -->
        <button type="button" class="flex absolute top-0 left-0 z-30 justify-center items-center px-4 h-full cursor-pointer group focus:outline-none" data-carousel-prev>
            <span class="inline-flex justify-center items-center w-8 h-8 rounded-full sm:w-10 sm:h-10 bg-white/30 dark:bg-gray-800/30 group-hover:bg-white/50 dark:group-hover:bg-white-800/60 group-focus:ring-4 group-focus:ring-white dark:group-focus:ring-white-800/70 group-focus:outline-none">
                <svg class="w-5 h-5 text-black sm:w-6 sm:h-6 dark:text-white-800" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"></path></svg>
                <span class="hidden">Previous</span>
            </span>
        </button>
        <button type="button" class="flex absolute top-0 right-0 z-30 justify-center items-center px-4 h-full cursor-pointer group focus:outline-none" data-carousel-next>
            <span class="inline-flex justify-center items-center w-8 h-8 rounded-full sm:w-10 sm:h-10 bg-white/30 dark:bg-gray-800/30 group-hover:bg-white/50 dark:group-hover:bg-white-800/60 group-focus:ring-4 group-focus:ring-white dark:group-focus:ring-white-800/70 group-focus:outline-none">
                <svg class="w-5 h-5 text-black sm:w-6 sm:h-6 dark:text-white-800" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"></path></svg>
                <span class="hidden">Next</span>
            </span>
        </button>
    </div>
</div>
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