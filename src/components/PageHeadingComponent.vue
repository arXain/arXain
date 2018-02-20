<template>
<div class="jumbotron">
    <h1 class="text-center" v-html="header"></h1>
</div>
</template>

<script>
    module.exports= {
        name:"PageHeadingComponent",
        props: {title: String},
        data (){
            return {}
        },
        computed: {
            header: function() {
                if (this.title == "paper-submit") {
                    return 'ar&chi;ain Submission Form';
                } else if(this.title == "paper-amend") {
                    return 'ar&chi;ain Revision Form';
                } else if(this.title == "paper-status") {
                    return 'ar&chi;ain Check Blockchain';
                } else if(this.title == "paper-comments") {
                    return 'ar&chi;ain  Submit Comments';
                } else {
                    return 'ar&chi;ain Form';
                }
            }
        }
    }

</script>


<style scoped>
</style
