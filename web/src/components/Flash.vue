<template>
    <div class="fixed top-0 right-0 m-6">
      <div v-for="message in fMsg.getMessages" :key="message.text"
        :class="{
          'bg-red-200 text-red-900 mb-3': message.type === 'error',
          'bg-green-200 text-green-900 mb-3': message.type === 'success',
          'bg-blue-200 text-blue-900 mb-3': message.type === 'info',
          'bg-grey-200 text-grey-900 mb-3': message.type === 'default',
        }"
        class="rounded-lg shadow-md p-6 pr-10"
        style="min-width: 240px"
      >
        <button :onClick="() => messages.splice(messages.indexOf(message), 1)"
          class="opacity-75 cursor-pointer absolute top-0 right-0 py-2 px-3 hover:opacity-100"
        >
          &times;
        </button>
        <div class="flex items-center">
          {{ message.text }}
        </div>
        <div class="flex items-center italic text-xs" v-if="appConfig.getShowDetailedErrors && message.details">
          {{ message.details }}
        </div>
      </div>
    </div>
  </template>
  

  <script setup>
    import { ref } from 'vue';
    import {useFlashMessagesStore} from '../stores/flashMessages';
    import {useAppConfig} from '../stores/appConfig';
    const fMsg = useFlashMessagesStore();
    const appConfig = useAppConfig();
  </script>