<template>
  <div class="mx-auto xs:px-6 text-center text-white pt-16 md:pt-32">
    <div class="flex flex-col md:flex-row justify-center">
      <div class=" mx-auto md:w-1/2">
        <img
          class="rounded-lg shadow-xl h-48 sm:h-64 block mx-auto"
          src="/img/gabe-square.png"
          alt="me"
        />
      </div>
      <div class="md:w-1/2 max-w-2xl">
        <div class="tracking-wider text-3xl lg:text-4xl font-mono pt-10 md:pt-0">
          Software<span class="font-semibold text-blue-200">Developer</span>
        </div>
        <div>
          <div
            class="leading-normal text-center hyphens-text pt-2 px-3 md:text-left md:px-0"
          >I am passionate about technology and truly enjoy the work in this field. My eagerness to learn and desire to gain experience have led me to engage in a wide variety of roles including hybrid mobile applications, SPA web apps, and back-end development.</div>
        </div>
        <router-link
          to="/contact"
          class="invisible sm:visible inline-flex items-center mt-8 px-8 py-2 bg-gray-800 hover:bg-gray-600 rounded-full max-w-xs cursor-pointer text-xs uppercase tracking-wide"
        >
          <span class="mr-2">Contact me</span>
          <svg class="fill-current" style="width:24px;height:24px" viewBox="0 0 24 24">
            <path
              d="M17,12V3A1,1 0 0,0 16,2H3A1,1 0 0,0 2,3V17L6,13H16A1,1 0 0,0 17,12M21,6H19V15H6V17A1,1 0 0,0 7,18H18L22,22V7A1,1 0 0,0 21,6Z"
            />
          </svg>
        </router-link>
      </div>
      <div class="flex  sm:hidden">
        <router-link
          to="/skills"
          class=" mx-auto text-center font-bold py-2 px-4 rounded flex items-center bg-blue-500 hover:bg-blue-700 text-gray-100 px-4 border-b-4 border-blue-800 shadow-md"
        >
          <span class="pr-3 tracking-wider font-mono">Skills</span>
          <svg class="fill-current" style="width:24px;height:24px" viewBox="0 0 24 24">
            <path  d="M4,11V13H16L10.5,18.5L11.92,19.92L19.84,12L11.92,4.08L10.5,5.5L16,11H4Z" />
          </svg>
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
