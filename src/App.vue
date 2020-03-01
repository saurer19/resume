<template>
  <div id="app" class="antialiased text-gray-900">
    <div class="min-h-screen svgBackground min-w-full flex flex-col">
      <div class="relative" :class="{'shadow-md border-b border-gray-900':$route.name!=='home'}">
        <Navbar />
      </div>
      <div class="min-h-full flex flex-col flex-grow" :class="{'bg-gray-200':$route.name!=='home'}">
        <transition name="page" mode="out-in">
          <router-view />
        </transition>
        <div class="flex flex flex-grow"></div>
        <Footer />
      </div>
    </div>
  </div>
</template>
<script>
import Navbar from "./components/Navbar";
import Footer from './components/Footer';
export default {
  scrollToTop: true,
  name: "app",
  components: {
    Footer,
    Navbar
  }
};
</script>
<style src="./assets/tailwind.css"></style>
<style>
.svgBackground {
  background-color: #000000;
  background-image: linear-gradient(147deg, #000000 0%, #2c3e50 74%);
}
.page-enter-active, .page-leave-active {
  transition: opacity .5s, transform .5s;
}
.page-enter, .page-leave-to {
  opacity: 0;
  transform: translateX(-30%);
}

</style>
