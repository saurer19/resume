<template>
  <div class="flex-1 h-full py-8 px-6 justify-center text-gray-800">
    <div class="max-w-6xl mx-auto py-8">
      <div class="lg:mx-12 text-5xl text-blue-700 font-normal">Skills</div>
      <div class="flex flex-wrap pt-6 justify-center content-center">
        <div
          class="w-full md:flex mx-auto my-4 lg:mx-12 shadow-lg lg:max-w-full"
          v-for="(skill, index) in skills"
          v-bind:key="skill.title"
          :class="{'md:flex-row-reverse': index % 2 === 0}"
        >
          <div
            class="h-64 md:h-auto md:w-1/2 flex-none rounded-t text-center overflow-hidden bg-grad"
            :class="{'md:rounded-none md:rounded-r ': index % 2 === 0, ' md:rounded-none md:rounded-l ': index % 2 !== 0}"
          >
            <div class="py-16 inline-flex justify-around" :class="{'imgs-row': index % 2 === 0}">
              <img
                v-for="skillImg in skill.imgs"
                v-bind:key="skillImg.alt"
                class="h-32"
                :src="skillImg.src"
                alt="react.js logo"
              />
            </div>
          </div>
          <div
            class="w-full md:w-1/2 border-r border-b border-l border-gray-300 md:border-l-0 md:border-t bg-white rounded-b md:rounded-b-none p-4 flext flex-col justify-between leading-normal"
            :class="{'md:rounded-l ': index % 2 === 0, 'md:rounded-r ': index % 2 !== 0}"
          >
            <div class="font-bold text-xl mb-2 p-2 text-gray-800">{{skill.title}}</div>
            <div class="text-gray-700 text-base p-2 text-gray-700">{{skill.description}}</div>
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
      skills: [
        {
          title: "Javascript",
          description: `I’m very confident with my JavaScript knowledge, I have worked with the DOM API and the core concepts behind JS and ES6, I have experience with the most popular Frameworks (React, Vue and Angular +). I also have experience working with modern toolings as such as Webpack, NPM/Yarn and Babel.`,
          imgs: [
            {
              alt: "Vue",
              src: "/img/vue.svg"
            },
            {
              alt: "React",
              src: "/img/react.png"
            },
            {
              alt: "Angular",
              src: "/img/angular.svg"
            },
            {
              alt: "Node.js",
              src: "/img/node.svg"
            }
          ]
        },
        {
          title: "CSS3/HTML5",
          description: `I have worked using HTML/CSS for years, I have in-depth knowledge of the HTML/CSS API to keep cross-browser compatibility when it’s needed. I have experience working with plain CSS, with CSS Frameworks and using utility-first CSS frameworks.`,
          imgs: [
            {
              alt: "html",
              src: "/img/csshtml.svg"
            }
          ]
        },
        {
          title: "Python",
          description: `I have experience working with embedded system using Python to develop IU using Kivy, understanding GPIO and SPI interfaces communicate with micro-controllers, and back-end experience using Flask and SQLAlchemy`,
          imgs: [
            {
              alt: "Kivy",
              src: "/img/kivy.png"
            },
            {
              alt: "Flask",
              src: "/img/flask.png"
            },
            {
              alt: "SQLALchemy",
              src: "/img/python.svg"
            }
          ]
        },
        {
          title: "AWS",
          description: `I’m able to create a REST API using API Getaway and Lambda functions. 
I have experience creating CI/CD using Pipeline to automate the deployment of webapps.
Full understanding of IAM to grant the necessary permission.
`,
          imgs: [
            {
              alt: "AWS",
              src: "/img/aws.svg"
            }
          ]
        }
      ]
    };
  }
};
</script>
<style>
.imgs-row {
  width: 130%;
  animation-duration: 25s;
  animation-timing-function: linear;
  animation-delay: 0s;
  animation-iteration-count: infinite;
  animation-direction: alternate;
  animation-fill-mode: both;
  animation-play-state: running;
  animation-name: imgs;
}
@keyframes imgs {
  100% {
    transform: translate(20%);
  }
  50% {
    transform: translate(-20%);
  }
}
.bg-grad {
  background-color: #5b6467;
  background-image: linear-gradient(315deg, #5b6467 0%, #8b939a 74%);
}
</style>
