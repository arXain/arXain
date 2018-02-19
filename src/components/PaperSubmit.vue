<template>
<div>
    <load-contracts
        :localWeb3='localWeb3'
        :load='contract'
        @update:contractData="value => contractData = value"
        @update:contractArtifacts="value => contractArtifacts = value">
    </load-contracts>
        <h4> Step 1. Create an empty contract.</h4>
        <div class="form-group">
            <button type="submit" class="btn btn-primary btn-create" v-on:click.prevent="createContract">Create Contract</button>
        </div>
        <p><span v-html="message"></span></p>
        <h4> Step 2. Enter details and upload to IPFS.</h4>
        <div class="form-group">
            <label for="contract">Contract Address:</label>
            <div class="input-group mb-3">
                <input type="text" class="form-control" pattern="[A-Za-z0-9]" :disabled="contractCreated == true" placeholder="0x0" v-model="contractAddr">
                <div class="input-group-append">
                    <button class="btn btn-outline-secondary" type="button" v-clipboard:copy="contractAddr">Copy</button>
                </div>
            </div>
        </div>

       <ipfs-submit
            @ipfs:fileDir="value => submitIpfs(value)"
            @ipfs:resetPaper="value => paperCreated = false">
       </ipfs-submit>

        <div class="form-group">
           <label for="contract">Paper Hash:</label>
            <div class="input-group mb-3">
                <input type="text" pattern="[A-Za-z0-9]" :disabled="paperCreated == true" class="form-control" placeholder="Paper Hash" v-model="paperHash">
                <div class="input-group-append">
                    <button class="btn btn-outline-secondary" type="button" v-clipboard:copy="paperHash">Copy</button>
                </div>
            </div>
        </div>
        <p><span v-html="messageIpfs"></span></p>
        <br>
        <h4> Step 3. Submit paper to the blockchain.</h4>
        <div class="form-group">
            <button type="submit" class="btn btn-primary btn-submit" v-on:click.prevent="submitContract">Submit Paper</button>
        </div>
        <p><span v-html="messageInit"></span></p>
</div>
</template>

<script>
import BetaWeb3 from 'web3'
import LoadContracts from '../components/LoadContracts.vue'
import IpfsSubmit from '../components/IpfsSubmit.vue'
import { initAuthor, submitManuscript } from '../js/ipfs-helper.js'

export default {
    data () {
        return {
            paperHash: '',
            contractAddr: '',
            contractCreated: false,
            paperCreated: false,
            contract: 'Paper',
            contractData: {},
            contractArtifacts: {},
            message: '',
			messageIpfs: '',
            messageInit: ''
        }
    },
    props: ['localWeb3'],
	components: {
		LoadContracts, IpfsSubmit
	},
    methods: {
        createContract: function() {
            console.log('local web3 is: '+this.localWeb3.version.api);
            console.log('global web3 is: '+BetaWeb3.version);
            var betaWeb3 = new BetaWeb3(this.localWeb3.currentProvider);
            var el = this;
            betaWeb3.eth.getAccounts(function(error, accounts) {
                if (error) {
                    console.log(error);
                    el.message = 'Error: '+ error;
                }
                //get account from provider
                var account = accounts[0];
                //Create IPFS directory
                console.log('user account is '+account);
                el.createIpfs(account);
                //set defaults
                el.contractData[el.contract].defaults({
                    from: account,
                    gas: 2100000,
                    gasPrice: '20000000000'
                });
                el.message = 'Creating the contract...';
                var tempContract = new betaWeb3.eth.Contract(el.contractArtifacts[el.contract].abi );
                tempContract.deploy({ data: el.contractArtifacts[el.contract].bytecode })
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
                    el.message = 'Success! Contract created at address '+instance.contractAddress.toLowerCase()+'.';
                    console.log('Successful contract creation.');
                    el.contractAddr = instance.contractAddress.toLowerCase();
                    el.contractCreated = true;
                    el.$emit('ipfs:contractId', el.contractAddr);
                }).on('error', function(error) {
                    console.log(error.message);
                    el.message = 'Contract Creation Failed!';
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
                    console.log(response);
                    if (response.data.Success) {
                        el.$emit("ipfs:message", "✅ account found");
                    } else {
                        el.$emit("ipfs:message", "❌ - Could not GET create author.");
                    }
                }).catch(function (error) {
                    el.$emit("ipfs:message", "❌  "+error);
                    console.log(error);
                });
            }
        },
        submitIpfs: function(paperDir) {
            var contract = this.contractAddr;
            var el = this;
            this.localWeb3.eth.getAccounts(function(error, accounts) {
                if (error) {
                    console.log(error);
                    el.messageIpfs = 'Error: '+ error;
                }
                var account = accounts[0];
                console.log('user account is '+account);
                el.$emit("ipfs:message", "Uploading paper to IPFS...");
                submitManuscript(account, contract, paperDir).then(function (response) {
                    console.log(response);
                    if (response.data.Success) {
                        el.$emit("ipfs:message", "✅ Loaded Paper to IPFS");
                        el.paperHash = response.data.Hash;
                        el.paperCreated = true;
                        el.messageIpfs = '<b>IPFS link:</b> <a href="http://localhost:8080/ipfs/'+response.data.Hash+'">http://localhost:8080/ipfs/'+response.data.Hash+'</a><br>';
                    } else {
                        el.$emit("ipfs:message", "❌ - Could not GET submit manuscript.");
                    }
                }).catch(function (error) {
                    el.$emit("ipfs:message", "❌  "+error);
                    console.log(error);
                });
            });
        },
		submitContract: function() {
            var paperHash = this.paperHash;
            var contractAddr = this.contractAddr;
            var paperInstance = this.contractData[this.contract].at(contractAddr);
            var el = this;
            this.localWeb3.eth.getAccounts(function(error, accounts) {
                if (error) {
                    console.log(error);
                }
                //get account from provider
                var account = accounts[0];
                //set defaults
                el.contractData[el.contract].defaults({
                    from: account,
                    gas: 200000,
                    gasPrice: 20000000000
                });
                el.messageInit = 'Initializing the contract...';
                paperInstance.initPaper(paperHash).then(function(result) {
                    el.messageInit = 'Success! Your paper has been registered on the blockchain';
                    console.log('Successful submission');
                }).catch(function(err) {
                    el.messageInit = 'paper submission failed!';
                    console.log(err.messageInit);
                });
            });
        }
    }
}
</script>


<style scoped>

</style>
