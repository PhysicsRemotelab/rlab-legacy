<template>
    <div>
        <AppHeader />
        <div class="jumbotron">
            <h1 class="display-4">Labor {{ id }} {{ accessToken }}</h1>
            <div v-if='!accessTokenValid'>Labor hõivatud</div>
            <p v-else class="lead">Mõõtmine siin</p>
        </div>
    </div>
</template>

<script>
import AppHeader from '../../components/AppHeader'
import RestService from '../../services/RestService'

var data = {
    accessTokenValid: false
}

export default {
    components: {
        AppHeader
    },
    props: {
        id: {
            type: Number,
            required: true
        },
        accessToken: {
            type: String,
            required: true
        }
    },
    data() {
        return data
    },
    created() {
        var apidata = { 'id': this.$props.id, 'access_token': this.$props.accessToken }
        RestService.accessToken(apidata)
            .then(response => {
                console.log(response.data)
                if(response.data.result === '1') 
                    data.accessTokenValid = true
            })
            .catch(error => {
                console.log('Error:', error.response)
            })
    }
}
</script>

<style>
</style>
