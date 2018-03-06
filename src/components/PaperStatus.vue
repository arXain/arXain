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
          <label>Contract Address:</label> 
          <input type="text" class='form-control' placeholder="0x1" v-model="contractAddr">
        </div>
        <button type="submit" class="btn btn-primary btn-check" @click.prevent="handleCheck">Check Contract</button>
        </form>
        <br>
        <p><span v-html="messagePaper"> </span></p>
        <p> If you forgot the contract address, put in the transaction number that created the contract below:</p>
        <form>
    <div class="form-group">
        <label>Transaction number:</label> 
        <input type="text" class='form-control' placeholder="0x1" v-model="statusTx">
    </div>
    <button type="submit" class="btn btn-primary btn-check" @click.prevent="handleTx">Find Contract</button>
        </form>
        <p><span v-html="messageTx"> </span></p>
        <form>
        <div class="form-group">
          <label>Comment Address:</label> 
          <input type="text" class='form-control' placeholder="0x1" v-model="commentsAddr">
        </div>
        <button type="submit" class="btn btn-primary btn-check" @click.prevent="checkComments">Check Comments</button>
        </form>
        <br>
        <p><span v-html="messageComments"> </span></p>
    </div>
</template>

<script>
import TruffleContract from 'truffle-contract'
import LoadContracts from '../components/LoadContracts.vue'

export default {
    data () {
        return {
            contractAddr: '',
            commentsAddr: '',
            statusTx: '',
            contractData: {},
            contractArtifacts: {},
            contract: ['Paper', 'Comments'],
            messagePaper: '',
            messageTx: '',
            messageComments: ''
        }
    },
    components: { LoadContracts},
    props: ['localWeb3'],
    methods: {
		handleCheck: function() {
            var contractAddr = this.contractAddr;
            if(!contractAddr) {
                this.messagePaper = "No contract address was entered.";
                return;
            }
            console.log('contract address is: '+contractAddr);
            var paperInstance = this.contractData['Paper'].at(contractAddr);
            var el = this;
            console.log('about to call getPaper()');
            paperInstance.getPaper2().then(function(result) {
                console.log(result);
                var hash = result[1];
                var rev = result[2];
                $.getJSON('http://localhost:8080/ipfs/'+hash+'/v'+rev+'/meta.json', function(data) {
                    var time = new Date(data.timestamp);
                    el.messagePaper = (
                    '<b>Title:</b> '+data.title+'<br>'+
                    '<b>Author(s):</b> '+data.authors+'<br>'+
                    '<b>Author Address:</b> '+result[0]+'<br>'+
                    '<b>Abtract:</b> '+data.summary+'<br>'+
                    '<b>Keywords:</b> '+data.keywords+'<br>'+
                    '<b>Revision #:</b> '+rev+'<br>'+
                    '<b>Revision timestamp:</b> '+time.toLocaleString()+'<br>'+
                    '<b>Reviews (Needs work):</b> '+result[3]+'<br>'+
                    '<b>Reviews (Acceptable):</b> '+result[4]+'<br>'+
                    '<b>Comment Address:</b> '+result[5]+'<br>'+
                    '<b>Paper Hash:</b> '+hash+'<br>'+
                    '<b>IPFS link:</b> <a href="http://localhost:8080/ipfs/'+result[1]+'/v'+result[2]+'">http://localhost:8080/ipfs/'+result[1]+'/v'+result[2]+'</a><br>'
                    );
                    console.log('Successful check');
                });
            }).catch(function(err) {
                el.messagePaper = 'paper3 check failed!';
                console.log(err.message);
            });
        },
		checkComments: function() {
            var contractAddr = this.commentsAddr;
            if(!contractAddr) {
                this.messageComments = "No contract address was entered.";
                return;
            }
            console.log('comments address is: '+contractAddr);
            var paperInstance = this.contractData['Comments'].at(contractAddr);
            var el = this;
            console.log('about to call getStatus()');
            paperInstance.getStatus().then(function(result) {
                console.log(result);
                console.log('Successful check');
            }).catch(function(err) {
                el.messageComments = 'comments check failed!';
                console.log(err.message);
            });
        },
		handleTx: function() {
            var tx = this.statusTx;
            console.log('transaction address is: '+tx);
            var el = this;
            this.localWeb3.eth.getTransactionReceipt(tx, function(error, result) {
                if(error) {
                    console.log(error);
                    el.messageTx = 'Failed. Could not access transaction.';
                }
                else {
                    var contractAddr = result['contractAddress'];
                    console.log('got contract address from tx.');
                    el.messageTx = 'The contract address is '+contractAddr;
                }
            });
        }
    }
}
</script>


<style scoped>

</style>
