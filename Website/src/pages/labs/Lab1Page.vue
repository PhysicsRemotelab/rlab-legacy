<template>
    <div>
        <AppHeader />
        <div class="jumbotron">
            <div class="container">
                <div class="row">
                    <div class="col-sm-11">
                        <h1 class="display-4">Labor {{ id }} {{ lab.name }}</h1>
                    </div>
                    <div class="col-sm-1">
                        <button class="btn btn-raised btn-danger" @click='markFree'>Lõpeta</button>
                    </div>
                </div>
            </div>
            <div class="container">
                <countdown :time="time" :interval="100" tag="p">
                    <template v-if='time != 0' slot-scope="props">Lõpetamiseni jäänud：{{ props.hours }} h {{ props.minutes }} m {{ props.seconds }}.{{ Math.floor(props.milliseconds / 100) }} s.</template>
                </countdown>
                <div v-if='!accessTokenValid'>Labor hõivatud</div>
                <p v-else class="lead">Mõõtmine siin</p>
            </div>
        </div>
    </div>
</template>

<script>
import AppHeader from '../../components/AppHeader'
import RestService from '../../services/RestService'
import io from 'socket.io-client'
import { getRemainingTime } from '../../helpers/helpers'
import VueCountdown from '@chenfengyuan/vue-countdown'

export default {
    components: {
        AppHeader,
        'countdown': VueCountdown
    },
    props: {
        id: {
            type: Number,
            required: true
        }
    },
    data() {
        return {
            accessTokenValid: false,
            lab: {},
            time: 0
        }
    },
    created() {
        const accessToken = window.localStorage.getItem('access_token')
        var apidata = { 'id': this.$props.id, 'access_token': accessToken }
        RestService.accessToken(apidata)
            .then(response => {
                console.log(response.data)
                if(response.data.result === '1') {
                    this.accessTokenValid = true
                }
                this.lab = response.data.lab
                var time = getRemainingTime(this.lab.updated)
                this.time = time
            })
            .catch(error => {
                console.log('Error:', error.response)
            })
    },
    methods: {
        markFree: function() {
            const accessToken = window.localStorage.getItem('access_token')
            var apidata = { 'id': this.$props.id, 'access_token': accessToken }
            RestService.freeLab(apidata)
            .then(response => {
                console.log(response.data)
                this.$router.push('labs')
            })
            .catch(error => {
                console.log('Error:', error.response)
            })
        }
    }
}
</script>

<style>
</style>
