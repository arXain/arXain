<template>
<div>
    <load-contracts
        :localWeb3='localWeb3'
        :load='contracts'
        @update:contractData="value => contractData = value"
        @update:contractArtifacts="value => contractArtifacts = value">
    </load-contracts>
    <div v-if='isCreate'>
        <create-contract
            :localWeb3='localWeb3'
            :contractData='contractData'
            :contractArtifacts='contractArtifacts'
            @create:contractId='value => setContract(value)'
            @create:commentsId='value => meta.comments = value'
            @create:submitterId='value => meta.submitter = value'
            @ipfs:message="value => dispatchIpfs(value)"
            @create:goToIpfs='goToIpfs()'>
        </create-contract>
    </div>
    <div v-else-if='isIpfs'>
        <h4> Step 3. Enter details.</h4>
		<div class="form-group">
            <span>
                If you have a JSON of the metdata, upload it here:
                <label class="btn btn-outline-secondary"> Browse 
                <input type="file" hidden @change="uploadMeta($event.target.files);">
                </label>
                {{ metajson }}
            </span>
		</div>
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
        	<button type="submit" class="btn btn-primary btn-create" :disabled="!fileUploaded" v-on:click.prevent="goToSubmit()">Next</button>
		</div>
    </div>
    <div v-else-if='isSubmit'>
        <h4> Step 4. Submit paper to IPFS and the blockchain.</h4>
		<submit-contract
            :localWeb3='localWeb3'
            :contractData='contractData'
            :contract='meta.contract'
            :comments='meta.comments'
            :fileDir='fileDir'
            @ipfs:message="value => dispatchIpfs(value)">
        </submit-contract>
    </div>
</div>
</template>

<script>
import BetaWeb3 from 'web3'
import LoadContracts from '../components/LoadContracts.vue'
import CreateContract from '../components/CreateContract.vue'
import IpfsSubmit from '../components/IpfsSubmit.vue'
import SubmitContract from '../components/SubmitContract.vue'

const ACTIVE_CREATE = 1, ACTIVE_IPFS = 2, ACTIVE_SUBMIT = 3;

export default {
    data () {
        return {
            currentView: ACTIVE_CREATE,
            contracts: ['Paper','Comments'],
            fileUploaded: '',
            fileDir: '',
            metajson: '',
            meta: {
                contract: '',
                comments: '',
                submitter: '',
                title: '',
                authors: [],
                summary: '',
                timestamp: '',
                keywords: [],
                version: ''
            },
            contractData: {},
            contractArtifacts: {}
        }
    },
    props: ['localWeb3'],
	components: {
		LoadContracts, CreateContract, IpfsSubmit, SubmitContract
	},
    methods: {
        goToIpfs: function() {
            this.currentView = ACTIVE_IPFS;
        },
        goToSubmit: function() {
            this.currentView = ACTIVE_SUBMIT;
        },
        setContract: function(contractAddr) {
            this.meta.contract = contractAddr;
            this.meta.version = '1';
            var time = new Date();
            this.meta.timestamp = time;
        },
        uploadMeta: function(file) {
            if (!file.length) return;
            this.metajson = 'Loaded '+file[0].name;
            //parse the data
            var fr = new FileReader();
            var el = this;
            fr.onload = function(e) { 
                var result = JSON.parse(e.target.result);
                el.meta.title = result.title;
                el.meta.authors = result.authors;
                el.meta.keywords = result.keywords;
                el.meta.summary = result.summary;
            }
            fr.readAsText(file[0]);
        },
        dispatchIpfs: function(message) {
            this.$emit("ipfs:message", message);
        }
    },
    computed: {
        isCreate() {
            return this.currentView === ACTIVE_CREATE;
        },
        isIpfs() {
            return this.currentView === ACTIVE_IPFS;
        },
        isSubmit() {
            return this.currentView === ACTIVE_SUBMIT;
        },
    }

}
</script>


<style scoped>

</style>
