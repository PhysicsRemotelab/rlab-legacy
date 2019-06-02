<template>
    <div>
        <table class="table table-hover text-center">
            <thead>
                <tr>
                    <th scope="col">#</th>
                    <th scope="col">Labor</th>
                    <th scope="col">Mõõdetud</th>
                    <th scope="col">Mõõtmistulemused</th>
                    <th scope="col">Kustuta</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for='m in measurements' :key='m.id'>
                    <th scope="row">{{ m.id }}</th>
                    <td>{{ m.lab_id.name }}</td>
                    <td>{{ m.created }}</td>
                    <td><button class="btn btn-info" @click='downloadCSV(m.results)'>Lae alla</button></td>
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
        },
        downloadCSV: function(results) {
            const csvFile = new Blob([results], { type: 'text/csv' })

            const downloadLink =  document.createElement('a')
            downloadLink.download = `data.csv`
            downloadLink.href = window.URL.createObjectURL(csvFile)
            downloadLink.style.display = 'none'
            document.body.appendChild(downloadLink)
            downloadLink.click()
            document.body.removeChild(downloadLink)
        }
    }
}
</script>

<style>
</style>
