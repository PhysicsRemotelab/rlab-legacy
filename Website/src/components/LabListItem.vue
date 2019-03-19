<template>
    <div class="col-sm-6 p-1">
        <div class="card">
            <div class="card-body">
                <h5 class="card-title">{{ lab.name }}</h5>
                <p class="card-text"> {{ lab.description }}</p>
            </div>
            <router-link v-if='!lab.taken' :to="{ name: lab.seo, params: { id: lab.id }}" tag='button' class="btn btn-raised btn-success">Alusta</router-link>
            <button v-else class="btn btn-raised btn-danger" disabled>Hõivatud</button>
        </div>
    </div>
</template>

<script>
export default {
    props: {
        lab: {
            type: Object,
            required: true
        }
    }
}
</script>

<style>
</style>
