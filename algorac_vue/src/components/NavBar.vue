<template >
  <header
    class="sticky top-0 text-gray-900 z-10 backdrop-blur-none drop-shadow container mx-auto border-transparent border-8 flex flex-row py-5 px-4"
  >
    <div
      class="flex flex-wrap px-5 py-4 flex-row items-center justify-items-center w-32"
    >
      <a href="/" class="flex title-font items-center text-white mb-4 mx-auto">
        <img src="../assets/med.svg" alt="ALGORAC Logo" class="w-12 h-12" />
        <span class="text-4xl pl-4">ALGORAC</span>
      </a>
    </div>
    <div
      class="container bg-slate-200 flex flex-wrap px-5 ml-auto flex-row items-center lg:w-96 rounded-xl w-32"
    >
      <nav
        class="md:ml-auto flex flex-wrap mx-auto items-center text-base justify-center"
      >
        <router-link
          to="/"
          class="mr-3 py-1 text-xl font-semibold border-black hover:border-b-2"
          >Home</router-link
        >
        <router-link
          to="/projects"
          class="mr-3 py-1 text-xl font-semibold border-black hover:border-b-2"
          >projects</router-link
        ><router-link
          to="/mentors"
          class="mr-3 py-1 text-xl font-semibold border-black hover:border-b-2"
          >mentors</router-link
        >
      </nav>
      <!-- <button
        class="inline-flex items-center my-2 bg-gray-100 border-0 py-1 px-3 focus:outline-none hover:bg-gray-200 rounded text-black md:mt-0"
      >
        <a href="/login">Login</a>
        <svg
          fill="none"
          stroke="currentColor"
          stroke-linecap="round"
          stroke-linejoin="round"
          stroke-width="2"
          class="w-4 h-4 ml-1"
          viewBox="0 0 24 24"
        >
          <path d="M5 12h14M12 5l7 7-7 7"></path>
        </svg>
      </button> -->
    </div>
  </header>
</template>
<script>
export default {
  name: "NavBar",
};
</script>
<style scoped>
a.router-link-active {
  border-bottom: 2px solid #000;
}
</style>
    
    