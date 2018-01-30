<!-- amendContract -->
<template>
        <div class="panel panel-default panel-article">
          <div class="panel-heading">
              <h3 class="panel-title"><center>Revise here</center></h3>
          </div>
          <div class="panel-body">
            <center>
            <div class="form-group">
              <strong>Contract Address</strong>: <input type="text" placeholder="0x1" class="amend_contract">
            </div>
            <div class="form-group">
              <strong>DOI</strong>: <input type="text" placeholder="DOI" class="amend_doi">
            </div>
            <div class="form-group">
              <strong>Paper Hash</strong>: <input type="text" placeholder="Revised Paper Hash" class="amend_hash">
            </div>
            <button type="submit" class="btn btn-default btn-submit">Submit</button>
            <br/><br>
            <span style="display: none;" class="success-text">Success!</span>
            </center>
          </div>
        </div>
      </div>
</template>

<script src="../js/app_ammend.js">
</script>


<style scoped>

</style>
