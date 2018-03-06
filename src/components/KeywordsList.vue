<template>
<div class="input-group col-auto">
    <span class="form-control">
        {{item}}
    </span>
    <div class="input-group-append">
        <button class="btn btn-outline-secondary" @click="deleteItem">x</button>
    </div>
</div>
</template>

<script>

export default {
    props: ['item'],
    data() {
        return {
        }
    },
	methods: {
        deleteItem: function() {
            this.$emit("delete:item",this.item);
        }
	}
}
</script>


<style scoped>
</style>
