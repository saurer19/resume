<template>
  <header class="sm:flex text-gray-300 sm:justify-between sm:items-center sm:px-4 sm:py-3">
    <div class="flex items-center justify-between px-4 py-3">
      <router-link to="/" class="text-2xl cursor-pointer pl-2 md:pl-4" @click.native="isOpen=false">
        Gabriel<span class="text-blue-200 font-semibold">Rivas</span>
      </router-link>
      <div class="sm:hidden">
        <button
          @click="isOpen = !isOpen"
          aria-label="Navigate"
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
          v-for="route in routes"
          :key="route.path"
          :to="route.path"
          v-slot="{ navigate, isActive }"
          @click.native="isOpen=false"
          class="cursor-pointer mt-1 block px-2 py-1 tracking-wide rounded hover:bg-gray-800 sm:mt-0 sm:ml-2"
        >
          <div
            :class="isActive ?'text-blue-200 font-black':'text-gray-400 font-normal'"
            @click="navigate"
          >{{route.name}}</div>
        </router-link>
      </div>
    </nav>
  </header>
</template>
<script>
export default {
  data() {
    return {
      isOpen: false,
      routes: [
        {
          path: "/skills",
          name: "Skills"
        },
        {
          path: "/experience",
          name: "Experience"
        },
        {
          path: "/contact",
          name: "Contact"
        }
      ]
    };
  },
  computed: {
    currentRouteName() {
      return this.$route.name;
    }
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