<template>
    <div>
        <component :is='load'
          :localWeb3='localWeb3'
          :contracts='findContract'
          :contractArtifacts='findContractArtifacts'
        ></component>
    </div>
</template>

<script>
import TruffleContract from 'truffle-contract'
import PaperSubmit from '../components/PaperSubmit.vue'
import PaperStatus from '../components/PaperStatus.vue'
import PaperAmend from '../components/PaperAmend.vue'
import PaperComments from '../components/PaperComments.vue'

export default {
    components: {
        PaperSubmit, PaperStatus,
        PaperAmend, PaperComments
    },
    data: function () {
        return {}
    },
    props: ['load','localWeb3'],
    computed: {
        findContract: function() {
            var contracts = {};
            var el = this;
            $.getJSON('/build/contracts/Paper.json', function(data) {
                // Get the necessary contract artifact file
                // and instantiate it with truffle-contract
                var PaperArtifact = data;
                contracts.Paper = TruffleContract(PaperArtifact);
                // Set the provider for our contract
                contracts.Paper.setProvider(el.localWeb3.currentProvider);
                contracts.Paper.defaults({
                    gas: 2100000,
                    gasPrice: 20000000000
                });
            });
            return contracts;        
         },
        findContractArtifacts: function() {
            var contractArtifacts = {};
            $.getJSON('/build/contracts/Paper.json', function(data) {
                //work around for MetaMask, described in
                //https://github.com/trufflesuite/truffle-contract/issues/70#issuecomment-355376332
                //will be removed after MetaMask bug is fixed.
                contractArtifacts.Paper = data;
            });
            return contractArtifacts;        
         }
    }
}
</script>

<style scoped>
</style>
