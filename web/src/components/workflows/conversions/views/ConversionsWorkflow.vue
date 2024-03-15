<template>
    <div class="container">

      {{cStore.current.steps_current}}
      
      <!-- Stage One -->
      <ViewStep1 v-show="cStore.current.steps_current===1"/>
      <!-- Stage Two -->
      <ViewStep2 v-show="cStore.current.steps_current===2"/>
      <!-- Stage Three -->
      <ViewStep3 v-show="cStore.current.steps_current===3"/>
      <!-- Stage Four -->
      <ViewStep4 v-show="cStore.current.steps_current===4"/>
      <button class="btn btn-primary" @click="goBackStep()">Back</button>
      <button class="btn btn-primary" @click="goNextStep()">Next</button>
    </div>
  
  
  
    <!--  class="flex gap-4 flex-row justify-center mt-8z bg-red-100" -->
  
      <!--<div v-show="currentWorkflowStep===1" class="flex gap-4 flex-row justify-center mt-8z">
        
        <div class="flex flex-row gap-4 flex-wrap justify-center">
          <div class="flex flex-col gap-4 flex-wrap justify-center">
            <div class="flex flex-col p-8 text-center text-2xl font-bold">
              Welcome AirLift
            </div>
          <div class="flex flex-row gap-4 flex-wrap justify-center">
            <div class="flex flex-col bg-white shadow-md rounded-lg p-8 text-center">
              ---- Create New Conversion
            </div>
            <div class="flex flex-col bg-white shadow-md rounded-lg p-8 text-center">
              ---- Select Existing Conversion
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
  
      </div> -->
  
    </template>
  
  <script setup>
  // Import Vue Components 
  import { onMounted, ref } from 'vue'; 
  // Import Plugins
  import axios from 'axios';
  // Import Components 
  import ViewStep1 from '@/components/workflows/conversions/views/Step1.vue';
  import ViewStep2 from '@/components/workflows/conversions/views/Step2.vue';
  import ViewStep3 from '@/components/workflows/conversions/views/Step3.vue';
  import ViewStep4 from '@/components/workflows/conversions/views/Step4.vue';
  // Import Stores 
  import {useWorkflowConversionsStore} from '@stores/workflows/conversions';
  // Define Variables 
  // -- Stores
  const cStore = useWorkflowConversionsStore();
   // -- Functions
   const goNextStep = () => {
    cStore.nextStep();
   }
   const goBackStep = () => {
    cStore.previousStep();
   }
 


  // -- Variables
  //const selectedFile = ref(null);
  //const existingConversions = ref([])
  //const conversionID = ref(null); 
  // -- Functions
  //const handleFileUpload = (event) => {
  //  selectedFile.value = event.target.files[0];
  //};
  /*const uploadFile = async () => {
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
  };*/
  
  // On Mounted
  onMounted(async () => {
  
      //currentWorkflowStep.value = 1
  
  
      //console.log('Loading Existing Conversions')
      /*try {
          const response = await axios.get('/api/v1/conversions');
          existingConversions.value = response.data; 
      } catch (error) {
          fMsg.addMessage({text:'An error occurred while loading existing conversions.', details:error.response.data.message, type:'error'})
      }*/
  
      //return { existingConversions }; 
  });
  </script>