<template>
    <div>
        <div :class="{ valid: !v$.$error && v$.$dirty, error: v$.$error }">
            <input type="text" v-model="v$.name.$model"/>
        </div>
        <div v-for="(error, index) in v$.name.$errors" :key="index">
            {{ error.$message }}
        </div>
        <div :class="{ valid: !v$.$error && v$.$dirty, error: v$.$error }">
            <input type="text" v-model="v$.description.$model"/>
        </div>
        <div v-for="(error, index) in v$.description.$errors" :key="index">
            {{ error.$message }}
        </div>
        
        <input type="file" accept=".xml"/>
        <button @click="showAll = !showAll">Toggle All Output</button>
        <pre v-show="showAll">{{ v$ }}</pre>
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
import useVuelidate from "@vuelidate/core";
import {required, minLength, maxLength} from '@vuelidate/validators'
// Import Components 
// -- None
// Import Stores 
import {useWorkflowConversionsStore} from '@stores/workflows/conversions';
// Define Variables 
// -- Stores
const cStore = useWorkflowConversionsStore();
// -- Objects 
const showAll = ref(false);
const newConversionForm = reactive({
  fields: {
    file: null,        // [Required] - File to Upload
    name: null,        // [Required] - Name of Conversion
    description: null, // [Optional] - Description of Conversion
  },
  fieldRules: {
    name: {
      //required,
      minLength: minValue(5),
      maxLength: maxValue(300)
    },
    description: {
      maxLength: maxValue(500),
    },
  }
});
// -- Functions
const onSubmit = (event) => {
    event.preventDefault();
    alert("Form Submitted")
}

const v$ = useVuelidate(newConversionForm.fieldRules, newConversionForm.fields);
return { v$, showAll };
</script>

