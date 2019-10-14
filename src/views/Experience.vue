<template>
  <div class="flex-1 h-full pt-8 px-6 justify-center bg-gray-200 text-gray-800">
    <div class="experience">
      <h1>This is an experience page</h1>
    </div>
  </div>
</template>
<script>
export default {
  data:function() {
    return{
      works:[{
        title:'CityWallet',
        description:`My responsibilities were to research and develop in the area of NFC technology (Near Field Communication) to create an intelligent payment system using single-board computers and micro-controllers, and achieve its integration to existing platforms (ex. Parking lot equipment and public transportation).`,
        img:{
          src:'/assets/citywallet.png',
          alt:'Citywallet'
        }
      },
        {
        title:'TZone',
        description:`My responsibilities were to research and develop in the area of NFC technology (Near Field Communication) to create an intelligent payment system using single-board computers and micro-controllers, and achieve its integration to existing platforms (ex. Parking lot equipment and public transportation).`,
        img:{
          src:'/assets/citywallet.png',
          alt:'Citywallet'
        },
      }]
    }
  }
}
</script>