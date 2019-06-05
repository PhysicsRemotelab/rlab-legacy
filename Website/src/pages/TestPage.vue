<template>
    <div>
        <AppHeader />
        <div class="jumbotron">
            <h1 class="display-4">Test here</h1>
            <button @click='click'>Click</button>
        </div>
    </div>
</template>

<script>
import AppHeader from '../components/AppHeader'
import { range } from '../helpers/range'

export default {
    components: {
        AppHeader
    },
    methods: {
        click: function() {
            console.log('clicked')
        }
    }
}
</script>

<style>
</style>
