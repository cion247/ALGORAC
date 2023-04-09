<template>
  <div class="font-mono w-full h-full bg-one bg-fixed bg-cover bg-center">
    <div class="container mx-auto text-left text-white">
      <div class="flex items-center">
        <div class="w-1/2">
          <h1 class="text-5xl font-medium mb-6">ABOUT US</h1>
          <p class="text-xl mb-12">
            <strong>ALGORAC</strong> Coding Club is an ingrain part of ICFAI
            UNIVERSITY TRIPURA(IUT), a private university located at Agartala,
            Tripura, India.
            <br />
            ALGORAC is the perfect platform for all techies who are inquisitive
            and diligent about tackling real life problem with the aid of
            programming. The club focuses on
            <i>
              <b className="purple">
                Competitive programming, Web Dev, App Dev,
              </b>
            </i>
            and various other aspects of programming.
            <br />
            <strong>ALGORAC </strong>strives to inculcate and foster the culture
            of programming and to create a healthy programming environment in
            the campus. It aims to create an environment which proliferate
            quantity and quality of programmers irrespective of their respective
            engineering discipline.
            <br>
            <br>
            <strong><i>"ALGORAC believes in coding the problems away."</i></strong>
          </p>
        </div>
        <div class="w-1/2 px-2">
          <div
            class="shadow-2xl border-1 mx-auto my-20 border rounded-lg backdrop-blur-lg"
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
                      <a href="#" class="text-green-500 font-semibold"
                        >Term of Use</a
                      >
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
        </div>
      </div>
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
      

      