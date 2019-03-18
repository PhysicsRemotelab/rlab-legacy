<template>
    <div class="row">
        <LabListItem v-for='lab in labs' :key='lab.id' :lab='lab' />
    </div>
</template>

<script>
import LabListItem from './LabListItem'

export default {
    components: {
        LabListItem
    },
    computed: {
        labs() {
            return this.$store.getters.getLabs
        }
    },
    created() {
        this.$store.dispatch('fetchLabs')
    }
}
</script>

<style>
</style>
