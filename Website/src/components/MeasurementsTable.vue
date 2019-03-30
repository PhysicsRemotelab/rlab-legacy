<template>
    <div>
        <table class="table table-hover">
            <thead>
                <tr>
                    <th scope="col">#</th>
                    <th scope="col">Labor</th>
                    <th scope="col">Tulemus</th>
                    <th scope="col">Mõõdetud</th>
                    <th scope="col">Kustuta</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for='m in measurements' :key='m.id'>
                    <th scope="row">{{ m.id }}</th>
                    <td>{{ m.lab_id.name }}</td>
                    <td>{{ m.results }}</td>
                    <td>{{ m.created }}</td>
                    <td><button class="btn btn-danger" @click='deleteMeasurement(m.id)'>Kustuta</button></td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<script>
export default {
    computed: {
        measurements() {
            return this.$store.getters.getMeasurements
        }
    },
    created() {
        this.$store.dispatch('fetchMeasurements')
    },
    methods: {
        deleteMeasurement: function(id) {
            this.$store.dispatch('deleteMeasurement', id)
        }
    }
}
</script>

<style>
</style>
