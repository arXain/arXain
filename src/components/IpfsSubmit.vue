<template>
<div>
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
    <div class="form-group">
        <label> Title: </label>
        <input type="text" class='form-control' maxlength="1000"  v-model="sync_title"> 
    </div>
    <div class="form-group">
        <label> Author(s): </label>
        <input type="text" class="form-control" placeholder="Press enter to add authors" v-model="newauthor" @keyup.enter="addItem('authors', newauthor)">
        <br>
        <div class="form-inline">
                <keywords-list v-for="item in authors" 
                :item="item" :key="item.id" @delete:item="val => deleteItem('authors',val)"></keywords-list>
        </div>
    </div>
    <div class="form-group">
        <label>Keywords:</label>
        <input type="text" class="form-control" placeholder="Press enter to add keyword" v-model="newkey" @keyup.enter="addItem('keywords', newkey)">
        <br>
        <div class="form-inline">
                <keywords-list v-for="item in keywords" 
                :item="item" :key="item.id" @delete:item="val => deleteItem('keywords',val)"></keywords-list>
        </div>
    </div>
    <div class="form-group">
        <label> Abstract: </label>
        <textarea type="text" class='form-control' v-model="sync_summary"> </textarea>
    </div>
	<div class="form-group">
        <label> Upload PDF </label>
        <div class="input-group input-file">
          <input type="file" class="custom-file-input" id="inputGroupFile01" @change="fileChange($event.target.files);">
          <label class="custom-file-label" for="inputGroupFile01"> {{pdfTitle}} </label>
        </div>
	</div>
    <div class="form-group">
            <button type="submit" :disabled="isSaving||isSuccess" @click.prevent="fileSave();" class="btn btn-primary">Upload files</button>
            <p v-if="isSaving"> Uploading...</p>
        <!--SUCCESS-->
        <div v-if="isSuccess">
            <br>
            <p><strong>Uploaded {{ uploadedFile[0].name }} and metadata successfully.</strong></p>
            <p><a href="javascript:void(0)" @click="reset()">Upload a Different paper</a></p>
        </div>
        <!--FAILED-->
        <div v-if="isFailed">
            <br>
            <p><strong>Upload failed.</strong></p>
            <p><a href="javascript:void(0)" @click="reset()">Try Again</a></p>
            <pre>{{ uploadError }}</pre>
        </div>
    </div>
</div>
</template>

<script>
  import { upload, submitManuscript } from '../js/ipfs-helper.js';
  import KeywordsList from '../components/KeywordsList.vue';

  const STATUS_INITIAL = 0, STATUS_SAVING = 1, STATUS_SUCCESS = 2, STATUS_FAILED = 3;

  export default {
    props: ['localWeb3','contract','comments','submitter','title',
            'authors','summary','keywords','timestamp','version'],
    components: { KeywordsList },
    data() {
      return {
        newkey: '',
        newauthor: '',
        uploadedFile: [],
        uploadError: null,
        currentStatus: null
      }
    },
    computed: {
      sync_title: {
          get() { return this.title },
          set(val) { this.$emit('update:title', val) }
      },
      sync_summary: {
          get() { return this.summary },
          set(val) { this.$emit('update:summary', val) }
      },
      pdfTitle() {
          if (!this.uploadedFile.length) {
              return 'Choose a file';
          } else {
              return this.uploadedFile[0].name;
          }
      },
      isInitial() {
        return this.currentStatus === STATUS_INITIAL;
      },
      isSaving() {
        return this.currentStatus === STATUS_SAVING;
      },
      isSuccess() {
        return this.currentStatus === STATUS_SUCCESS;
      },
      isFailed() {
        return this.currentStatus === STATUS_FAILED;
      }
    },
    methods: {
	  reset() {
		// reset form to initial state
		this.currentStatus = STATUS_INITIAL;
		this.uploadedFile = [];
		this.uploadError = null;
		this.$emit('ipfs:resetPaper');
	  },
      addItem(cat, value) {
          if (value.trim()) {
              this.$emit('update:'+cat, value);
          }
          if(cat === "authors") {
              this.newauthor = '';
          } 
          else if(cat === "keywords") {
              this.newkey = '';
          }
      },
      deleteItem(cat,item) {
          if (item.trim()) {
              this.$emit('delete:'+cat, item);
          }
      },
	  save(formData) {
		// upload data to the server
		this.currentStatus = STATUS_SAVING;

		upload(formData)
		  .then(x => {
			  //data = x.data();
			  console.log('result data is:');
			  console.log(x.data);
			  if(x.data.Success == true) {
			this.currentStatus = STATUS_SUCCESS;
			this.$emit("ipfs:fileDir", x.data.fileDirectory);
			  } else {
			this.uploadError = 'Failed to upload paper.';
			this.currentStatus = STATUS_FAILED;
			  }
		  })
		  .catch(err => {
			this.uploadError = err.response;
			this.currentStatus = STATUS_FAILED;
		  });
	  },
	  fileSave() {
		// package the data for transfer
		const formData = new FormData();
		var metadata = {
			title: this.title,
			authors: this.authors,
			summary: this.summary,
            keywords: this.keywords,
			contract: this.contract,
			comments: this.comments,
			submitter: this.submitter,
            timestamp: this.timestamp,
            revision: this.version
		};
		if (!this.uploadedFile.length) return;
		formData.append('paper', this.uploadedFile[0], this.uploadedFile[0].name);
		formData.append('meta', JSON.stringify(metadata));

		// save it
		this.save(formData);
	  },
	  fileChange: function(file) {
		  if (!file.length) return;
		  this.uploadedFile = file;
	  },
    },
    mounted() {
      this.reset();
    },
  }

</script>


<style scoped>
</style>
