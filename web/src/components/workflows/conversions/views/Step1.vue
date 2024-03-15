<template>
    <div class="flex gap-4 flex-row justify-center mt-8z">
        Step 1: Start a Conversion
        <FormConversionSelect />
        <FormConversionCreate />
    </div>
</template>

<script setup>
// Import Vue Components 
import { ref } from 'vue'; 
// Import Components 
import FormConversionCreate from '/src/components/workflows/conversions/forms/FormConversionCreate.vue';
import FormConversionSelect from '/src/components/workflows/conversions/forms/FormConversionSelect.vue';
</script>
