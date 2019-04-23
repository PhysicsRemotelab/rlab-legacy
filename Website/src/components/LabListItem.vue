<template>
    <div class="col-sm-4 p-1">
        <div class="card">
            <div class="card-body">
                <h5 class="card-title">{{ lab.name }}</h5>
                <p class="card-text"> {{ lab.description }}</p>
            </div>
            <router-link v-if='!lab.taken' :to="{ name: 'lab-page-' + lab.id, params: { id: lab.id }, query: { access: access }}" tag='button' class="btn btn-raised btn-success">Alusta</router-link>
            <button v-else class="btn btn-raised btn-danger" disabled>Hõivatud</button>
        </div>
    </div>
</template>

<script>
const uuidv1 = require('uuid/v1');

var data = {
    access: uuidv1()
}

export default {
    props: {
        lab: {
            type: Object,
            required: true
        }
    },
    data() {
        return data
    }
}
</script>

<style>
</style>
