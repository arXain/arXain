<template>
<div>
    <div class="container">
        <navbar-component 
         @update:header="value => header = value" 
         @update:view="value => currentView = value" 
         @update:sub="value => subtitle = value">
        </navbar-component>
    </div>
    <div class="container">
        <page-heading-component :title="header"/>
    </div>
    <div class="container">
        <div class="panel panel-default panel-article">
            <div class="panel-heading">
                <h3 class="panel-title"><center> {{ subtitle }}</center></h3>
            </div>
            <div class="panel-body"><center>
                <div v-if='web3find === undefined'>
                <p>No web3 element (MetaMask/Mist) detected. Download MetaMask or another wallet client to use this page from the browser. </p>
                </div>
                <div v-else>
                    <load-contracts
                    :localWeb3='web3find'
                    :load='currentView'
                    ></load-contracts>
                </div>
            </center></div>
        </div>
    </div>
</div>
</template>

<script>
import NavbarComponent from '../components/NavbarComponent.vue'
import PageHeadingComponent from '../components/PageHeadingComponent.vue'
import LoadContracts from '../components/LoadContracts.vue'
export default {
    components: {
        NavbarComponent, PageHeadingComponent, LoadContracts
    },
    data: function () {
        return {
            currentView: 'paper-submit',
            header: 'ar&chi;ain Submission Form',
            subtitle: 'Submit here'
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
    }
}
</script>

<style scoped>
</style>
