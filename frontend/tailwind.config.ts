import type { Config } from "tailwindcss";

const config: Config = {
  content: [
    "./pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./components/**/*.{js,ts,jsx,tsx,mdx}",
    "./app/**/*.{js,ts,jsx,tsx,mdx}",
  ],

  // theme: {
  //   extend: {
  //     // backgroundImage: {
  //     //   "gradient-radial": "radial-gradient(var(--tw-gradient-stops))",
  //     //   "gradient-conic":
  //     //     "conic-gradient(from 180deg at 50% 50%, var(--tw-gradient-stops))",
  //     // },
  //   },
  // },
 
  daisyui: {
   themes: [
     "light", "dark", "cupcake",
      {
        mytheme: {
          "primary": "#a991f7",
          "secondary": "#f6d860",
          "accent": "#37cdbe",
          "neutral": "#3d4451",
          "base-100": "oklch(25.3267% .015896 252.417568 /1)",

          "--rounded-box": "1rem", // border radius rounded-box utility class, used in card and other large boxes
          "--rounded-btn": "0.5rem", // border radius rounded-btn utility class, used in buttons and similar element
          "--rounded-badge": "1.9rem", // border radius rounded-badge utility class, used in badges and similar
          "--animation-btn": "0.25s", // duration of animation when you click on button
          "--animation-input": "0.2s", // duration of animation for inputs like checkbox, toggle, radio, etc
          "--btn-focus-scale": "0.95", // scale transform of button when you focus on it
          "--border-btn": "1px", // border width of buttons
          "--tab-border": "1px", // border width of tabs
          "--tab-radius": "0.5rem", // border radius of tabs
        },
      },
     
    ],
    themeRoot: ":root",
  },
  plugins: [
    require('daisyui'),
    
  ],

};
export default config;
