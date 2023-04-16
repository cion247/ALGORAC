<template>
  <section class="w-full h-full text-white">
    <div class="text-center pb-6">
      <h2 class="text-base font-bold text-indigo-50">|| OUR MENTORS IN ||</h2>
      <div>
        <h1 class="font-bold text-3xl md:text-4xl lg:text-5xl font-heading">
          <strong class=""> ALGORAC </strong>
        </h1>
      </div>
      <img src="../assets/head.png" class="w-full" />
    </div>

    <div
      class="container mx-auto grid grid-cols-1 sm:grid-cols-2 md:grid-cols-2 lg:grid-cols-3 gap-3"
    >
      <div class="m-12 mx-auto w-full">
        <div
          class="w-full card mx-auto overflow-hidden bg-white bg-opacity-10 backdrop-blur rounded-lg p-12 flex max-w-md flex-col justify-center items-center"
        >
          <div class="mb-4">
            <img
              class="object-center object-cover rounded-full h-36 w-36"
              src="http://2.bp.blogspot.com/_lwBPBFdTaWM/TIeBFJY4EVI/AAAAAAAAAA8/hta0nczcYrk/s1600/canstockphoto1799922+teacher.jpg"
              alt="photo"
            />
          </div>
          <div class="text-center">
            <p class="text-xl text-gray-300 font-bold mb-2">NAME</p>
            <h3>(designation)</h3>

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
              CONTACT
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
<style>
.card {
  box-shadow: 5px 5px 20px gray;
  transition: 0.9s;
}
.card:hover {
  cursor: pointer;
  transform: scale(1.1);
}
.ph1 {
  color: gray;
}
.ph1:hover {
  color: white;
}
</style>