<template>
  <div class="mx-auto px-6 text-center text-white py-16 md:py-64 ">
    <div class="flex flex-col md:flex-row">
<div class="max-w-xs mx-auto md:w-1/2">
      <img
        class="rounded-lg shadow-xl h-48 sm:h-64 block mx-auto"
        src="/img/gabe-square.png"
        alt="me"
      />
    </div>
    <div class=" md:w-1/2 max-w-2xl">
      <div class="tracking-wider text-3xl lg:text-4xl font-mono pt-10 md:pt-0">
        Software
        <span class="font-semibold text-blue-200">Developer</span>
      </div>
      <div>
        <div
          class="leading-normal text-left hyphens-text pt-2"
        >I am passionate about technology and truly enjoy the work in this field. My eagerness to learn and desire to gain experience have led me to engage in a wide variety of roles including hybrid mobile applications, SPA websites, and back-end development.</div>
      </div>
      <router-link
        to="/contact"
        class="inline-flex items-center mt-8 px-8 py-2 bg-gray-800 hover:bg-gray-600 rounded-full max-w-xs cursor-pointer text-xs uppercase tracking-wide"
      >
        <svg
          xmlns="http://www.w3.org/2000/svg"
          class="fill-current"
          viewBox="0 0 24 24"
          width="24"
          height="24"
        >
          <path
            class="heroicon-ui"
            d="M8 7V5c0-1.1.9-2 2-2h4a2 2 0 0 1 2 2v2h4a2 2 0 0 1 2 2v10a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V9c0-1.1.9-2 2-2h4zm8 2H8v10h8V9zm2 0v10h2V9h-2zM6 9H4v10h2V9zm4-2h4V5h-4v2z"
          />
        </svg>

        <span class="ml-2">Contact me</span>
      </router-link>
    </div>
    </div>
    
  </div>
</template>

<script>
// @ is an alias to /src

export default {
  name: "home"
};
</script>
<style>
</style>