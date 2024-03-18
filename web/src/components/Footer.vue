<template>
   <footer class="fixed bottom-0 left-0 w-full bg-gray-800 text-white text-center py-4">
    &copy; 2024 {{ appName }} -  {{ apiVersion }}
  </footer>
  </template>


<script setup>
import {ref, reactive, onMounted, computed } from 'vue';
import axios from "axios";

const apiVersion = ref(null);
const appName = ref(null);

onMounted(async () => {

    try {
        const response = await axios.get('/api/v1/app');
        appName.value = response.data.name; 
    } catch (error) {
        console.error("Error fetching App Name:", error);
    }

    try {
        const response = await axios.get('/api/v1/version');
        apiVersion.value = response.data.version; 
    } catch (error) {
        console.error("Error fetching API version:", error);
    }

    return { appName, apiVersion }; 
});
</script>