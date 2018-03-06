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
        <label>Comment Hash:</label> 
        <input type="text" class='form-control' placeholder="0x0" v-model="commentHash">
    </div>
    <div class="form-group">
        <label>Contract Address:</label> 
        <input type="text" class='form-control' placeholder="0x1" v-model="contractAddr">
    </div>
    <div class="form-group">
        <label> Ratings: </label>
        <div class="form-check form-check-inline">
            <input type="radio" class="form-check-input" name="review" id="choice_0" v-model="picked" value=0> 
            <label class="form-check-label" for="choice_0"> Needs Work </label>
        </div>
        <div class="form-check form-check-inline">
            <input type="radio" class="form-check-input" name="review" id="choice_1" v-model="picked" value=1>
            <label class="form-check-label" for="choice_1"> Acceptable </label>
        </div>
    </div>
    <div class="form-group">
        <button type="submit" class="btn btn-primary btn-submit" @click.prevent="handleComment">Submit Comments</button>
    </div>
    <p><span> {{ message}} </span></p>
    </form>
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
            contract: ['Paper','Comments'],
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
