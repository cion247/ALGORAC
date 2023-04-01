<template>
  <div class="home">
    <!-- <img alt="Vue logo" src="../assets/logo.png" />
    <HelloWorld msg="Welcome to Your Vue.js App" /> -->
    <section>
      <div class="intro">
        <p class="title mb-6">welcome to ALGORAC</p>
        <p class="subtitle">the ICFAI coding club</p>
      </div>
      <NoticeBoard />
    </section>
  </div>
</template>

<script >
// @ is an alias to /src
import NoticeBoard from "@/components/NoticeBoard.vue";
import axios from "axios";

export default {
  name: "Home",
  data() {
    return {};
  },
  components: {
    NoticeBoard,
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