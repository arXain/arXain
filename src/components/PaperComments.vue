<template>
<div>
    <load-contracts
        :localWeb3='localWeb3'
        :load='contract'
        @update:contractData="value => contractData = value"
        @update:contractArtifacts="value => contractArtifacts = value">
    </load-contracts>
    <div class="form-group">
    <strong>Comment Hash</strong>: <input type="text" placeholder="(be constructive!)" v-model="commentHash">
    <br><br>
    <strong>Contract Address</strong>: <input type="text" placeholder="0x1" v-model="contractAddr">
    </div>
    <div class="form-group">
    <strong>Rating</strong>:
    <input type="radio" name="review" id="choice_0" v-model="picked" value=0> Needs Work 
    <input type="radio" name="review" id="choice_1" v-model="picked" value=1> Acceptable
    <br>
    </div>
    <br>
    <button type="submit" class="btn btn-default btn-submit" @click.prevent="handleComment">Submit Comments</button>
    <br><br>
    <p><span> {{ message}} </span></p>
</div>
</template>

<script>
import LoadContracts from '../components/LoadContracts.vue'

export default {
    data () {
        return {
            commentHash: '',
            contractAddr: '',
            picked: 999,
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
		handleComment: function() {
            var commentHash = this.commentHash;
            var contractAddr = this.contractAddr;
            var review = this.picked;
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
                el.message = 'Submiting the comment...';
                paperInstance.reviewPaper(commentHash, contractAddr, review).then(function(result) {
                    el.message = 'Success! Your comment has been registered on the blockchain.';
                    console.log('Successful submission');
                }).catch(function(err) {
                    el.message = 'Comment submission failed!';
                    console.log(err.message);
                });
            });
        }
    }
}
</script>


<style scoped>

</style>
