/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./public/**/*.html', './src/**/*.{vue,js,ts,jsx,tsx}'],
  theme: {
    extend: {
      backgroundImage: {
        'big-bg': "url('./src/assets/notice_board.svg')",
      },
    },
    plugins: [],
  }
}
