<template>
<div>
    <form>
        <div class="form-group">
            <button type="submit" class="btn btn-primary btn-submit" :disabled="contractInitialized" v-on:click.prevent="submitIpfs(fileDir)">Submit Paper</button>
        </div>
        <p><span v-html="messageInit"></span></p>
        <div class="form-group">
           <label for="contract">Paper Hash:</label>
            <div class="input-group mb-3">
                <input type="text" :disabled="true" class="form-control" placeholder="Submit the contract to get the Paper Hash" v-model="paperHash">
                <div class="input-group-append">
                    <button class="btn btn-outline-secondary" type="button" v-clipboard:copy="paperHash">Copy</button>
                </div>
            </div>
        </div>
        <p><span v-html="messageIpfs"></span></p>
		<div class="form-group">
			<label for="contract">Contract Address:</label>
			<div class="input-group mb-3">
				<input type="text" class="form-control" :disabled="true" placeholder="0x0" v-model="contract">
				<div class="input-group-append">
					<button class="btn btn-outline-secondary" type="button" v-clipboard:copy="contract">Copy</button>
				</div>
			</div>
		</div>
		<div class="form-group">
			<label for="contract">Comments Address:</label>
			<div class="input-group mb-3">
				<input type="text" class="form-control" :disabled="true" v-model="comments">
				<div class="input-group-append">
					<button class="btn btn-outline-secondary" type="button" v-clipboard:copy="comments">Copy</button>
				</div>
			</div>
		</div>
    </form>
</div>
</template>

<script>
import {  submitManuscript } from '../js/ipfs-helper.js'

export default {
    data () {
        return {
            paperHash: '',
            paperCreated: false,
            contractInitialized: false,
			messageIpfs: '',
            messageInit: ''
        }
    },
    props: ['localWeb3','contractData','contract','comments','fileDir'],
    methods: {
	  submitIpfs: function(paperDir) {
		var contract = this.contract;
		var el = this;
		this.localWeb3.eth.getAccounts(function(error, accounts) {
			if (error) {
				console.log(error);
				el.$emit("submit:message", 'Error: '+ error);
			}
			var account = accounts[0];
			console.log('user account is '+account);
			el.$emit("ipfs:message", "Uploading paper to IPFS...");
			submitManuscript(account, contract, paperDir).then(function (response) {
				if (response.data.Success) {
					el.$emit("ipfs:message", "✅  Loaded Paper to IPFS");
					el.paperHash = response.data.Hash;
                    el.paperCreated = true;
					el.messageIpfs = '<b>IPFS link:</b> <a href="http://localhost:8080/ipfs/'+response.data.Hash+'">http://localhost:8080/ipfs/'+response.data.Hash+'</a><br>';
                    el.submitContract(el, account);
				} else {
					el.$emit("ipfs:message", "❌: "+response.data.Message);
				}
			}).catch(function (error) {
				el.$emit("ipfs:message", "❌   "+error);
				console.log(error);
			});
		});
      },
		submitContract: function(el, account) {
            var paperHash = el.paperHash;
            var contractAddr = el.contract;
            var commentsAddr = el.comments;
            var paperInstance = el.contractData['Paper'].at(contractAddr);
            el.contractData['Paper'].defaults({
                from: account,
                gas: 200000,
                gasPrice: 20000000000
            });
            el.messageInit = 'Initializing the contract...';
            paperInstance.initPaper(paperHash, commentsAddr).then(function(result) {
                el.messageInit = 'Success! Your paper has been registered on the blockchain';
                console.log('Successful submission');
                el.contractInitialized = true;
            }).catch(function(err) {
                el.messageInit = 'paper submission failed!';
                console.log(err.messageInit);
            });
        }
    },
}
</script>


<style scoped>

</style>
