<template>
  <div class="container">
    <!-- Stage One -->
    <div v-show="currentWorkflowStep===1" class="flex gap-4 flex-row justify-center mt-8z">
      
      <div class="flex flex-row gap-4 flex-wrap justify-center">
        <div class="flex flex-col gap-4 flex-wrap justify-center">
          <div class="flex flex-col p-8 text-center text-2xl font-bold">
            Welcome AirLift
          </div>
        
      

        <div class="flex flex-row gap-4 flex-wrap justify-center">
          <div class="flex flex-col bg-white shadow-md rounded-lg p-8 text-center">
            <h1 class="text-xl font-bold mb-4">Start New Conversion</h1>
            <div class="flex flex-col gap-4 flex-wrap justify-center">
                <input type="file" accept=".xml" @change="handleFileUpload" ref="fileInput" />
                <button :disabled="!selectedFile" @click="uploadFile" 
                    class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
                Begin
                </button>
            </div>
          </div>
          <div class="flex flex-col bg-white shadow-md rounded-lg p-8 text-center">
            <h1 class="text-xl font-bold mb-4">Continue Existing Conversion</h1>
            
            <div class="flex flex-col gap-4 flex-wrap justify-center" v-if="!existingConversions.length">
              <h1 class="text-xs font-bold mb-4">No existing conversion jobs</h1>
            </div>
            <div class="flex flex-col gap-4 flex-wrap justify-center" v-else>
                <select v-model="selected">
                  <option v-for="conversion in existingConversions" v-bind:value="conversion.id" :selected="conversion.id">
                    {{ conversion.name }}
                  </option>
                </select>
                <button :disabled="!selectedFile" @click="uploadFile" 
                    class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
                Continue
                </button>
            </div>
          </div>
        </div>
        </div>
      </div>

    </div>

    <div v-show="currentWorkflowStep===2" class="flex gap-4 flex-row justify-center mt-8z">
      
      <div class="flex flex-row gap-4 flex-wrap justify-center">
        <div class="flex flex-col gap-4 flex-wrap justify-center">
          <div class="flex flex-col p-8 text-center text-2xl font-bold">
            Analyze
          </div>
          <button :disabled="!conversionID" @click="analyzeData" 
                    class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
                Analyze Control-M Data
                </button>
        </div>
      </div>

    </div>

  </div>

  </template>

<script setup>
import axios from 'axios';
import { onMounted, ref } from 'vue'; 
import {useFlashMessagesStore} from '../stores/flashMessages';

const fMsg = useFlashMessagesStore();
const selectedFile = ref(null);
const existingConversions = ref([])
const handleFileUpload = (event) => {
  selectedFile.value = event.target.files[0];
};

const currentWorkflowStep = ref(0);

// API Control Variables 
const conversionID = ref(null); 







const uploadFile = async () => {
  if (!selectedFile.value) return; // Early exit if no file

  const formData = new FormData();
  formData.append("file", selectedFile.value);

  try {
    let resp = await axios.post('/api/v1/conversions', formData, {
      headers: {
        'Content-Type': 'multipart/form-data'
      }
    });
    // Use ref directly for accessing input element
    selectedFile.value = null; 
    fMsg.addMessage({text:'File uploaded successfully!',details:resp.data.message, type:'success'})
    if (resp.data.conversion.id == undefined || resp.data.conversion.id == null){
      fMsg.addMessage({text:'An error occurred during upload.', details:'server did not return a conversion id, which is required for analysis', type:'error'})
      return;
    }
    conversionID.value = resp.data.conversion.id;
    currentWorkflowStep.value++
  } catch (error) {
    fMsg.addMessage({text:'An error occurred during upload.', details:error.response.data.message, type:'error'})
  }
};

const analyzeData = async () => {

  try {
    if (!conversionID.value) return; // Early exit if no file

    let resp = await axios.post('/api/v1/conversions/'+conversionID.value+'/analyze', {
      headers: {
        'Content-Type': 'multipart/form-data'
      }
    });
    // Use ref directly for accessing input element
    console.log(resp)
    fMsg.addMessage({text:'Analyzed Successfully!',details:resp.data.message, type:'success'})
    //currentWorkflowStep.value++
  } catch (error) {
    console.log(error)
    fMsg.addMessage({text:'An error occurred while analyzing data.', details:error.response.data.message, type:'error'})
  }
};

onMounted(async () => {

    console.log("Set Workflow Step === 1")
    currentWorkflowStep.value = 1


    console.log('Loading Existing Conversions')
    try {
        const response = await axios.get('/api/v1/conversions');
        existingConversions.value = response.data; 
    } catch (error) {
        fMsg.addMessage({text:'An error occurred while loading existing conversions.', details:error.response.data.message, type:'error'})
    }

    return { existingConversions }; 
});
</script>