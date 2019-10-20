<template>
  <div class="lg:w-1/2">
    <transition name="fade">
      <Notification
        v-on:close="closeNotification"
        v-if="isNotificationOpen"
        :isError="isFetchError"
      ></Notification>
    </transition>
    <form>
      <div class="flex flex-wrap -mx-3 mb-4">
        <div class="w-full md:w-1/2 px-3">
          <label
            class="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2"
            for="email-input"
          >Email *</label>
          <input
            id="email-input"
            class="appearance-none block w-full bg-gray-100 text-gray-700 border border-gray-400 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white focus:border-gray-500"
            :class="{'border-red-500':!isEmailValid}"
            v-model="email"
            type="email"
            placeholder="Your Email..."
            @blur="isEmailValid=emailValid"
          />
          <p v-show="!isEmailValid" class="text-red-500 text-xs italic">Please insert a valid email.</p>
        </div>
        <div class="w-full md:w-1/2 px-3">
          <label
            class="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2"
            for="name-input"
          >Name *</label>
          <input
            id="name-input"
            class="appearance-none block w-full bg-gray-100 text-gray-700 border border-gray-400 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white focus:border-gray-500"
            type="text"
            placeholder="Your Name..."
            v-model="name"
          />
        </div>
        <div class="w-full px-3">
          <label
            class="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2"
            for="message-input"
          >Message *</label>
          <textarea
            id="message-input"
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
        <span class="pr-3 tracking-wider font-mono">Send</span>
        <svg class="fill-current" style="width:24px;height:24px" viewBox="0 0 24 24">
          <path
            d="M13 17H17V14L22 18.5L17 23V20H13V17M20 4H4A2 2 0 0 0 2 6V18A2 2 0 0 0 4 20H11.35A5.8 5.8 0 0 1 11 18A6 6 0 0 1 22 14.69V6A2 2 0 0 0 20 4M20 8L12 13L4 8V6L12 11L20 6Z"
          />
        </svg>
      </button>
    </div>
  </div>
</template>
<script>
import Notification from "./Notification";
export default {
  components: {
    Notification
  },
  data: function() {
    return {
      email: "",
      name: "",
      message: "",
      isEmailValid: true,
      isNotificationOpen: false,
      isFetchError: false,
      isSumited: false
    };
  },
  computed: {
    buttonDisable: function() {
      return !(this.emailValid && this.name && this.message && !this.isSumited);
    },
    emailValid: function() {
      const emailRegex = /^([A-Za-z0-9_\-.])+@([A-Za-z0-9_\-.])+\.([A-Za-z]{2,4})$/;
      return emailRegex.test(this.email);
    }
  },
  methods: {
    closeNotification: function() {
      this.isNotificationOpen = false;
    },
    sendMessage: function() {
      const { name, email, message } = this;
      this.isSumited = true;
      const url =
        "https://2j9xwebgc3.execute-api.us-east-1.amazonaws.com/Deployed";
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
          if (result === "ok") {
            this.name = "";
            this.email = "";
            this.message = "";
            this.isFetchError = false;
          } else {
            this.isFetchError = true;
          }
        })
        .catch(() => {
          this.isFetchError = true;
        })
        .finally(() => {
          this.isNotificationOpen = true;
          this.isSumited = false;
        });
    }
  }
};
</script>
<style>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s;
}
.fade-enter,
.fade-leave-to {
  opacity: 0;
}
</style>