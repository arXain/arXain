<template>
<div>
    <div class="form-group">
        <label for="upload"> Upload PDF to IPFS: </label>
        <form enctype="multipart/form-data" novalidate v-if="isInitial || isSaving">
                <input type="file" :name="uploadFieldName" :disabled="isSaving" @change="filesChange($event.target.name, $event.target.files);" class="input-file">
                <p v-if="isSaving"> Uploading PDF...</p>
        </form>
        <!--SUCCESS-->
        <div v-if="isSuccess">
            <p><strong>Uploaded  {{ uploadedFiles[0] }} successfully.</strong></p>
            <p><a href="javascript:void(0)" @click="reset()">Upload a Different paper</a></p>
        </div>
        <!--FAILED-->
        <div v-if="isFailed">
            <p><strong>Upload failed.</strong></p>
            <p><a href="javascript:void(0)" @click="reset()">Try again</a></p>
            <pre>{{ uploadError }}</pre>
        </div>
    </div>
</div>
</template>

<script>
  import { upload } from '../js/ipfs-helper.js';

  const STATUS_INITIAL = 0, STATUS_SAVING = 1, STATUS_SUCCESS = 2, STATUS_FAILED = 3;

  export default {
    data() {
      return {
        uploadedFiles: [],
        uploadError: null,
        currentStatus: null,
        uploadFieldName: 'paper'
      }
    },
    computed: {
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
        this.uploadedFiles = [];
        this.uploadError = null;
        this.$emit('ipfs:resetPaper');
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
            this.uploadedFiles = [].concat(x.data.fileName);
            this.currentStatus = STATUS_SUCCESS;
            this.$emit('ipfs:fileDir', x.data.fileDirectory);
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
      filesChange(fieldName, fileList) {
        // handle file changes
        const formData = new FormData();

        if (!fileList.length) return;

        formData.append(fieldName, fileList[0], fileList[0].name);

        // save it
        this.save(formData);
      }
    },
    mounted() {
      this.reset();
    },
  }

</script>


<style scoped>
</style>
