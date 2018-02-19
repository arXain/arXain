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
          <input type="text" class='form-control' placeholder="0x1" v-model="statusAddr">
        </div>
        <button type="submit" class="btn btn-primary btn-check" @click.prevent="handleCheck">Check Contract</button>
        </form>
        <br>
        <p> If you forgot the contract address, put in the transaction number from MetaMask that created the contract to retrieve the contract address below:</p>
        <form>
    <div class="form-group">
        <label>Transaction number:</label> 
        <input type="text" class='form-control' placeholder="0x1" v-model="statusTx">
    </div>
    <button type="submit" class="btn btn-primary btn-check" @click.prevent="handleTx">Find Contract</button>
    <p><span v-html="message"> </span></p>
        </form>
    </div>
</template>

<script>
import TruffleContract from 'truffle-contract'
import LoadContracts from '../components/LoadContracts.vue'

export default {
    data () {
        return {
            statusAddr: '',
            statusTx: '',
            contracts: {},
            contractArtifacts: {},
            contract: 'Paper',
            message: ''
        }
    },
    components: { LoadContracts},
    props: ['localWeb3'],
    methods: {
		handleCheck: function() {
            var contractAddr = this.statusAddr;
            console.log('contract address is: '+contractAddr);
            var paperInstance = this.contractData[this.contract].at(contractAddr);
            var el = this;
            paperInstance.getPaper().then(function(result) {
                el.message = ('<b>Author:</b> '+result[0]+'<br>'+
                '<b>Paper Hash:</b> '+result[1]+'<br>'+
                '<b>Revision #:</b> '+result[2]+'<br>'+
                '<b>Reviews (Needs work):</b> '+result[3]+'<br>'+
                '<b>Reviews (Acceptable):</b> '+result[4]+'<br>'+
                '<b>IPFS link:</b> <a href="http://localhost:8080/ipfs/'+result[1]+'">http://localhost:8080/ipfs/'+result[1]+'</a><br>'
                );
                console.log('Successful check');
            }).catch(function(err) {
                el.message = 'paper check failed!';
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
                    el.message = 'Failed. Could not access transaction.';
                }
                else {
                    var contractAddr = result['contractAddress'];
                    console.log('got contract address from tx.');
                    el.message = 'The contract address is '+contractAddr;
                }
            });
        }
    }
}
</script>


<style scoped>

</style>
