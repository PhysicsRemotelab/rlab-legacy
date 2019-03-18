<template>
    <div class="col-sm-6">
        <div class="card">
            <div class="card-body">
                <h5 class="card-title">{{ lab.name }}</h5>
                <p class="card-text"> {{ lab.description }}</p>
                <router-link :to="{ name: 'lab-page', params: { id: lab.id }}" class="btn btn-success">Alusta</router-link>
            </div>
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
