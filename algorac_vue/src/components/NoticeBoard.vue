<template>
  <div class="hello">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h2 class="is-size-2 has-text-centered">the notice board</h2>
      </div>

      <div
        class="column is-3"
        v-for="notice in this.latestNotices"
        v-bind:key="notice.id"
      >
        <div class="box">
          <h3 class="is-size-4">{{ notice.topic }}</h3>
          <h1 class="is-size-4">{{ notice.description }}</h1>

          notice details
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
  
<style scoped lang="scss">
.hello {
  background-color: #ffe28a;
  height: 400px;
  width: 50%;
  padding: 10px;

  display: inline-block;
  color: black;
}
h3 {
  margin: 40px 0 0;
}

a {
  color: #42b983;
}
</style>
  