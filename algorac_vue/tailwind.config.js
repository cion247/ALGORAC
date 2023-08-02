/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./public/**/*.html', './src/**/*.{vue,js,ts,jsx,tsx}'],
  theme: {

    extend: {
      backgroundImage: {
        'one': "url('/src/assets/bgpic_bw.svg')"
      }

    },

  }
}

