<!-- submitContract -->
<template>
<div class="panel panel-default panel-article">
  <div class="panel-heading">
	  <h3 class="panel-title"><center>Submit here</center></h3>
  </div>
  <div class="panel-body">
	<center>
	<div class="form-group" id="hash-form">
	  <strong>Paper Hash</strong>: <input type="text" placeholder="Paper Hash" class="submit_hash">
	</div>
	<div class="form-group" id="doi-form">
	  <strong>DOI</strong>: <input type="text" placeholder="DOI" class="submit_doi">
	</div>
	<div class="form-group" id="tx-form">
	  <strong>TX Address</strong>: <input type="text" placeholder="Leave empty for now" class="submit_tx">
	</div>
	<button type="submit" class="btn btn-default btn-create">Create Contract</button>
	<button type="submit"  class="btn btn-default btn-submit">Submit Paper</button>
	<br><br>
	<span style="display: none;" class="success-text">Success!</span><br>
	<span style="display: none;" class="failure-text">Failed to submit paper!</span><br>
	</center>
  </div>
</div>
</div>
</template>

<script src="../js/app_submit.js">
</script>


<style scoped>

</style>
