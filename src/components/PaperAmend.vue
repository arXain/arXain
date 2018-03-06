<!-- amendContract -->
<template>
<div>
    <load-contracts
        :localWeb3='localWeb3'
        :load='contract'
        @update:contractData="value => contractData = value"
        @update:contractArtifacts="value => contractArtifacts = value">
    </load-contracts>
    <div v-if='isLoad'>
        <h4> Step 1. Load the original contract.</h4>
        <form>
            <div class="form-group">
               <label for="contract">Contract Address:</label>
                <div class="input-group mb-3">
                    <input type="text" class="form-control" placeholder="Contract Address" v-model="contractAddr">
                </div>
            </div>
            <div class="form-group">
                <button type="submit" class="btn btn-primary btn-create" v-on:click.prevent="loadContract">Load Paper Contract</button>
            </div>
            <p><span v-html="loadMessage"></span></p>
        </form>
        <h4> Step 2. Edit details of the paper.</h4>
       <ipfs-submit
            :localWeb3='localWeb3'
            :contract='meta.contract'
            :comments='meta.comments'
            :submitter='meta.submitter'
            :version='meta.version'
            :timestamp='meta.timestamp'
            :title.sync='meta.title'
            :summary.sync='meta.summary'
            :authors='meta.authors'
            @update:authors='value => meta.authors.push(value)'
            @delete:authors='value => {var i = meta.authors.indexOf(value); meta.authors.splice(i,1);}'
            :keywords='meta.keywords'
            @update:keywords='value => meta.keywords.push(value)'
            @delete:keywords='value => {var i = meta.keywords.indexOf(value); meta.keywords.splice(i,1);}'
            @ipfs:resetPaper="value => fileUploaded = false"
            @ipfs:fileDir="value => {fileDir = value; fileUploaded = true}">
       </ipfs-submit>
       <div class="form-group">
           <button type="submit" class="btn btn-primary btn-create" :disabled="(!contractLoaded || !fileUploaded)" v-on:click.prevent="goToAmend()">Next</button>
       </div>
     </div>
     <div v-else-if='isAmend'>
        <h4> Step 3. Send revised paper to IPFS and the blockchain.</h4>
        <revise-contract
            :localWeb3='localWeb3'
            :contractData='contractData'
            :contract='meta.contract'
            :comments='meta.comments'
            :fileDir='fileDir'
            @ipfs:message="value => dispatchIpfs(value)">
        </revise-contract>
    </div>
</div>
</template>

<script>
import LoadContracts from '../components/LoadContracts.vue'
import IpfsSubmit from '../components/IpfsSubmit.vue'
import ReviseContract from '../components/ReviseContract.vue'

const ACTIVE_LOAD = 1, ACTIVE_AMEND = 2;

export default {
    data () {
        return {
            currentView: ACTIVE_LOAD,
            contractAddr: '',
			contractLoaded: false,
            loadMessage: '',
            fileDir: '',
			fileUploaded: false,
            contract: ['Paper','Comments'],
            contractData: {},
            contractArtifacts: {},
            meta: {
                contract: '',
                comments: '',
                submitter: '',
                title: '',
                authors: [],
                keywords: [],
                summary: '',
                timestamp: '',
                version: ''
            }
        }
    },
    props: ['localWeb3'],
	components: {
		LoadContracts, IpfsSubmit, ReviseContract
	},
    methods: {
        goToAmend: function() {
            this.currentView = ACTIVE_AMEND;
        },
        dispatchIpfs: function(message) {
            this.$emit("ipfs:message", message);
        },
        loadContract: function() {
            var contractAddr = this.contractAddr;
            if(!contractAddr) {
                this.loadMessage = "No contract address was entered.";
                return;
            }
            //run getPaper(), and get hash and version number
            var paperInstance = this.contractData['Paper'].at(contractAddr);
            var el = this;
            paperInstance.getPaper2().then(function(result) {
                var hash = result[1];
                var rev = result[2];
                //load meta.json from the hash location
                $.getJSON('http://localhost:8080/ipfs/'+hash+'/v'+rev+'/meta.json', function(data) { 
                    el.meta = data;
                    var time = new Date();
                    el.meta.timestamp = time;
                    el.meta.version = parseInt(rev)+1;
                    console.log('revision will be '+el.meta.version);
                    el.loadMessage = "Successfully loaded contract details.";
                    el.contractLoaded = true;
                });
            });
            //return an initial set of variables to propagate to submitIpfs
        }
    },
    computed: {
        isLoad() {
            return this.currentView === ACTIVE_LOAD;
        },
        isAmend() {
            return this.currentView === ACTIVE_AMEND;
        },
    }
}
</script>


<style scoped>

</style>
