<template>
    <div>
        Labs list
        <img v-if="labs.length == 0" src='img/spinner.gif'>
        <ul>
            <li 
                v-for='lab in labs' 
                :key='lab.id'
            >
                {{ lab.name }} - {{ lab.taken }}
            </li>
        </ul>
    </div>
</template>

<script>
export default {
    computed: {
        labs() {
            return this.$store.getters.availableLabs
        }
    },
    created() {
        this.$store.dispatch('fetchLabs')
    }
}
</script>

<style>
</style>
