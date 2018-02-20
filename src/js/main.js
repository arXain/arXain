import Vue from 'vue'
import VueClipboard from 'vue-clipboard2'
Vue.use(VueClipboard);

import Web3Box from '../components/Web3Box.vue'

new Vue({
    el: '#app',
    components: { 
        'web3-box': Web3Box 
    },
})

