<template>
    <div>
        <AppHeader />
        <div class="jumbotron">
            <h1 class="display-4">Esileht</h1>
            <p class="lead">Kaugjuhtivuslabori veebisait.</p>
            <button @click='onSubmit'>submit</button>
        </div>
    </div>
</template>

<script>
import AppHeader from '../components/AppHeader'
import axios from 'axios'

export default {
    components: {
        AppHeader
    },
    data: function() {
        return {
            lab_id: '1',
            user_id: '1',
            results: '{3,2,2}'
        }
    },
    computed: {

    },
    watch: {

    },
    methods: {
        onSubmit() {
            const formData = {
                lab_id: this.lab_id,
                user_id: this.user_id,
                results: this.results
            }
            axios.post('http://127.0.0.1:5000/measurements/', formData)
                .then(res => console.log(res))
                .catch(error => console.log(error))
        }
    }
}
</script>

<style>
</style>
