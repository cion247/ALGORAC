<template>
  <div
    class="container mx-auto py-4 p-5 space-y-5 sm:py-8 md:py-12 sm:space-y-8 md:space-y-16 page"
  >
    <div class="flex flex-col items-center md:flex-row">
      <div class="items-start justify-center w-full h-full md:w-1/2">
        <div
          class="flex flex-col items-start justify-center h-full space-y-3 transform md:pr-10 lg:pr-16 md:space-y-5"
        >
          <div
            class="bg-cyan-700 flex items-center leading-none rounded-full pt-1.5 pr-3 pb-1.5 pl-2 uppercase"
          >
            <p class="inline text-xs font-medium px-2">Projects</p>
          </div>
          <a class="text-4x1 font-bold leading-none lg:text-5xl xl:text-6xl"
            >Projects handled under ALGORAC.</a
          >
        </div>
      </div>
      <div class="w-full md:w-1/2">
        <div class="block border border-w-2 rounded-full">
          <img class="mx-auto my-2 rounded-lg" src="../assets/prj_1.svg" />
        </div>
      </div>
    </div>
    <div class="grid grid-cols-12 gap-x-8 gap-y-16">
      <div
        class="flex flex-col items-start col-span-12 space-y-3 sm:col-span-6 xl:col-span-4"
        v-for="prj in this.projects"
        :key="prj.id"
      >
        <img
          class="rounded-xl"
          v-bind:src="'http://127.0.0.1:8000' + prj.image"
        />
        <p
          class="bg-cyan-700 flex items-center leading-none text-sm font-medium pt-1.5 pr-3 pb-1.5 pl-3 rounded-full uppercase"
        >
          {{ prj.id }}
        </p>
        <a class="text-lg font-bold sm:text-xl md:text-2xl">{{ prj.title }}</a>
        <p class="text-sm">
          {{ prj.description }}
        </p>
        <div class="pt-2 pr-0 pb-0 pl-0">
          <p class="text-sm font-medium inline">By:</p>
          <a class="inline text-xs font-medium mt-0 mr-1 mb-0 ml-0 underline">{{
            prj.creator
          }}</a>
          <p class="inline text-xs font-medium mt-0 mr-1 mb-0 ml-1">
            · {{ prj.time_added }} ·
          </p>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import axios from "axios";
export default {
  name: "Projects",
  data() {
    return {
      projects: [],
    };
  },
  components: {},
  mounted() {
    this.getLatestProjects();
  },
  methods: {
    getLatestProjects() {
      axios
        .get("api/v1/projects/")
        .then((response) => {
          this.projects = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>
