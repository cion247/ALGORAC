<template>
  <div
    class="text-xl font-semibold w-full h-full bg-one bg-fixed bg-cover bg-bottom p-2"
  >
    <div class="container mx-auto text-left text-white">
      <div class="flex items-center">
        <div class="w-1/2">
          <h1 class="sm:text-4xl text-4xl font-medium mb-6">ABOUT US</h1>
          <p class="mb-12">
            ALGORAC Coding Club is an ingrain part of ICFAI University
            Tripura(IUT), a private university located at Agartala, Tripura,
            India.
            <br />
            ALGORAC is a dynamic and passionate community of tech enthusiasts, driven by a shared love 
            for coding and technology. It provides an inclusive space for students of all skill levels to
            explore, learn, and collaborate on coding projects.
            <br/>
            Through workshops, hackathons, and engaging activities, ALGORAC aims to foster a supportive environment 
            that nurtures creativity and innovation. As it embraces the ever-evolving world of programming, 
            the coding club strives to equip members with valuable skills, preparing them for exciting careers in the tech industry.
            Let's learn, network, and shape the future of technology together!          
          </p>
          <a
            class="bg-white bg-opacity-10 py-4 px-12 rounded-full hover:bg-white-600 backdrop-blur-lg"
            ><i>"ALGORAC believes in coding the problems away."</i></a
          >
        </div>
        <div class="w-1/2 px-2">
          <div
            class="shadow-2xl border-1 mx-auto my-20 border border-transparent rounded backdrop-blur-lg"
          >
            <div class="p-5 space-y-5 shadow-xl">
              <h4 class="text-center sm:text-2xl text-2xl">contact us</h4>

              <form @submit.prevent="submits" class="text-xl font-semibold">
                <div class="grid grid-cols-2 gap-2">
                  <label class="px-3">name</label>
                  <input
                    type="text"
                    class="border border-transparent rounded bg-neutral-800 bg-opacity-25 px-4 py-2 focus:outline-none focus:border-gray-500 col-span-2"
                    required
                    v-model="name"
                  />
                  <label class="px-3">email</label>
                  <input
                    type="email"
                    class="border border-transparent rounded bg-neutral-800 bg-opacity-25 px-4 py-2 focus:outline-none focus:border-gray-500 col-span-2"
                    required
                    v-model="email"
                  />
                  <label class="px-3">message</label>
                  <textarea
                    cols="10"
                    rows="5"
                    class="border border-transparent rounded bg-neutral-800 bg-opacity-25 px-4 py-2 focus:outline-none focus:border-gray-500 col-span-2"
                    required
                    v-model="message"
                  ></textarea>
                </div>
                <input
                  type="submit"
                  value="Send Message"
                  class="cursor-pointer focus:outline-none mt-5 bg-white bg-opacity-5 px-4 py-2 font-bold w-full"
                />
              </form>
              <!-- <p>emil: {{ email }}</p> -->
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
      
<script>
import axios from "axios";

export default {
  name: "AboutUs",
  data() {
    return {
      email: "",
      name: "",
      message: "",
    };
  },
  components: {},

  methods: {
    async submits() {
      const messageData = {
        name: this.name,
        email: this.email,
        description: this.message,
      };

      try {
        const response = await axios.post(
          "https://algoracbackend.onrender.com/api/v1/messages/",
          messageData
        );
        console.log(response);
        this.email = "";
        this.name = "";
        this.message = "";
      } catch (error) {
        console.error(error);
      }
    },
  },
};
</script>

      

      