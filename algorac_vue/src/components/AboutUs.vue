<template>
  <div
    class="container shadow-2xl border-6 rounded-lg mx-auto my-20 w-1/3 border border-orange-500 bg-white"
  >
    <div class="p-5 space-y-5 shadow-xl">
      <h4 class="font-serif text-center text-3xl">Send Queries</h4>

      <form>
        <div class="grid grid-cols-2 gap-5">
          <input
            type="text"
            class="border border-gray-500 px-4 py-2 focus:outline-none focus:border-purple-500 col-span-2"
            placeholder="Full Name"
          />
          <input
            type="email"
            class="border border-gray-500 px-4 py-2 focus:outline-none focus:border-purple-500 col-span-2"
            placeholder="Email"
          />
          <textarea
            cols="10"
            rows="5"
            class="border border-gray-500 px-4 py-2 focus:outline-none focus:border-purple-500 col-span-2"
            placeholder="Write your message..."
          ></textarea>
          <div class="mt-15">
            <input type="checkbox" class="border border-gray-400" />
            <span>
              I accept the
              <a href="#" class="text-green-500 font-semibold">Term of Use</a>
              &
              <a href="#" class="text-green-500 font-semibold"
                >Private Policy</a
              ></span
            >
          </div>
        </div>
        <input
          type="submit"
          value="Send Message"
          class="cursor-pointer focus:outline-none mt-5 bg-orange-500 px-4 py-2 text-white font-bold w-full"
        />
      </form>
    </div>
  </div>
</template>
      
<script>
export default {
  name: "AboutUs",
  data() {},
  components: {},
};
</script>
      

      