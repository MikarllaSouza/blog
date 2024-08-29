/** @type {import('tailwindcss').Config} */
module.exports = {
    content: [
        './src/**/*.{html,js,jsx,ts,tsx}',  // Inclui todos os arquivos HTML, JS, JSX, TS, TSX na pasta src
        './public/index.html',              // Inclui o arquivo index.html na pasta public
    ],
    theme: {
        extend: {},
    },
    plugins: [],
};
