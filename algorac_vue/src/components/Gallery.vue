
<template>
  <div
    class="container mx-auto flex p-5 items-center border rounded-full h-fill"
  >
    <swiper
      :spaceBetween="30"
      :centeredSlides="true"
      :autoplay="{
        delay: 2500,
        disableOnInteraction: false,
      }"
      :pagination="{
        clickable: true,
      }"
      :navigation="true"
      :modules="modules"
      class="mySwiper"
    >
      <swiper-slide>
        <img
          className="object-cover w-full  holo rounded-3xl"
          src="../assets/prj_1.svg"
          alt="image slide 1"
        />
      </swiper-slide>
      <swiper-slide>
        <img
          className="object-cover w-full holo rounded-3xl"
          src="../assets/prj_2.svg"
          alt="image slide 2"
        />
      </swiper-slide>
      <swiper-slide>
        <img
          className="object-cover w-full holo rounded-3xl"
          src="../assets/prj_3.svg"
          alt="image slide 3"
        />
      </swiper-slide>
    </swiper>
  </div>
</template>
<script>
// Import Swiper Vue.js components
import { Swiper, SwiperSlide } from "swiper/vue";

// Import Swiper styles
import "swiper/css";

import "swiper/css/pagination";
import "swiper/css/navigation";

// import required modules
import { Autoplay, Pagination, Navigation } from "swiper";

export default {
  components: {
    Swiper,
    SwiperSlide,
  },
  setup() {
    return {
      modules: [Autoplay, Pagination, Navigation],
    };
  },
};
</script>
<style scoped>
.holo {
  height: 35rem;
}
</style>