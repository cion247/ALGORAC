 
<template>
  <div
    class="container mx-auto flex p-5 items-center border rounded-full h-fill"
  >
    <swiper
      :spaceBetween="30"
      :centeredSlides="true"
      slides-per-view="1"
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
      loop="true"
    >
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
      <swiper-slide>
        <p class="absolute bottom-20">sdffsffdfsdfsdfsdfsdfsfsd</p>
        <img
          class="object-cover w-full holo rounded-3xl"
          src="../assets/prj_3.svg"
          alt="image slide 3"
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
      <swiper-slide>
        <p class="absolute bottom-20">sdffsffdfsdfsdfsdfsdfsfsd</p>
        <img
          class="object-cover w-full holo rounded-3xl"
          src="../assets/prj_3.svg"
          alt="image slide 3"
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
  height: 20rem;
}
@media (min-width: 1024px) {
  .holo {
    height: 35rem;
  }
}
</style> 