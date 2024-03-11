<script setup>
import navBar from './components/Nav.vue'
import footerBar from './components/Footer.vue'
import flashMessage from './components/Flash.vue'
</script>

<template>
  <div class="flex flex-col min-h-screen">
    <navBar class="sticky top-0 z-10 shadow-md"/>
    <flashMessage class="sticky bottom-0"/>
    <router-view class="flex-1 min-w-full overflow-y-auto p-10" />
    <footerBar class="sticky bottom-0 z-10"/>
  </div>
</template>