<template>
  <div class="flex-1 h-full pt-8 px-6 justify-center bg-gray-200 text-gray-800">
    <div class="text-3xl font-light">Skills</div>
    <div class="flex flex-col pt-6 justify-center content-center">
      <transition-group
        name="staggered-fade"
        tag="div"
        v-bind:css="false"
        v-on:before-enter="beforeEnter"
        v-on:enter="enter"
        v-on:leave="leave"
      >
        <div
          class="w-10/12 w-full md:flex mx-auto my-4 shadow-lg"
          v-for="skill in skills"
          v-bind:key="skill.title"
        >
          <div
            class="h-64 md:h-auto md:w-1/2 flex-none rounded-t md:rounded-t-none md:rounded-l text-center overflow-hidden bg-blue-900"
          >
            <div class="flex py-3">
              <img class="h-16 w-full" src="@/assets/react-logo.svg" alt="react.js logo" />
              <img class="h-16 w-full" src="@/assets/react-logo.svg" alt="react.js logo" />
            </div>
          </div>
          <div
            class="w-full md:w-1/2 border-r border-b border-l border-gray-300 md:border-l-0 md:border-t bg-white rounded-b md:rounded-b-none md:rounded-r p-4 flext flex-col justify-between leading-normal"
          >
            <div class="font-bold text-xl mb-2 p-2">{{skill.title}}</div>
            <div class="text-gray-700 text-base p-2">{{skill.description}}</div>
          </div>
        </div>
      </transition-group>
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
          description: `I’m very confident with my JavaScript knowledge, I have experience working with the DOM API, the core concepts behind JS and ES6, I have experience with the most popular Frameworks (React, Vue and Angular +). I also have experience working with modern toolings as such as Webpack, NPM/Yarn and Babel.`,
          imgs: [
            {
              row1: [
                {
                  alt: "Vue",
                  src: "/assets/vue.svg"
                },
                {
                  alt: "React",
                  src: "/assets/react.svg"
                },
                {
                  alt: "Angular",
                  src: "/assets/angular.svg"
                }
              ],
              row2: [
                {
                  alt: "Express.js",
                  src: "/assets/express.svg"
                },
                {
                  alt: "Node.js",
                  src: "/assets/node.svg"
                },
                {
                  alt: "ES6",
                  src: "/assets/es6.svg"
                }
              ]
            }
          ]
        },
        {
          title: "CSS3/HTML5",
          description: `I have worked using HTML/CSS for years, I have in-depth knowledge of the HTML/CSS API to keep cross-browser compatibility when it’s needed. I have experience working with plain CSS, with CSS Frameworks and using utility-first CSS frameworks.`,
          imgs: [
            {
              alt: "html",
              src: "/assets/kivy.svg"
            },
            {
              alt: "css",
              src: "/assets/flask.svg"
            }
          ]
        },
        {
          title: "Python",
          description: `I have experience working with embedded system using Python to develop IU using Kivy, understanding GPIO and SPI interfaces communicate with micro-controllers, and back-end experience using Flask and SQLAlchemy`,
          imgs: [
            {
              alt: "Kivy",
              src: "/assets/kivy.svg"
            },
            {
              alt: "Flask",
              src: "/assets/flask.svg"
            },
            {
              alt: "SQLALchemy",
              src: "/assets/sqlalchemy.svg"
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
              src: "/assets/aws.svg"
            }
          ]
        }
      ]
    };
  }
};
</script>