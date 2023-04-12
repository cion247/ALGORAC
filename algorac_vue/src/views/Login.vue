<template>
    <div class="container shadow-2xl border-6 rounded-lg mx-auto my-20 w-1/3 border border-gray-950 bg-white flex min-h-full items-center justify-center px-4 py-12 sm:px-6 lg:px-8">
      <div class="w-full max-w-md space-y-8">
        <div>
          <h2 class="mt-6 text-center text-3xl font-bold tracking-tight text-gray-900">Login to ALGORAC</h2>
        </div>
        <form class="mt-8 space-y-6" action="#" method="POST">
          <input type="hidden" name="remember" value="true">
          <div class="-space-y-px rounded-md shadow-sm">
            <div>
              <label for="username" class="sr-only">username</label>
              <input id="username" name="name" type="name" autocomplete="name" required class="relative block w-full rounded-t-md border-0 py-1.5 text-gray-900 ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:z-10 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" placeholder="username">
            </div>
            <div>
              <label for="password" class="sr-only">Password</label>
              <input id="password" name="password" type="password" autocomplete="current-password" required class="relative block w-full rounded-b-md border-0 py-1.5 text-gray-900 ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:z-10 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" placeholder="Password">
            </div>
          </div>
    
          <div class="flex items-center justify-between">
            <div class="flex items-center">
              <input id="remember-me" name="remember-me" type="checkbox" class="h-4 w-4 rounded border-gray-300 text-indigo-600 focus:ring-indigo-600">
              <label for="remember-me" class="ml-2 block text-sm text-gray-900">Remember me</label>
            </div>
    
            <div class="text-sm">
              <a href="#" class="font-medium text-gray-950 hover:text-gray-950">Forgot your password?</a>
            </div>
          </div>
    
          <div>
            <button type="submit" class="group relative flex w-full justify-center rounded-md bg-gray-950 px-3 py-2 text-sm font-semibold text-white hover:bg-gray-950 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-gray-500">
              <span class="absolute inset-y-0 left-0 flex items-center pl-3">
                <svg class="h-5 w-5 text-white-500 group-hover:text-gray-400" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true">
                  <path fill-rule="evenodd" d="M10 1a4.5 4.5 0 00-4.5 4.5V9H5a2 2 0 00-2 2v6a2 2 0 002 2h10a2 2 0 002-2v-6a2 2 0 00-2-2h-.5V5.5A4.5 4.5 0 0010 1zm3 8V5.5a3 3 0 10-6 0V9h6z" clip-rule="evenodd" />
                </svg>
              </span>
              Sign in
            </button>
          </div>
        </form>
      </div>
    </div>
    </template>

<script>
import axios from 'axios';

export default {
  name: 'Login',
  data() {
    return {
      username: '',
      password: '',
      rememberMe: false,
      errorMessage: '',
    };
  },
  methods: {
    async login() {
      try {
        const response = await axios.post(`http://127.0.0.1:8000/api/v1/token/`, {
          username: this.username,
          password: this.password,
        });

        // Save token to local storage
        localStorage.setItem('accessToken', response.data.access);
        localStorage.setItem('refreshToken', response.data.refresh);

        // Redirect to dashboard
        this.$router.push('/');
      } catch (error) {
        this.errorMessage = error.response.data.detail;
      }
    },
  },
};
</script>
    