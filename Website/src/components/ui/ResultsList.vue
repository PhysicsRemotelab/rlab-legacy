<template>
    <div>
        <v-toolbar flat color="white">
            <v-toolbar-title>Mõõtmistulemused</v-toolbar-title>
        </v-toolbar>
         <v-data-table :headers="headers" :items="measurements" class="elevation-1">
            <template v-slot:items="props">
                <td>{{ props.item.created }}</td>
                <td>{{ props.item.lab_id.name }}</td>
                <td>{{ props.item.results }}</td>
            </template>
        </v-data-table>
    </div>
</template>

<script>
export default {
    data() {
        return {
            headers: [
                {
                    text: 'Mõõdetud',
                    sortable: true,
                    value: 'created'
                },
                {
                    text: 'Labor',
                    sortable: true,
                    value: 'lab_id.name'
                },
                {
                    text: 'Mõõtmistulemused',
                    sortable: false,
                    value: 'results'
                }
            ]
        }
    },
    computed: {
        measurements() {
            return this.$store.getters.getMeasurements
        }
    },
    created() {
        this.$store.dispatch('fetchMeasurements')
    }
}
</script>

<style>
.disable-events {
  pointer-events: none
}
</style>
