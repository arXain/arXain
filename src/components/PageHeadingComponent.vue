<template>
<div class="jumbotron">
    <h1 class="text-center" v-html="title"></h1>
</div>
</template>

<script>
    module.exports= {
        name:"PageHeadingComponent",
        props: {title: String},
        data (){
            return {}
        }
    }

</script>


<style scoped>
</style
