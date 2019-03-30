<template>
    <div class="card h-100">
        <img class="card-img-top" :src=url>
        <div class="card-body">
            <p class="card-text">Kaamera</p>
        </div>
    </div>
</template>

<script>
export default {
    props: {
        url: {
            type: String,
            required: true
        }
    }
}
</script>

<style>
</style>
