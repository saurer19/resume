<template>
  <div class="top-0 left-0 w-full fixed z-50 mt-32">
    <div
      class="max-w-2xl w-10/12 mx-auto px-4 py-3 rounded text-gray-200 shadow-2xl relative"
      role="alert"
      :class="isError?'bg-red-600 ':'bg-green-600'"
    >
      <span class="font-bold pr-1">{{isError?error.title:success.title}}</span>
      <span class="block sm:inline">{{isError?error.message:success.message}}</span>
      <span class="absolute top-0 bottom-0 right-0 px-4 py-3" @click="closeNotification">
        <svg
          class="fill-current h-6 w-6 text-gray-100"
          role="button"
          xmlns="http://www.w3.org/2000/svg"
          viewBox="0 0 20 20"
        >
          <title>Close</title>
          <path
            d="M14.348 14.849a1.2 1.2 0 0 1-1.697 0L10 11.819l-2.651 3.029a1.2 1.2 0 1 1-1.697-1.697l2.758-3.15-2.759-3.152a1.2 1.2 0 1 1 1.697-1.697L10 8.183l2.651-3.031a1.2 1.2 0 1 1 1.697 1.697l-2.758 3.152 2.758 3.15a1.2 1.2 0 0 1 0 1.698z"
          />
        </svg>
      </span>
    </div>
  </div>
</template>
<script>
export default {
  props: {
    isError: Boolean
  },
  data: function() {
    return {
      error: {
        title: "Opps...",
        message: "Something went wrong!"
      },
      success: {
        title: "Success!",
        message: "Your message has been sent successfully."
      }
    };
  },

  methods: {
    closeNotification: function() {
      this.$emit("close");
    }
  },
  created() {
    setTimeout(() => {
      this.closeNotification();
    }, 5000);
  }
};
</script>
