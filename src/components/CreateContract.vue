<template>
<div>
    <form>
        <h4> Step 1. Create an empty paper contract.</h4>
        <div class="form-group">
            <button type="submit" class="btn btn-primary btn-create" :disabled="contractCreated" v-on:click.prevent="createContract">Create Paper Contract</button>
        </div>
        <p><span v-html="messageContract"></span></p>
        <h4> Step 2. Create a comment contract.</h4>
        <div class="form-group">
            <button type="submit" class="btn btn-primary btn-create" :disabled="commentsCreated" v-on:click.prevent="createComments">Create Comments</button>
        </div>
        <p><span v-html="messageComments"></span></p>
    </form>
    <div class="form-group">
            <button type="submit" class="btn btn-primary btn-create" :disabled="(!commentsCreated || !contractCreated)" v-on:click.prevent="goToIpfs()">Next</button>
    </div>
</div>
</template>

<script>
import BetaWeb3 from 'web3'
import { initAuthor } from '../js/ipfs-helper.js'

export default {
    data () {
        return {
            contractCreated: false,
            contractAddress: '',
            commentsCreated: false,
            messageContract: '',
            messageComments: '',
        }
    },
    props: ['localWeb3','contractData',"contractArtifacts"],
	components: {
	},
    methods: {
        goToIpfs: function() {
            this.$emit('create:goToIpfs');
        },
        createContract: function() {
            console.log('local web3 is: '+this.localWeb3.version.api);
            console.log('global web3 is: '+BetaWeb3.version);
            var betaWeb3 = new BetaWeb3(this.localWeb3.currentProvider);
            var el = this;
            betaWeb3.eth.getAccounts(function(error, accounts) {
                if (error) {
                    console.log(error);
                    el.messageContract = 'Error: '+ error;
                }
                //get account from provider
                var account = accounts[0];
                //Create IPFS directory
                console.log('user account is '+account);
                el.createIpfs(account);
                //set defaults
                el.contractData['Paper'].defaults({
                    from: account,
                    gas: 2100000,
                    gasPrice: '20000000000'
                });
                el.messageContract = 'Creating the contract...';
                var tempContract = new betaWeb3.eth.Contract(el.contractArtifacts['Paper'].abi );
                tempContract.deploy({ data: el.contractArtifacts['Paper'].bytecode })
                .send({
                    from: account,
                    gas: 1435500,
                    gasPrice: '20000000000'
                }, function(error, transactionHash) {
                    if(error) {
                        console.log(error);
                        el.messageContract = error;
                        //return error;
                    } else {
                        console.log('transaction hash is : '+transactionHash);
                        el.messageContract = 'transaction hash is : '+transactionHash;
                    }
                }).on('receipt', function(instance) {
                    el.messageContract = 'Success! Contract created at address '+instance.contractAddress.toLowerCase()+'.';
                    console.log('Successful contract creation.');
                    var contractAddress = instance.contractAddress.toLowerCase();
                    el.contractAddress = contractAddress;
                    el.contractCreated = true;
                    el.$emit('create:contractId', contractAddress);
                    el.$emit('create:submitterId', account);
                }).on('error', function(error) {
                    console.log(error.message);
                    el.messageContract = 'Contract Creation Failed: '+error.message;
                });
            });
        },
        createIpfs: function(account) {
            this.$emit("ipfs:message", "Finding/Creating account...");
            var el = this;
            if (account == undefined) {
                el.$emit("ipfs:message", "❌ - Account address is undefined.");
            } else {
                initAuthor(account).then(function (response) {
                    if (response.data.Success) {
                        el.$emit("ipfs:message", "✅ account found");
                    } else {
                        el.$emit("ipfs:message", "❌: "+response.data.Message);
                    }
                }).catch(function (error) {
                    el.$emit("ipfs:message", "❌  "+error);
                    console.log(error);
                });
            }
        },
        createComments: function() {
            if(!this.contractCreated) {
                this.messageComments = "Error! Have to create a contract first!";
                return;
            }
            var betaWeb3 = new BetaWeb3(this.localWeb3.currentProvider);
            var el = this;
            betaWeb3.eth.getAccounts(function(error, accounts) {
                if (error) {
                    console.log(error);
                    el.messageComments = 'Error: '+ error;
                }
                //get account from provider
                var account = accounts[0];
                //Create IPFS directory
                console.log('user account is '+account);
                //set defaults
                el.contractData['Comments'].defaults({
                    from: account,
                    gas: 2100000,
                    gasPrice: '20000000000'
                });
                el.messageComments = 'Creating the contract...';
                var tempContract = new betaWeb3.eth.Contract(el.contractArtifacts['Comments'].abi );
                tempContract.deploy({ data: el.contractArtifacts['Comments'].bytecode, arguments: [el.contractAddress]})
                .send({
                    from: account,
                    gas: 400000,
                    gasPrice: '20000000000'
                }, function(error, transactionHash) {
                    if(error) {
                        console.log(error);
                        el.messageComments = error;
                        //return error;
                    } else {
                        console.log('transaction hash is : '+transactionHash);
                        el.messageComments = 'transaction hash is : '+transactionHash;
                    }
                }).on('receipt', function(instance) {
                    el.messageComments = 'Success! Comments created at address '+instance.contractAddress.toLowerCase()+'.';
                    console.log('Successful comments contract creation.');
                    var commentsAddress = instance.contractAddress.toLowerCase();
                    el.commentsCreated = true;
                    el.$emit('create:commentsId', commentsAddress);
                }).on('error', function(error) {
                    console.log(error.message);
                    el.messageComments = 'Comments Creation Failed! '+error.message;
                });
            });
        }
    }
}
</script>


<style scoped>

</style>
