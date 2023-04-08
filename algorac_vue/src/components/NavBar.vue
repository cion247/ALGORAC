<template >
  <header
    class="sticky top-0 text-gray-900 z-10 backdrop-blur-none drop-shadow container mx-auto border-transparent border-8 flex flex-row p-3"
  >
    <div
      class="flex flex-wrap p-5 flex-row items-center justify-items-center w-32 rounded-lg"
    >
      <a href="/" class="flex title-font items-center text-white mb-4 mx-auto">
        <span class="text-4xl font-black">ALGORAC</span>
      </a>
    </div>
    <div
      class="container bg-slate-200 flex flex-wrap p-5 ml-auto flex-row items-center w-1/5 lg:w-96 rounded-lg"
    >
      <nav
        class="md:ml-auto flex flex-wrap place-items-start text-xl font-bold justify-start"
      >
        <a href="/about" class="mr-5 hover:text-gray-900"> About </a>
      </nav>
      <nav
        class="md:ml-auto flex flex-wrap items-center text-base justify-center"
      >
        <a href="/projects" class="mr-5 hover:text-gray-900">Projects</a>
        <a href="/mentors" class="mr-5 hover:text-gray-900">Mentors</a>
      </nav>
      <button
        class="inline-flex items-center bg-gray-100 border-0 py-1 px-3 focus:outline-none hover:bg-gray-200 rounded text-black mt-4 md:mt-0"
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
      </button>
    </div>
  </header>
</template>
<script>
export default {
  name: "NavBar",
};
</script>
    
    