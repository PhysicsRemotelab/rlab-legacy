<template>
    <div>
        <AppHeader />
        <div class="jumbotron">
            <h1 class="display-4">Labor {{ id }}</h1>
            <p class="lead">Mõõtmine siin</p>
        </div>
    </div>
</template>

<script>
import AppHeader from '../../components/AppHeader'
import axios from 'axios'

export default {
    components: {
        AppHeader
    },
    props: {
        id: {
            type: Number,
            required: true
        }
    },
    data() {
        return {
            
        }
    },
    created() {
        axios.get('http://127.0.0.1:5000/labs/' + this.id)
            .then(res => console.log(res))
            .catch(error => console.log(error))
    }
}
</script>

<style>
</style>
