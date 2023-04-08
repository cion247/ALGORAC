<template >
  <header
    class="sticky top-0 text-gray-900 z-10 drop-shadow-lg container mx-auto border-transparent border-8 flex flex-row p-3"
  >
    <div
      class="flex flex-wrap p-5 flex-row items-center justify-items-center w-32 rounded-lg"
    >
      <a href="/" class="flex title-font items-center text-white mb-4 mx-auto">
        <span class="text-4xl font-black">ALGORAC</span>
      </a>
    </div>
    <div
      class="container bg-slate-200 backdrop-blur-xl flex flex-wrap p-5 ml-auto flex-row items-center w-1/5 lg:w-96 rounded-lg"
    >
      <nav
        class="md:ml-auto flex flex-wrap place-items-start text-xl font-bold justify-start"
      >
        <a href="/about" class="m-2 hover:underline underline-offset-8"
          >about</a
        >
        <a class="m-2 hover:underline underline-offset-8">Projects</a>
        <a class="m-2 hover:underline underline-offset-8">Mentors</a>
      </nav>
      <button
        class="inline-flex items-center bg-gray-100 text-gray-900 py-1 px-3 focus:outline-none hover:bg-gray-200 rounded font-bold mt-4 md:mt-0"
      >
        Login
      </button>
    </div>
  </header>
</template>
<script>
export default {
  name: "NavBar",
};
</script>
    
    