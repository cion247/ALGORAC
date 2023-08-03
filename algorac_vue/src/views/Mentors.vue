<template>
  <section class="w-full h-full text-white">
    <div class="text-center pb-6">
      <h2 class="text-base font-bold text-indigo-50">|| OUR MENTORS IN ||</h2>
      <div>
        <h1 class="font-bold text-3xl md:text-4xl lg:text-5xl font-heading">
          <strong class=""> ALGORAC </strong>
        </h1>
      </div>
      <p class="mb-8 text-xl font-semibold">
        mentors are available for any help or guidance a student may require
        <br />
        strudents can reach out to mentors without prior introduction
      </p>
    </div>

    <div
      class="container mx-auto grid grid-cols-1 sm:grid-cols-2 md:grid-cols-2 lg:grid-cols-3 gap-3"
    >
      <div
        class="m-12 mx-auto w-full"
        v-for="ment in this.latestMentors"
        v-bind:key="ment.id"
      >
        <div
          class="w-full card mx-auto overflow-hidden bg-white bg-opacity-10 backdrop-blur rounded-lg p-12 flex max-w-md flex-col justify-center items-center"
        >
          <div class="mb-4">
            <img
              class="object-center object-cover rounded-full h-36 w-36"
              v-bind:src="'http://127.0.0.1:8000' + ment.image"
              alt="photo"
            />
          </div>
          <div class="text-center">
            <p class="text-xl text-gray-300 font-bold mb-2">{{ ment.name }}</p>
            <h3>{{ ment.description }}</h3>

            <p class="text-base text-black-400 font-normal">
              <span class="ph1"
                ><a
                  link
                  rel="stylesheet"
                  href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css"
                  integrity="sha512-9usAa10IRO0HhonpyAIVpjrylPvoDwiPUiKdWk5t3PyolY1cOd4DSE0Ga+ri4AuTroPR5aQvXU9xC6qOPnzFeg=="
                  crossorigin="anonymous"
                  referrerpolicy="no-referrer" />
                <i class="fa-solid fa-square-phone"></i
              ></span>
              {{ ment.email }}
            </p>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import axios from "axios";
export default {
  name: "Mentors",
  data() {
    return {
      latestMentors: [],
    };
  },
  components: {},
  mounted() {
    this.getLatestMentors();
  },
  methods: {
    getLatestMentors() {
      axios
        .get("/api/v1/mentor/")
        .then((response) => {
          this.latestMentors = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>
<style>
.card {
  box-shadow: 5px 5px 20px gray;
  transition: 0.9s;
}
/* .card:hover {
  cursor: pointer;
  transform: scale(1.1);
} */
.ph1 {
  color: gray;
}
.ph1:hover {
  color: white;
}
</style>