<template>
    <div>
        <AppHeader />
        <div class="jumbotron">
            <LabList />
        </div>
    </div>
</template>

<script>
import AppHeader from '../components/AppHeader'
import LabList from '../components/LabList'

export default {
    components: {
        AppHeader,
        LabList
    }
}
</script>

<style>

</style>
