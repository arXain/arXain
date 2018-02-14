<!-- amendContract -->
<template>
    <div>
    <div class="form-group">
    <strong>Paper Hash</strong>: <input type="text" placeholder="Revised Paper Hash" v-model="amendHash">
    <br><br>
    <strong>Contract Address</strong>: <input type="text" placeholder="0x1" v-model="amendAddr">
    </div>
    <button type="submit" class="btn btn-default btn-submit" v-on:click.prevent="handleAmend">Submit</button>
    <br/><br>
    <span> {{ message }}</span>
    </div>
</template>

<script>

export default {
    data () {
        return {
            amendHash: '',
            amendAddr: '',
            message: ''
        }
    },
    props: ['localWeb3', 'contracts'],
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
