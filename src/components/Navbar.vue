<template>
  <header class="sm:flex text-gray-300 sm:justify-between sm:items-center sm:px-4 sm:py-3">
    <div class="flex items-center justify-between px-4 py-3">
      <router-link to="/" class="text-2xl cursor-pointer">
        Gabriel<span class="text-blue-200 font-semibold">Rivas</span>
      </router-link>
      <div class="sm:hidden">
        <button
          @click="isOpen = !isOpen"
          type="button"
          class="block text-gray-500 hover: focus: focus:outline-none"
        >
          <svg class="h-6 w-6 fill-current" viewBox="0 0 24 24">
            <path
              v-if="isOpen"
              fill-rule="evenodd"
              d="M18.278 16.864a1 1 0 0 1-1.414 1.414l-4.829-4.828-4.828 4.828a1 1 0 0 1-1.414-1.414l4.828-4.829-4.828-4.828a1 1 0 0 1 1.414-1.414l4.829 4.828 4.828-4.828a1 1 0 1 1 1.414 1.414l-4.828 4.829 4.828 4.828z"
            />
            <path
              v-if="!isOpen"
              fill-rule="evenodd"
              d="M4 5h16a1 1 0 0 1 0 2H4a1 1 0 1 1 0-2zm0 6h16a1 1 0 0 1 0 2H4a1 1 0 0 1 0-2zm0 6h16a1 1 0 0 1 0 2H4a1 1 0 0 1 0-2z"
            />
          </svg>
        </button>
      </div>
    </div>
    <nav :class="{'close max-h-0 ': !isOpen}" class="sm:block sm:max-h-full navLinks">
      <div class="px-4 pt-2 pb-4 sm:flex sm:p-0">
        <router-link
          to="/skills"
          @click.native="isOpen=false"
          class="cursor-pointer mt-1 block px-2 py-1 font-semibold rounded hover:bg-gray-800 sm:mt-0 sm:ml-2"
        >Skills</router-link>
        <router-link
          to="/experience"
          @click.native="isOpen=false"
          class="cursor-pointer mt-1 block px-2 py-1 font-semibold rounded hover:bg-gray-800 sm:mt-0 sm:ml-2"
        >Experience</router-link>
        <router-link
          to="/contact"
          @click.native="isOpen=false"
          class="cursor-pointer mt-1 block px-2 py-1 font-semibold rounded hover:bg-gray-800 sm:mt-0 sm:ml-2"
        >Contact</router-link>
      </div>
    </nav>
  </header>
</template>
<script>
export default {
  data() {
    return {
      isOpen: false
    };
  }
};
</script>
<style>
.navLinks.close {
  overflow: hidden;
  transition: max-height 0.15s ease-out;
}
.navLinks {
  max-height: 400px;
  transition: max-height 0.25s ease-in;
}
</style>