<template>
    <div>
        <AppHeader />
        <div class="jumbotron">
            <h1 class="display-4">Labor {{ id }} - {{ lab.name }}</h1>
            <p class="lead">Mõõtmine siin</p>
        </div>
    </div>
</template>

<script>
import AppHeader from '../../components/AppHeader'
import RestService from '../../services/RestService'

export default {
    components: {
        AppHeader
    },
    props: {
        id: {
            type: Number,
            required: true
        },
        confirmed: {
            type: Boolean,
            default: false
        }
    },
    data() {
        return {
            
        }
    },
    computed: {
        lab() {
            return this.$store.getters.getLab
        }
    },
    created() {
        this.$store.dispatch('fetchLab', { id: this.id })
    },
    beforeRouteLeave(to, from, next) {
        if (this.confirmed) {
            this.$store.dispatch('updateLabAvailable', this.lab)
            next()
        } else {
            if (confirm('Soovid katkestada?')) {
                this.$store.dispatch('updateLabAvailable', this.lab)
                next()
            } else {
                next(false)
            }
        }
    }
}
</script>

<style>
</style>
