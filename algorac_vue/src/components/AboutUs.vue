<template>
  <div class="hello">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h1 class="is-size-2 has-text-centered"><b>ABOUT US</b></h1>
        <br>

        <body>


        </body>
        <strong className="one">ALGORAC</strong> is an ingrain part of ICFAI UNIVERSITY TRIPURA, a private university
        located at Agartala, Tripura.
        <br>
        It is the perfect platform for all the techies who are diligent about tackling real life problems with the aid of
        programming.
        It focuses on competitive programming, wev dev and other aspects of programming.
        The ALGORAC Frontend part is using HTML, TAILWIND CSS and VUE.JS whereas in Backend we are using PYTHON, SQLITE
        AND DJANGO.
        <br>
        <b><i>ALGORAC believes in coding the problems away.</i></b>

        <div class="container shadow-2xl border-6 rounded-lg mx-auto my-20 w-1/3 border border-orange-500 bg-white ">
          <div class="p-5 space-y-5 shadow-xl">
            <h4 class="font-serif text-center text-3xl">Send Queries</h4>

            <form>
              <div class="grid grid-cols-2 gap-5">
                <input type="text" class="border border-gray-500 px-4 py-2 focus:outline-none focus:border-purple-500"
                  placeholder="First Name" />
                <input type="text" class="border border-gray-500 px-4 py-2 focus:outline-none focus:border-purple-500"
                  placeholder="Last Name" />
                <input type="email"
                  class="border border-gray-500 px-4 py-2 focus:outline-none focus:border-purple-500 col-span-2"
                  placeholder="Email" />
                <textarea cols="10" rows="5"
                  class="border border-gray-500 px-4 py-2 focus:outline-none focus:border-purple-500 col-span-2"
                  placeholder="Write your message..."></textarea>
                <div class="mt-15">
                  <input type="checkbox" class="border border-gray-400">
                  <span> I accept the <a href="#" class="text-green-500 font-semibold">Term of Use</a> & <a href="#"
                      class="text-green-500 font-semibold">Private Policy</a></span>
                </div>
              </div>
              <input type="submit" value="Send Message"
                class="cursor-pointer focus:outline-none mt-5 bg-orange-500 px-4 py-2 text-white font-bold w-full" />
            </form>
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
  data() { },
  components: {},
};
</script>
      
<style scoped lang="scss">
.hello {
  background-color: #d2dfe6;
  height: 850px;
  width: 100%;
  padding: 10px;

  display: inline-block;
  color: black;
}

h3 {
  margin: 40px 0 0;
}

a {
  color: #42b983;
}
</style>
      