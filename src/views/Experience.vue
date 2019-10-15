<template>
  <div class="flex-1 h-full py-8 px-6 justify-center bg-gray-200 text-gray-800">
    <div class="max-w-6xl mx-auto py-8">
      <div class="lg:mx-12 text-5xl text-blue-700 font-normal">Experience</div>

      <div
        class="lg:mx-12 mt-6 sm:mt-12 bg-gray-700 rounded overflow-hidden shadow-lg md:flex"
        v-for="job in jobs"
        v-bind:key="job.title"
      >
        <div class="md:w-1/2 md:pt-16 md:pr-0 md:pl-12">
          <a class="block relative padding-image-sm md:padding-image-lg"  :href="job.link">
            <img
              class="inset-0 absolute block rounded-t md:rounded-b md:shadow-lg"
              :src="job.img.src"
              :alt="job.img.alt"
            />
          </a>
        </div>
        <div class="px-6 pb-6 md:w-1/2 md:px-12 md:py-8 md:flex md:items-center">
          <div>
            <div class="antialiased text-2xl md:text-2xl font-medium text-gray-100">{{job.title}}</div>
            <div
              class="text-gray-100 mt-2 md:mt-3 antialiased font-medium text-sm md:text-md leading-tight md:leading-normal opacity-75"
            >{{job.description}}</div>
          </div>
        </div>
      </div>
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
          }
        },
        {
          title: "TZone",
          link: "http://tzone.run/",
          description: `I was a member of a startup project which focuses on the runners field. My responsibilities were to translate mobile mockups into components using React Native and make an integration with GPX files which traces the workout that a person did using smartwatches.`,
          img: {
            src: "/img/tzone.png",
            alt: "Tzone"
          }
        },
        {
          title: "PGA Group",
          link: "http://pgagroup.online",
          description: `I had the opportunity to focus on analyzing the customer needs and I was able to develop and host a WordPress website which meets their requirements and keep the brand style guide.`,
          img: {
            src: "/img/pgagroup.png",
            alt: "PGA"
          }
        },
        {
          title: "Firefly Integrations",
          link: "http://www.fireflyint.com",
          description:
            "My responsibilities include the initial research and development of features and projects, and develop web application tools for internal use and web applications for the company clients.",
          img: {
            src: "/img/fireflyint.jpg",
            alt: "Firefly"
          }
        }
      ]
    };
  }
};
</script>
