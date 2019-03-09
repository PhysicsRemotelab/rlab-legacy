<template>
    <div>
        <AppHeader />
        Labs page
        <LabList />
        <AppFooter />
    </div>
</template>

<script>
import AppHeader from '../components/layout/AppHeader'
import AppFooter from '../components/layout/AppFooter'
import LabService from '../services/LabService'
import LabList from '../components/ui/LabList'

export default {
    components: {
        AppHeader,
        AppFooter,
        LabList
    }
}
</script>

<style>
</style>
