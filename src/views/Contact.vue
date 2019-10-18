<template>
  <div class="flex-1 h-full pt-8 px-6 justify-center text-gray-800">
    <div class="max-w-lg w-full lg:max-w-6xl mx-auto">
      <div class="text-5xl text-blue-700 font-normal py-8 px-10">Contact Me</div>
    </div>

    <div class="max-w-lg lg:max-w-6xl mx-auto py-8 px-10 flex flex-wrap">
      <div class="flex flex-col lg:w-1/2 pr-8">
        <div
          class="hyphens-text leading-normal pb-4"
        >Have a question? Looking to work together? Want to grab a cup of coffee? Feel free to contact me!</div>
        <div class="inline-flex leading-normal text-left hyphens-text border-b py-4">
          <a
            class="inline-flex hover:text-blue-700"
            href="https://goo.gl/maps/BmMZgMrwSHdC86eK8"
            target="_blank"
            rel="noopener noreferrer"
          >
            <svg style="width:24px;height:24px" class="fill-current" viewBox="0 0 24 24">
              <path
                d="M12,11.5A2.5,2.5 0 0,1 9.5,9A2.5,2.5 0 0,1 12,6.5A2.5,2.5 0 0,1 14.5,9A2.5,2.5 0 0,1 12,11.5M12,2A7,7 0 0,0 5,9C5,14.25 12,22 12,22C12,22 19,14.25 19,9A7,7 0 0,0 12,2Z"
              />
            </svg>
            <span class="pl-2">South Bend, IN</span>
          </a>
        </div>
        <div class="inline-flex leading-normal text-left hyphens-text border-b py-4">
          <a
            class="inline-flex hover:text-blue-700"
            href="https://github.com/saurer19"
            target="_blank"
            rel="noopener noreferrer"
          >
            <svg class="fill-current" style="width:24px;height:24px" viewBox="0 0 24 24">
              <path
                d="M12,2A10,10 0 0,0 2,12C2,16.42 4.87,20.17 8.84,21.5C9.34,21.58 9.5,21.27 9.5,21C9.5,20.77 9.5,20.14 9.5,19.31C6.73,19.91 6.14,17.97 6.14,17.97C5.68,16.81 5.03,16.5 5.03,16.5C4.12,15.88 5.1,15.9 5.1,15.9C6.1,15.97 6.63,16.93 6.63,16.93C7.5,18.45 8.97,18 9.54,17.76C9.63,17.11 9.89,16.67 10.17,16.42C7.95,16.17 5.62,15.31 5.62,11.5C5.62,10.39 6,9.5 6.65,8.79C6.55,8.54 6.2,7.5 6.75,6.15C6.75,6.15 7.59,5.88 9.5,7.17C10.29,6.95 11.15,6.84 12,6.84C12.85,6.84 13.71,6.95 14.5,7.17C16.41,5.88 17.25,6.15 17.25,6.15C17.8,7.5 17.45,8.54 17.35,8.79C18,9.5 18.38,10.39 18.38,11.5C18.38,15.32 16.04,16.16 13.81,16.41C14.17,16.72 14.5,17.33 14.5,18.26C14.5,19.6 14.5,20.68 14.5,21C14.5,21.27 14.66,21.59 15.17,21.5C19.14,20.16 22,16.42 22,12A10,10 0 0,0 12,2Z"
              />
            </svg>
            <span class="pl-2">saurer19</span>
          </a>
        </div>
        <div class="inline-flex leading-normal text-left hyphens-text py-4">
          <a
            class="inline-flex hover:text-blue-700"
            href="https://www.linkedin.com/in/gabriel-alexander-rivas-rojas-571227b4/"
            target="_blank"
            rel="noopener noreferrer"
          >
            <svg class="fill-current" style="width:24px;height:24px" viewBox="0 0 24 24">
              <path
                d="M19,3A2,2 0 0,1 21,5V19A2,2 0 0,1 19,21H5A2,2 0 0,1 3,19V5A2,2 0 0,1 5,3H19M18.5,18.5V13.2A3.26,3.26 0 0,0 15.24,9.94C14.39,9.94 13.4,10.46 12.92,11.24V10.13H10.13V18.5H12.92V13.57C12.92,12.8 13.54,12.17 14.31,12.17A1.4,1.4 0 0,1 15.71,13.57V18.5H18.5M6.88,8.56A1.68,1.68 0 0,0 8.56,6.88C8.56,5.95 7.81,5.19 6.88,5.19A1.69,1.69 0 0,0 5.19,6.88C5.19,7.81 5.95,8.56 6.88,8.56M8.27,18.5V10.13H5.5V18.5H8.27Z"
              />
            </svg>
            <span class="pl-2">Gabriel Rivas</span>
          </a>
        </div>
      </div>
      <div class="lg:w-1/2">
        <form>
          <div class="flex flex-wrap -mx-3 mb-4">
            <div class="w-full md:w-1/2 px-3">
              <label
                class="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2"
                for="grid-password"
              >Email *</label>
              <input
                class="appearance-none block w-full bg-gray-100 text-gray-700 border border-gray-400 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white focus:border-gray-500"
                v-model="email"
                type="email"
                placeholder="Your Email..."
              />
            </div>
            <div class="w-full md:w-1/2 px-3">
              <label
                class="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2"
                for="grid-password"
              >Name *</label>
              <input
                class="appearance-none block w-full bg-gray-100 text-gray-700 border border-gray-400 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white focus:border-gray-500"
                type="text"
                placeholder="Your Name..."
                v-model="name"
              />
            </div>
            <div class="w-full px-3">
              <label
                class="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2"
                for="grid-password"
              >Message *</label>
              <textarea
                v-model="message"
                placeholder="Your Message..."
                rows="6"
                class="appearance-none block w-full bg-gray-100 text-gray-700 border border-gray-400 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white focus:border-gray-500"
              ></textarea>
            </div>
          </div>
        </form>
        <div class="w-full flex">
          <button
            class="mx-auto text-center font-bold py-2 px-4 rounded inline-flex items-center"
            @click="sendMessage"
            :disabled="buttonDisable"
            :class="{'bg-blue-500 hover:bg-blue-700 text-gray-100 px-4 border-b-4 border-blue-800': !buttonDisable, 'bg-gray-300 text-gray-800 ':buttonDisable }"
          >
            <span class="pr-3">Sent</span>
            <svg class="fill-current" style="width:24px;height:24px" viewBox="0 0 24 24">
              <path
                d="M13 17H17V14L22 18.5L17 23V20H13V17M20 4H4A2 2 0 0 0 2 6V18A2 2 0 0 0 4 20H11.35A5.8 5.8 0 0 1 11 18A6 6 0 0 1 22 14.69V6A2 2 0 0 0 20 4M20 8L12 13L4 8V6L12 11L20 6Z"
              />
            </svg>
          </button>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  data: function() {
    return {
      email: "",
      name: "",
      message: ""
    };
  },
  computed: {
    buttonDisable: function() {
      return !(this.emailValid && this.name && this.message);
    },
    emailValid: function() {
      const emailRegex = /^([A-Za-z0-9_\-.])+@([A-Za-z0-9_\-.])+\.([A-Za-z]{2,4})$/;
      return emailRegex.test(this.email);
    }
  },
  methods: {
    sendMessage: function() {
      const { name, email, message } = this;
      const url =
        "https://535xyteb27.execute-api.us-east-1.amazonaws.com/Deployed/";
      fetch(url, {
        method: "POST",
        body: JSON.stringify({
          name,
          email,
          message
        })
      })
        .then(response => {
          return response.json();
        })
        .then(result => {
          this.name = "";
          this.email = "";
          this.message = "";
          console.log(result);
        })
        .catch(function(error) {
          console.log("Request failure: ", error);
        });
    }
  }
};
</script>
