<template>
    <div>

    </div>
    <!--<h1 class="text-xl font-bold mb-4">Start New Conversion</h1>
    <div class="flex flex-col gap-4 flex-wrap justify-center">
        <input type="file" accept=".xml" @change="handleFileUpload" ref="fileInput" />
        <button :disabled="!selectedFile" @click="uploadFile" 
            class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
        Begin
        </button>
    </div>-->
</template>

<script setup>
// Import Vue Components 
import { onMounted, ref } from 'vue'; 
// Import Plugins
// -- None
// Import Components 
// -- None
// Import Stores 
import {useWorkflowConversionsStore} from '@stores/workflows/conversions';
// Define Variables 
// -- Stores
// -- Objects 
const myObject = ref({
  form: {
    name: null,        // [Required] - Name of Conversion
    description: null, // [Optional] - Description of Conversion
  },
});
const cStore = useWorkflowConversionsStore();
// -- Functions
const onSubmit = (event) => {
    event.preventDefault();
    alert("Form Submitted")
}
</script>

