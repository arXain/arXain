<!-- commentsContract -->
<template>
        <div class="panel panel-default panel-article">
          <div class="panel-heading">
              <h3 class="panel-title"><center>Submit comments here</center></h3>
          </div>
          <div class="panel-body">
            <center>
            <div class="form-group">
              <strong>Comment Hash</strong>: <input type="text" placeholder="(be constructive!)" class="comment_hash">
            </div>
            <div class="form-group">
              <strong>DOI</strong>: <input type="text" placeholder="paper DOI" class="comment_doi">
            </div>
            <div class="form-group">
              <strong>Contract Address</strong>: <input type="text" placeholder="0x1" class="contract_hash">
            </div>
            <div class="form-group">
                <strong>Rating</strong>:
                <input type="radio" name="review" id="choice_no" onclick="check(this.value)" value=0> Needs Work <input type="radio" name="review" id="choice_yes" onclick="check(this.value)" value=1> Acceptable<br>
            </div>
            <br>
            <button type="submit" class="btn btn-default btn-submit">Submit Comments</button>
            <br/><br>
            <span style="display: none;" class="results-text">Stuff!</span>
            </center>
          </div>
        </div>
      </div>
</template>

<script src="../js/app_comments.js">
</script>


<style scoped>

</style>
