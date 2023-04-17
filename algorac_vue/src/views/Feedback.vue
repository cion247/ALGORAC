<template>
    <center>
    <div class="w-1/2 px-2">
      <div
        class="shadow-2xl border-1 mx-auto my-20 border border-white rounded backdrop-blur-lg"
      >
        <div class="p-5 space-y-5 shadow-xl">
          <h4 class="font-serif text-center text-3xl">Feedback</h4>

          <form @submit.prevent="feedback">
            <div class="grid grid-cols-2 gap-2">
              <label class="flex title-font font-medium items-center md:justify-start justify-center text-white-900">name</label>
              <input
                type="text"
                class="border border-transparent rounded bg-neutral-800 bg-opacity-25 px-4 py-2 focus:outline-none focus:border-gray-500 col-span-2"
                required
                v-model="name"
              />
              <label class="flex title-font font-medium items-center md:justify-start justify-center text-white-900">message</label>
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
    </center>
</template>

<script>
 
import axios from "axios";

export default {
data() {
return {
  name: "",
  message: "",
    };
  }
};
</script>