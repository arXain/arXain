<!-- submitContract -->
<template>
    <div>
        <button type="submit" class="btn btn-default btn-create" v-on:click.prevent="handleCreate">Create Contract</button>
        <br><br>
        <div class="form-group">
            <strong>Paper Hash</strong>: <input type="text" placeholder="Paper Hash" v-model="submitHash">
        </div>
        <button type="submit"  class="btn btn-default btn-submit" v-on:click.prevent="handleSubmit">Submit Paper</button>
        <br><br>
        <span v-html="message"></span><br>
   </div>
</template>

<script>
import BetaWeb3 from 'web3'

export default {
    data () {
        return {
            submitHash: '',
            contractAddr: '',
            message: ''
        }
    },
    props: ['localWeb3','contracts','contractArtifacts'],
    methods: {
        handleCreate: function() {
            console.log('local web3 is: '+this.localWeb3.version.api);
            console.log('global web3 is: '+BetaWeb3.version);
            var betaWeb3 = new BetaWeb3(this.localWeb3.currentProvider);
            //betaWeb3 = new BetaWeb3(window.web3.currentProvider);
            var el = this;
            //el.localWeb3.eth.getAccounts(function(error, accounts) {
            betaWeb3.eth.getAccounts(function(error, accounts) {
                if (error) {
                    console.log(error);
                    el.message = 'Error: '+ error;
                }
                //get account from provider
                var account = accounts[0];
                //set defaults
                el.contracts.Paper.defaults({
                    from: account,
                    gas: 2100000,
                    gasPrice: '20000000000'
                });
                el.message = 'Creating the contract...';
                /*
                BUG: Contract.new() should fire two callback functions, once when the contract
                transaction is set, and then again once the contract itself is set. But
                MetaMask does not resolve the promise of a successfully deployed contract,
                it only returns the transaction address:
                https://github.com/MetaMask/metamask-extension/issues/2426.
                We are using the work-around described in 
                https://github.com/trufflesuite/truffle-contract/issues/70#issuecomment-355376332
                for now. Once bug is fixed we can use this...
                instead though we have to do (start workaround)...
                */
                var tempContract = new betaWeb3.eth.Contract(el.contractArtifacts.Paper.abi );
                tempContract.deploy({ data: el.contractArtifacts.Paper.bytecode })
                .send({ 
                    from: account, 
                    gas: 1435500, 
                    gasPrice: '20000000000' 
                }, function(error, transactionHash) { 
                    if(error) {
                        console.log(error);
                        el.message = error;
                        //return error;
                    } else {
                        console.log('transaction hash is : '+transactionHash); 
                        el.message = 'transaction hash is : '+transactionHash;
                    }
                }).on('receipt', function(instance) {
                    el.message = 'Success! Contract created at address '+instance.contractAddress.toLowerCase()+'.<br> Put this into your papers metadata and put the paper hash below.';
                    console.log('Successful contract creation.');
                    el.contractAddr = instance.contractAddress.toLowerCase();
                }).on('error', function(error) {
                    console.log(error.message);
                    el.message = 'Contract Creation Failed!';
                });
            });
        },
		handleSubmit: function() {
            var paperHash = this.submitHash;
            var contractAddr = this.contractAddr;
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
                el.message = 'Initializing the contract...';
                paperInstance.initPaper(paperHash).then(function(result) {
                    el.message = 'Success! Your paper has been registered on the blockchain';
                    console.log('Successful submission');
                }).catch(function(err) {
                    el.message = 'paper submission failed!';
                    console.log(err.message);
                });
            });
        }
    }
}
</script>


<style scoped>

/* using web3 1.0-beta

*/
/*using web3 0.2
                var tempContract = el.localWeb3.eth.contract(el.contractArtifacts.Paper.abi );
                tempContract.new({
                    data: el.contractArtifacts.Paper.bytecode,
                    from: account,
                    gas: 1435500,
                    gasPrice: '20000000000'
                }, function(error, myContract){
                    if(!error) {
                        if(!myContract.address) {
                        console.log('transaction hash is: '+myContract.transactionHash);
                            el.message = "Contract creation success! Use this Tx has to find the contract address in 'Check Blockchain' <br> Tx Address is: <b>"+myContract.transactionHash+"</b>";
                        } else {
                            console.log('contract address is: '+myContract.address);
                            el.message = "Contract creation success! <br> Contract address is: <b>"+myContract.address+"</b>";
                        }
                    }else{
                        console.log(error);
                        el.message = "Contract creation failed!";
                    }
                });
*/

/*using truffle contract
                el.contracts.Paper.new().then(function(instance) {
                    console.log(instance);
                    el.message = "Success!";
                }).catch(function(error) {
                    console.log(error);
                    el.message = "Error!";
                });
*/
</style>
