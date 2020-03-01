<template>
  <div class="flex-1 h-full py-8 px-6 justify-center text-gray-800">
    <div class="max-w-6xl mx-auto py-8">
      <div class="lg:mx-12 text-5xl text-blue-700 font-normal">Experience</div>
      <transition-group appear tag="div" class="skill" name="animation">
        <div
          class="lg:mx-12 mt-6 sm:mt-12 bg-job rounded overflow-hidden shadow-lg md:flex"
          v-for="job in jobs"
          v-bind:key="job.title"
        >
          <div class="md:w-1/2 md:pt-16 md:pr-0 md:pl-12">
            <a
              class="block relative padding-image-sm md:padding-image-lg"
              :href="job.link"
            >
              <img
                class="inset-0 absolute block rounded-t md:rounded-b md:shadow-lg hover:opacity-75"
                :src="job.img.src"
                :alt="job.img.alt"
              />
            </a>
          </div>
          <div
            class="px-6 pb-6 pt-3 md:w-1/2 md:px-12 md:py-8 md:flex md:items-center"
          >
            <div>
              <div class="antialiased text-2xl md:text-2xl font-medium ">
                <a
                  :href="job.link"
                  target="_blank"
                  rel="noopener noreferrer"
                  class="text-gray-100 hover:text-gray-300"
                  >{{ job.title }}</a
                >
              </div>
              <div
                class="text-gray-100 mt-2 md:mt-3 antialiased font-medium text-sm md:text-md leading-tight md:leading-normal opacity-90"
              >
                {{ job.description }}
              </div>
              <div class="px-6 py-4">
                <a
                  :href="tool.link"
                  target="_blank"
                  v-for="tool in job.tools"
                  v-bind:key="tool.name"
                  class="inline-block shadow-md bg-gray-300 hover:bg-gray-500 rounded-full px-3 py-1 text-xs font-semibold text-gray-700 mr-2"
                  >{{ tool.name }}</a
                >
              </div>
            </div>
          </div>
        </div>
      </transition-group>
    </div>
    <div class="flex  sm:invisible pt-4">
      <router-link
        to="/contact"
        class=" mx-auto text-center font-bold py-2 px-4 rounded flex items-center bg-blue-500 hover:bg-blue-700 text-gray-100 px-4 border-b-4 border-blue-800 shadow-md"
      >
        <span class="pr-3 tracking-wider font-mono">Contact Me</span>
        <svg
          class="fill-current"
          style="width:24px;height:24px"
          viewBox="0 0 24 24"
        >
          <path
            d="M4,11V13H16L10.5,18.5L11.92,19.92L19.84,12L11.92,4.08L10.5,5.5L16,11H4Z"
          />
        </svg>
      </router-link>
    </div>
  </div>
</template>
<script>
export default {
  data: function() {
    return {
      jobs: [
        {
          title: "CityWallet",
          description: `My responsibilities were to research and develop in the area of NFC technology (Near Field Communication) to create an intelligent payment system using single-board computers and micro-controllers, and achieve its integration to existing platforms (ex. Parking lot equipment and public transportation).`,
          link: "https://www.citywallet.net",
          img: {
            src: "/img/citywallet.png",
            alt: "Citywallet"
          },
          tools: [
            { name: "Python", link: "https://www.python.org" },
            { name: "Kivy", link: "https://kivy.org/" },
            { name: "Raspberry Pi", link: "https://www.raspberrypi.org" }
          ]
        },
        {
          title: "TZone",
          link: "http://tzone.run/",
          description: `I was a member of a startup project which focuses on the runners field. My responsibilities were to translate mobile mockups into components using React Native and make an integration with GPX files which traces the workout that a person did using smartwatches.`,
          img: {
            src: "/img/tzone.png",
            alt: "Tzone"
          },
          tools: [
            {
              name: "React Native",
              link: "https://facebook.github.io/react-native/"
            },
            {
              name: "ES6",
              link:
                "https://https://developer.mozilla.org/en-US/docs/Web/JavaScript/New_in_JavaScript/ECMAScript_2015_support_in_Mozilla.org/"
            }
          ]
        },
        {
          title: "PGA Group",
          link: "http://pgagroup.online",
          description: `I had the opportunity to focus on analyzing the customer needs and I was able to develop and host a WordPress website which meets their requirements and keep the brand style guide.`,
          img: {
            src: "/img/pgagroup.png",
            alt: "PGA"
          },
          tools: [
            { name: "WordPress", link: "https://wordpress.org" },
            { name: "PHP", link: "https://www.php.net" }
          ]
        },
        {
          title: "Firefly Integrations",
          link: "https://www.vegatouch.com",
          description:
            "My responsibilities included the initial research and development of features and projects, and develop web application tools for internal use and web applications for the company clients.",
          img: {
            src: "/img/vegatouch.png",
            alt: "Firefly"
          },
          tools: [
            { name: "Angular +", link: "https://angular.io/" },
            { name: "Vue.js", link: "https://vuejs.org" },
            { name: "AWS", link: "https://aws.amazon.com" }
          ]
        },
        {
          title: "MHVillage",
          link: "https://www.mhvillage.com",
          description:
            "My responsabilities as FrontEnd developer are planing and develop features for a server-side web application with thousands of visitors per day.",
          img: {
            src: "/img/mhvillage.png",
            alt: "Firefly"
          },
          tools: [{ name: "Angular +", link: "https://angular.io/" }]
        }
      ]
    };
  }
};
</script>
<style scoped>
.bg-job {
  background-color: #5b6467;
  background-image: linear-gradient(315deg, #5b6467 0%, #8b939a 74%);
}
</style>
