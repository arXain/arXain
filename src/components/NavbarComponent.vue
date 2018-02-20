<!-- Navbar Component -->
<template>
	<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
        <div class ="container">
        <a class="navbar-brand" href="/index.html">ar&chi;ain</a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarResponsive" aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse justify-content-end" id="navbarResponsive">
            <ul class="navbar-nav nav-fill">
			<li class="nav-item">
                <a class="nav-link" v-bind:class="{active: isSubmit}" 
                  @click="changeView('paper-submit', 0)" 
                  href="#">Submit a paper
              </a>
			</li>
			<li class="nav-item">
                <a class="nav-link" v-bind:class=" {active: isRevise} " 
                  @click="changeView('paper-amend', 1);" 
                  href="#">Revise a paper
              </a>
			</li>
			<li class="nav-item">
                <a class="nav-link" v-bind:class=" {active: isCheck} " 
                 @click="changeView('paper-status', 2)" 
                 href="#">Check blockchain
              </a>
			</li>
			<li class="nav-item">
                <a class="nav-link" v-bind:class=" {active: isComment} " 
                @click="changeView('paper-comments', 3)"  
                href="#">Comment on a paper
              </a>
			</li>
            </ul>
		</div><!--/.navbar-collapse -->
        </div>
	</nav>
</template>

<script>
    const ACTIVE_SUBMIT = 0, ACTIVE_REVISE = 1, ACTIVE_CHECK = 2, ACTIVE_COMMENT = 3;

    module.exports = {
        data(){
            return {
                currentActive: ACTIVE_SUBMIT
            }
        },
        methods: {
            changeView: function(newView, newIsActive) {
                this.$emit('update:view',newView);
                this.currentActive = newIsActive;
            }
        },
        computed: {
            isSubmit() {
                return this.currentActive === ACTIVE_SUBMIT;
            },
            isRevise() {
                return this.currentActive === ACTIVE_REVISE;
            },
            isCheck() {
                return this.currentActive === ACTIVE_CHECK;
            },
            isComment() {
                return this.currentActive === ACTIVE_COMMENT;
            },
        }
    }
</script>


<style scoped>

</style>
