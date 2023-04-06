<template>
  <div
    class="lg:max-w-lg lg:w-full md:w-1/2 w-5/6 bg-gray-200 rounded-lg m-8 h-96 border-4 border-gray-900 text-gray-900 p-2 overflow-auto"
  >
    <h1 class="title-font sm:text-4xl text-3xl mb-4 font-medium text-gray-900" align="center">
      Notice Board
    </h1>

    <div class="flex flex-wrap m-2">
      <!-- notices -->
      <div
        class="p-2 xl:w-1/4 md:w-1/2 w-full"
        v-for="notice in this.latestNotices"
        v-bind:key="notice.id"
      >
        <div
          class="h-full p-3 rounded-lg border-2 border-gray-900 flex flex-col relative overflow-hidden"
        >
          <h1>{{ notice.topic }}</h1>
          <h1>{{ notice.description }}</h1>
        </div>
      </div>
    </div>
  </div>
</template>
  
<script>
import axios from "axios";
export default {
  name: "NoticeBoard",
  data() {
    return {
      latestNotices: [],
    };
  },
  components: {},
  mounted() {
    this.getLatestNotices();
  },
  methods: {
    getLatestNotices() {
      axios
        .get("/api/v1/notices-latest/")
        .then((response) => {
          this.latestNotices = response.data;
          console.log(this.latestNotices);
          console.log(this.latestNotices.topic);
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
  