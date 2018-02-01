<template>
<div class="jumbotron">
    <h1 class="text-center">{{title}}</h1>
</div>
</template>

<script>
    module.exports= {
        name:"PageHeadingComponent",
        //props: ['title'],
        props: {title: String},
        data (){
            return {}
        }
    }

</script>


<style scoped>
</style
