/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./app/templates/**/*.html"],
  theme: {
    extend: {
      fontFamily: {
        source: ['"Sans"', "sans-serif"],
      }
    },
  },
  plugins: [],
}

