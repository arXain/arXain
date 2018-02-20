<template>
<div>
    <navbar-component 
     @update:view="value => currentView = value">
    </navbar-component>
    <page-heading-component :title="currentView"/>
    <main role="main" class="container">
    <div class="row">
        <div class="col-md-12">
        <div class="my-3 p-3 bg-white rounded box-shadow">
            <center><h3>  IPFS status: <span> {{ ipfsMessage }} </span> </h3></center>
        </div>
        <div class="my-3 p-3 bg-white rounded box-shadow">
            <div v-if='web3find === undefined'>
            <p>No web3 element (MetaMask/Mist) detected. Download MetaMask or another wallet client to use this page from the browser. </p>
            </div>
            <div v-else>
                <component :is='currentView'
                :localWeb3='web3find'
                @ipfs:message="value => ipfsMessage = value"
                ></component>
            </div>
        </div>
        </div>
    </div>
    </main>
</div>
</template>

<script>
import NavbarComponent from '../components/NavbarComponent.vue'
import PageHeadingComponent from '../components/PageHeadingComponent.vue'
import LoadContracts from '../components/LoadContracts.vue'
import PaperSubmit from '../components/PaperSubmit.vue'
import PaperStatus from '../components/PaperStatus.vue'
import PaperAmend from '../components/PaperAmend.vue'
import PaperComments from '../components/PaperComments.vue'

import { initIpfs } from '../js/ipfs-helper.js'

export default {
    components: {
        NavbarComponent, PageHeadingComponent, PaperSubmit,
        PaperAmend, PaperComments, PaperStatus
    },
    props: ['initialView'],
    data: function () {
        return {
            currentView: this.initialView,
            ipfsMessage: ''
        }
    },
    computed: {
        web3find: function() {
            var localWeb3 = undefined;
            // Is there an injected web3 instance like MetaMask?
            if (typeof web3 !== 'undefined') {
                console.log('I found a web3 provider');
                localWeb3 = new Web3(web3.currentProvider);
             } else {
                // If no injected web3 instance is detected, fall back to Ganache
                console.log("I did not find a web3 instance. Loading one from port 8545.")
                localWeb3 = new Web3(new Web3.providers.HttpProvider('http://localhost:8545'));
             }
             return localWeb3;        
         }
    },
    mounted: function() {
        this.ipfsMessage = "Loading...";
        var el = this;
        initIpfs().then(function (response) {
            console.log(response);
            if (response.data.Success) {
                el.ipfsMessage = "✅  ";
            } else {
                el.ipfsMessage = "❌ Error: Could not GET init.";
            }
        }).catch(function (error) {
            el.ipfsMessage = "❌  "+error+". Is the IPFS node running?";
            console.log(error);
        });
    }
}
</script>

<style scoped>
</style>
