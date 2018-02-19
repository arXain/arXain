<template>
    <div>
    </div>
</template>

<script>
import TruffleContract from 'truffle-contract'

export default {
    data: function () {
        return {}
    },
    props: ['localWeb3','load'],
    methods: {
        findContracts: function() {
            var contracts = {};
            var el = this;
            $.getJSON('/build/contracts/'+this.load+'.json', function(data) {
                // Get the necessary contract artifact file
                // and instantiate it with truffle-contract
                var Artifact = data;
                contracts[el.load] = TruffleContract(Artifact);
                // Set the provider for our contract
                contracts[el.load].setProvider(el.localWeb3.currentProvider);
                contracts[el.load].defaults({
                    gas: 2100000,
                    gasPrice: 20000000000
                });
            });
            return contracts;        
         },
        findContractArtifacts: function() {
            var contractArtifacts = {};
            var el = this;
            $.getJSON('/build/contracts/'+this.load+'.json', function(data) {
                //work around for MetaMask, described in
                //https://github.com/trufflesuite/truffle-contract/issues/70#issuecomment-355376332
                //will be removed after MetaMask bug is fixed.
                contractArtifacts[el.load] = data;
            });
            return contractArtifacts;        
         }
    },
    mounted: function() {
        var contracts = this.findContracts();
        var contractArtifacts = this.findContractArtifacts();
        this.$emit('update:contractData', contracts);
        this.$emit('update:contractArtifacts', contractArtifacts);
    }
}
</script>

<style scoped>
</style>
