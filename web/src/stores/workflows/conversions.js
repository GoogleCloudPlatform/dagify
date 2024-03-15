import {defineStore} from 'pinia';

export const useWorkflowConversionsStore = defineStore({
    id: 'workflowConversionsStore',
    state: () => ({
        // All the Default Values used for a Workflow Conversion Reset
        defaults: {
            steps_max: 4,
            steps_min: 1,
            steps_current: 1,
            steps_init: 1,
        },
        // Current Workflow Conversion State
        current: {
            steps_max: 4,
            steps_min: 1,
            steps_current: 1,
            steps_init: 1,
        },
    }),
    getters: {
       getWorkflowCurrentStep: (state) => {
           return state.current.steps_current;
       }
    },
    actions: {
        workflowReset() {
            // Reset the Currentflow to the Defaults
            this.current = this.defaults;
        },
        nextStep() {
            // Increment the Current Workflow Step (if possible)
            if (this.current.steps_current < this.current.steps_max){
                this.current.steps_current++;
            } else {
                this.current.steps_current = this.current.steps_max;
            }
        },
        previousStep() {
            // Decrement the Current Workflow Step (if possible)
            if (this.current.steps_current > this.current.steps_min){
                this.current.steps_current--;
            } else {
                this.current.steps_current = this.current.steps_min;
            }
        }
    }
})