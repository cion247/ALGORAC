<template>
  <div class="hello"></div>
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
<style scoped >


</style>
    