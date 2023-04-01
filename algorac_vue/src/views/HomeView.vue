<template>
  <div class="home">
    <!-- <img alt="Vue logo" src="../assets/logo.png" />
    <HelloWorld msg="Welcome to Your Vue.js App" /> -->
    <section class="hero is-medium is-dark mb-6">
      <div class="hero-body has-text-centered">
        <p class="title mb-6">
          welcome to ALGORAC
        </p>
        <p class="subtitle">
          the ICFAI coding club
        </p>

      </div>

    </section>
    <div class="columns is-multiline">
      <div class="column is-12">
        <h2 class="is-size-2 has-text-centered ">latest news</h2>
      </div>

      <div class="column is-3" v-for="notice in latestNotices" v-bind:key="notice.id">
        <div class="box">
          <figure class="image mb-4">
            <img v-bind:src="notice.get_image">
          </figure>
          <h3 class="is-size-4">{{ notice.topic }}

          </h3>

          notice details
        </div>
      </div>
    </div>
  </div>
</template>

<script >
// @ is an alias to /src
// import HelloWorld from "@/components/HelloWorld.vue";
import axios from 'axios'

export default {
  name: "Home",
  data() {
    return {
      latestNotices: []
    }
  },
  components: {
  },
  mounted() {
    this.getLatestNotices()
  },
  methods: {
    getLatestNotices() {
      axios
        .get('notices-latest/')
        .then(response => {
          this.latestNotices = response.data;
          console.log(this.latestNotices)
        })
        .catch(error => {
          console.log(error)
        })
    }
  }
};
</script>

<style scoped>
.image {
  margin: -1.25rem
}
</style>