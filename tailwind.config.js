/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      fontFamily: {
        rubik: ['Rubik'],
      },
      height: {
        'windvisible': 'calc(100vh - 100px)', // Personaliza la altura según lo deseado
        'mainvisible': 'calc(100vw)',
      },
    },
  },
  plugins: [],

}

