<template>
  <div class="mx-auto px-6 text-center text-white">
    <div class="max-w-xs mx-auto mt-16">
      <img
        class="rounded-lg shadow-xl h-48 sm:h-64 block mx-auto"
        src="/img/gabe-square.png"
        alt="me"
      />
    </div>
    <div class="tracking-wider text-2xl font-mono pt-10">
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
        class="fill-current"
        xmlns="http://www.w3.org/2000/svg"
        viewBox="0 0 24 24"
        width="20"
        height="20"
      >
        <path
          class="heroicon-ui"
          d="M4 4h16a2 2 0 0 1 2 2v12a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V6c0-1.1.9-2 2-2zm16 3.38V6H4v1.38l8 4 8-4zm0 2.24l-7.55 3.77a1 1 0 0 1-.9 0L4 9.62V18h16V9.62z"
        />
      </svg>

      <span class="ml-2">Contact me</span>
    </router-link>
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