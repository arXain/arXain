<template>
    <div>
    </div>
</template>

<script>
import TruffleContract from 'truffle-contract'

export default {
    data: function () {
        return {
        }
    },
    props: ['localWeb3','load'],
    methods: {
        findContracts: function(contracts, i) {
            var el = this;
            if (i < this.load.length) {
                var item = this.load[i];
                $.getJSON('/build/contracts/'+item+'.json', function(data) {
                    // Get the necessary contract artifact file
                    // and instantiate it with truffle-contract
                    var Artifact = data;
                    contracts[item] = TruffleContract(Artifact);
                    // Set the provider for our contract
                    contracts[item].setProvider(el.localWeb3.currentProvider);
                    contracts[item].defaults({
                        gas: 2100000,
                        gasPrice: 20000000000
                    });
                    el.findContracts(contracts, i+1);
                });
            }
         },
        findContractArtifacts: function(contractArtifacts, i) {
            var el = this;
            if (i < this.load.length) {
                var item = this.load[i];
                $.getJSON('/build/contracts/'+item+'.json', function(data) {
                    //work around for MetaMask, described in
                    //https://github.com/trufflesuite/truffle-contract/issues/70#issuecomment-355376332
                    //will be removed after MetaMask bug is fixed.
                    contractArtifacts[item] = data;
                    el.findContractArtifacts(contractArtifacts, i+1);
                });
            }
         }
    },
    mounted: function() {
        var contracts = {};
        this.findContracts(contracts, 0);
        var contractArtifacts = {};
        this.findContractArtifacts(contractArtifacts, 0);
        this.$emit('update:contractData', contracts);
        this.$emit('update:contractArtifacts', contractArtifacts);
    }
}
</script>

<style scoped>
</style>
