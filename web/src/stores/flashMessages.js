import {defineStore} from 'pinia';

export const useFlashMessagesStore = defineStore({
    id: 'flashMessages',
    state: () => ({
        timeouts: {
            success: 5000,
            error: 15000,
            info: 10000,
            default: 25000,
        },
        messages: []
    }),
    getters: {
        getMessages: state => {return state.messages},
        getTimeout: state => {return (type) => state.timeouts[type]}
    },
    actions: {
        addMessage(message) {
            console.log(message)
            if(message.type == undefined || message.type == null) {
                message.type = "default"
            }
            
            if (message.timeout == undefined || message.timeout == null) {
                    message.timeout = this.getTimeout(message.type)
            }

            this.messages.unshift(message)
            let action = this
            setTimeout(function() {
                action.removeMessage(message)
            }, message.timeout)
           
        },
        removeMessage(message) {
            this.messages = this.messages.filter(item => item.id !== message.id);
        }
    }
})