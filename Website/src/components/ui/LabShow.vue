<template>
    <div>
        {{ lab.name }}
    </div>
</template>

<script>
import LabService from '../services/LabService'

export default {
    props: [{
        name: id,
        type: Object
    }],
    data() {
        return {
            lab: {}
        }
    },
    created() {
        LabService.getLab(this.id)
            .then(response => {
                this.labs = response.data
            })
            .catch(error => {
                console.log('Error:', error.response)
            })
    }
}
</script>

<style>
</style>
