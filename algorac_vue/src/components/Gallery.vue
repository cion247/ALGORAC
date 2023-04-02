<template>
  <div class="hello">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h2 class="is-size-2 has-text-centered">sliding gallery</h2>
      </div>

      <div
        class="column is-3"
        v-for="notice in latestEvents"
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
    getLatestevents() {
      axios
        .get("events-latest/")
        .then((response) => {
          this.latestEvents = response.data;
          console.log(this.latestEvents);
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
  background-color: #308349;
  height: 400px;
  width: 100%;
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
    