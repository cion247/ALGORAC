<template>
  <div class="hello">
    <h1>HOLI SHIT</h1>
    <div class="columns is-multiline">
      <div class="column is-12">
        <h2 class="is-size-2 has-text-centered">latest news</h2>
      </div>

      <div
        class="column is-3"
        v-for="notice in latestNotices"
        v-bind:key="notice.id"
      >
        <div class="box">
          <figure class="image mb-4">
            <img v-bind:src="notice.get_image" />
          </figure>
          <h3 class="is-size-4">{{ notice.topic }}</h3>

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
        .get("notices-latest/")
        .then((response) => {
          this.latestNotices = response.data;
          console.log(this.latestNotices);
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>
  
  <!-- Add "scoped" attribute to limit CSS to this component only -->
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
  