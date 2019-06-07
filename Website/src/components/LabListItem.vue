<template>
    <div class="col-sm-4 p-1">
        <div class="card h-100">
            <div class="card-body">
                <h5 class="card-title">{{ lab.id }}. {{ lab.name }}</h5>
                <p class="card-text"> {{ lab.description }}</p>
            </div>
            <div class="card-footer text-muted h-100">
                <countdown :time="time" :interval="100" tag="p">
                    <template v-if='time != 0 && lab.taken' slot-scope="props">Lõpetamiseni jäänud：{{ props.hours }} h {{ props.minutes }} m {{ props.seconds }}.{{ Math.floor(props.milliseconds / 100) }} s.</template>
                </countdown>
            </div>
            <router-link v-if='!lab.taken' :to="{ name: 'lab-page-' + lab.id, params: { id: lab.id }}" tag='button' class="btn btn-raised btn-success">Alusta</router-link>
            <button v-if='lab.taken && lab.access_token != access' class="btn btn-raised btn-danger" disabled>Hõivatud</button>
            <router-link v-if='lab.taken && lab.access_token == access' :to="{ name: 'lab-page-' + lab.id, params: { id: lab.id }}" tag='button' class="btn btn-raised btn-info">Jätka</router-link>
        </div>
    </div>
</template>

<script>
import VueCountdown from '@chenfengyuan/vue-countdown'
import {  getRemainingTime } from '../helpers/helpers'

const uuidv1 = require('uuid/v1')
let accessToken = window.localStorage.getItem('access_token')
if (accessToken === null) {
    accessToken = uuidv1()
    window.localStorage.setItem('access_token', accessToken)
}

export default {
    components: {
        'countdown': VueCountdown
    },
    props: {
        lab: {
            type: Object,
            required: true
        }
    },
    data() {
        return {
          time : getRemainingTime(this.lab.updated),
          access: accessToken
        }
    }
}
</script>

<style>
</style>
