<template>
    <div>
        <AppHeader />
        <div class="jumbotron">
            <h1 class="display-4">Labor {{ $route.params.id }}</h1>
            <p class="lead">Mõõtmine siin</p>
        </div>
    </div>
</template>

<script>
import AppHeader from '../../components/AppHeader'

export default {
    components: {
        AppHeader
    }
}
</script>

<style>
</style>
