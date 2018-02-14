<!-- Navbar Component -->
<template>
	<nav class="navbar navbar-inverse">
		<div class="navbar-header">
		  <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">
			<span class="sr-only">Toggle navigation</span>
			<span class="icon-bar"></span>
			<span class="icon-bar"></span>
			<span class="icon-bar"></span>
		  </button>
		  <a class="navbar-brand" href="/index.html">ar&chi;ain</a>
		  <a class="navbar-brand" href="/about.html">About Us</a>
		</div>
		<div id="navbar" class="navbar-collapse collapse">
		  <form class="navbar-form navbar-right">
			<div class="form-group">
			  <a class="form-control" 
                  @click="changeView('paper-submit','ar&chi;ain Submission Form','Submit here')" 
                  href="#">Submit a paper
              </a>
			</div>
			<div class="form-group">
			  <a class="form-control" 
                  @click="changeView('paper-amend','ar&chi;ain Revision Form','Revise here')" 
                  href="#">Revise a paper
              </a>
			</div>
			<div class="form-group">
			  <a class="form-control" 
                 @click="changeView('paper-status','ar&chi;ain Check Blockchain','Check contract state on the blockchain')" 
                 href="#">Check blockchain
              </a>
			</div>
			<div class="form-group">
			  <a class="form-control" 
                @click="changeView('paper-comments','ar&chi;ain Submit Comments','Submit comments here')"  
                href="#">Comment on a paper
              </a>
			</div>
		  </form>
		</div><!--/.navbar-collapse -->
	</nav>
</template>

<script>
    module.exports = {
        data(){
            return {}
        },
        methods: {
            changeView: function(newView, newHeader, newSubtitle) {
                this.$emit('update:header',newHeader);
                this.$emit('update:view',newView);
                this.$emit('update:sub',newSubtitle);
            }
        }
    }
</script>


<style scoped>

</style>
