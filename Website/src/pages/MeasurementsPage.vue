<template>
    <div>
        <AppHeader />
        <div class="jumbotron">
            <h1 class="display-4">Mõõtmistulemused</h1>
            <MeasurementsTable />
        </div>
    </div>
</template>

<script>
import AppHeader from '../components/AppHeader'
import MeasurementsTable from '../components/MeasurementsTable'

export default {
    components: {
        AppHeader,
        MeasurementsTable
    }
}
</script>

<style>
</style>
