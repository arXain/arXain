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
		  <a class="navbar-brand" href="#">ar&chi;ain</a>
		</div>
		<div id="navbar" class="navbar-collapse collapse">
		  <form class="navbar-form navbar-right">
			<div class="form-group">
			  <a class="form-control" href="/submit.html">Submit a paper</a>
			</div>
			<div class="form-group">
			  <a class="form-control" href="/ammend.html">Revise a paper</a>
			</div>
			<div class="form-group">
			  <a class="form-control" href="/status.html">Check blockchain</a>
			</div>
			<div class="form-group">
			  <a class="form-control" href="/comments.html">Comment on a paper</a>
			</div>
			<div class="form-group">
			  <a class="form-control" href="/about.html">About Us</a>
			</div>
		  </form>
		</div><!--/.navbar-collapse -->
	</nav>
</template>

<script>
    module.exports = {
        data(){
            return {}
        }
    }
</script>


<style scoped>

</style>
