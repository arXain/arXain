<!-- amendContract -->
<template>
    <div>
		<load-contracts
            :localWeb3='localWeb3'
            :load='contract'
            @update:contractData="value => contractData = value"
            @update:contractArtifacts="value => contractArtifacts = value">
        </load-contracts>
        <form>
        <div class="form-group">
            <label>Paper Hash:</label> 
            <input type="text" class="form-control" placeholder="Revised Paper Hash" v-model="amendHash">
        </div>
        <div class="form-group">
            <label>Contract Address:</label> 
            <input class="form-control" type="text" placeholder="0x1" v-model="amendAddr">
        </div>
        <div class="form-group">
            <button type="submit" class="btn btn-primary btn-submit" v-on:click.prevent="handleAmend">Submit</button>
        </div>
        <p><span> {{ message }}</span></p>
        </form>
    </div>
</template>

<script>
import LoadContracts from '../components/LoadContracts.vue'

export default {
    data () {
        return {
            amendHash: '',
            amendAddr: '',
            contract: 'Paper',
            contractData: {},
            contractArtifacts: {},
            message: ''
        }
    },
    props: ['localWeb3'],
	components: {
		LoadContracts	
	},
    methods: {
		handleAmend: function() {
            var paperHash = this.amendHash;
            var contractAddr = this.amendAddr;
            var paperInstance = this.contracts.Paper.at(contractAddr);
            var el = this;
            this.localWeb3.eth.getAccounts(function(error, accounts) {
                if (error) {
                    console.log(error);
                }
                //get account from provider
                var account = accounts[0];
                //set defaults
                el.contracts.Paper.defaults({
                    from: account,
                    gas: 200000,
                    gasPrice: 20000000000
                });
                el.message = 'Revising the contract...';
	            paperInstance.amendPaper(paperHash).then(function(result) {
                    el.message = 'Success! Your paper has been revised.';
                    console.log('Successful submission');
                }).catch(function(err) {
                    el.message = 'paper revision failed!';
                    console.log(err.message);
                });
            });
        }
    }
}
</script>


<style scoped>

</style>
