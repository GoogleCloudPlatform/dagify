import {defineStore} from 'pinia';

export const useAppConfig = defineStore({
    id: 'appConfig',
    state: () => ({
        debug: {
            showDetailedErrors: true
        },
    }),
    getters: {
        getShowDetailedErrors: state => {return state.debug['showDetailedErrors']},

    },
    actions: {
        setShowDetailedErrors(value) {
            this.debug['showDetailedErrors'] = value;
        }
    }
})