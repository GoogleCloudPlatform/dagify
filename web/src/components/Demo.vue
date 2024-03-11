

<template>
  <h1>Airflow Agent</h1>

  <div class="card">
    <p>
     {{ apiVersion }}
    </p>
  </div>
</template>



<script setup>
    import {ref, reactive, onMounted, computed } from 'vue';
    import axios from "axios";

    const apiVersion = ref(null);

    onMounted(async () => {
        console.log('Application mounted')
        try {
            const response = await axios.get('/api/v1/version');
            apiVersion.value = response.data.version; 
        } catch (error) {
            console.error("Error fetching API version:", error);
        }
   

        return { apiVersion }; 
    });
</script>