<template>
  <div
    class="lg:max-w-lg lg:w-full md:w-1/2 w-5/6 bg-slate-200 rounded-lg my-8 h-96 border-4 text-stone-900 p-2 overflow-auto scroll-m-2"
  >
    <h1
      class="title-font sm:text-4xl text-3xl mb-1 font-normal text-stone-900 text-center rounded-xl p-1"
    >
      notice_board
    </h1>

    <div class="flex flex-wrap flex-col">
      <!-- notices -->
      <div
        class="p-1 flex-1 flex"
        v-for="notice in this.latestNotices"
        v-bind:key="notice.id"
      >
        <div class="p-1 rounded-lg flex flex-col text-lg break-words grow">
          <h1 class="font-bold">{{ notice.topic }}</h1>
          <h1>{{ notice.description }}</h1>
          <h1>------------------------------</h1>
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
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>

  