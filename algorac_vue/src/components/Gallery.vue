 
<template>
  <div
    class="container mx-auto flex p-5 items-center border rounded-full h-fill"
  >
    <swiper
      :spaceBetween="30"
      :centeredSlides="true"
      slides-per-view="1"
      :autoplay="{
        delay: 2000,
        disableOnInteraction: false,
        pauseOnMouseEnter: true,
      }"
      :pagination="{
        clickable: true,
      }"
      :navigation="true"
      :modules="modules"
      class="mySwiper"
      loop="true"
    >
      <swiper-slide v-for="images in this.latestGallery" v-bind:key="images.id">
        <p class="absolute bottom-20">{{ images.topic }}</p>
        <p class="absolute bottom-10">
          http://127.0.0.1:8000{{ images.image }}
        </p>
        <img
          class="object-cover w-full holo rounded-3xl"
          v-bind:src="'http://127.0.0.1:8000' + images.image"
          alt="image slider"
        />
      </swiper-slide>
      <swiper-slide>
        <p class="absolute bottom-20">sdffsffdfsdfsdfsdfsdfsfsd</p>
        <img
          class="object-cover w-full holo rounded-3xl"
          src="../assets/prj_1.svg"
          alt="image slide 1"
        />
      </swiper-slide>

      <swiper-slide>
        <p class="absolute bottom-20">sdffsffdfsdfsdfsdfsdfsfsd</p>
        <img
          class="object-cover w-full holo rounded-3xl"
          src="../assets/prj_2.svg"
          alt="image slide 2"
        />
      </swiper-slide>
    </swiper>
  </div>
</template>
<script>
import { Swiper, SwiperSlide } from "swiper/vue";

import "swiper/css";
import "swiper/css/pagination";
import "swiper/css/navigation";

import { Autoplay, Pagination, Navigation } from "swiper";
import axios from "axios";

export default {
  name: "Gallery",
  data() {
    return {
      latestGallery: [],
    };
  },
  components: {
    Swiper,
    SwiperSlide,
  },
  setup() {
    return {
      modules: [Autoplay, Pagination, Navigation],
    };
  },
  mounted() {
    this.getLatestGallery();
  },

  methods: {
    getLatestGallery() {
      axios
        .get("api/v1/gallery-latest/")
        .then((response) => {
          this.latestGallery = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>
<style scoped>
.holo {
  height: 20rem;
}
@media (min-width: 1024px) {
  .holo {
    height: 35rem;
  }
}
</style> 