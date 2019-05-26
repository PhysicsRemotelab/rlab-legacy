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
            <div v-if='!accessTokenValid'>Labor hõivatud</div>
            <div v-else class="row">
                <div class="col-sm-8 p-2">
                    <div class="card h-100">
                        <div class="card-body">
                            <h5 class="card-title">Kaamera</h5>
                        </div>
                    </div>
                </div>
                <div class="col-sm-4 p-2">
                    <div class="card h-100">
                        <div class="card-body">
                            <h5 class="card-title">Algandmed</h5>
                            <countdown :time="time" :interval="100" tag="p">
                                <template v-if='time != 0' slot-scope="props">Lõpetamiseni jäänud：{{ props.hours }} h {{ props.minutes }} m {{ props.seconds }}.{{ Math.floor(props.milliseconds / 100) }} s.</template>
                            </countdown>
                            <button class="btn btn-raised btn-success" @click='startSpectrometer'>Käivita spektromeeter</button>
                        </div>
                    </div>
                </div>
                <div class="col-sm-12 p-2">
                    <div class="card h-100">
                        <div class="card-body">
                            <h5 class="card-title">Spektromeeter</h5>
                            <canvas id="myChart" width="200" height="100"></canvas>
                        </div>
                    </div>
                </div>
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
import Chart from 'chart.js';
import { SPECTROMETER_SERVICE } from '../../constants'

var data = {
    accessTokenValid: false,
    lab: {},
    time: 0
}

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
        return data
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
        },
        startSpectrometer: function() {
            var ws = new WebSocket(SPECTROMETER_SERVICE)
            var chart = buildChart()
            ws.onmessage = function (event) {
                var resp = JSON.parse(event.data)
                console.log(resp.data)
                chart.data.datasets[0].data = resp.data
                chart.update()
            }
        }
    }
}

function buildChart() {
    var ctx = document.getElementById('myChart').getContext('2d');
    var chart = new Chart(ctx, {
        type: 'scatter',
        data: {
            labels: [''],
            datasets: [
                {
                    data: data.spectrometerData
                }
            ]
        },
        options: {
            legend: {
                display: false
            },
            showLines: true,
            animation: {
                duration: 0 // general animation time
            },
            hover: {
                animationDuration: 0 // duration of animations when hovering an item
            },
            responsiveAnimationDuration: 0,
            elements: {
                line: {
                    tension: 0 // disables bezier curves
                }
            },
            scales: {
                xAxes: [{
                    display: true,
                    ticks: {
                        min: 350,
                        max: 900,
                        stepSize: 50
                    }
                }],
                yAxes: [{
                    display: true,
                    ticks: {
                        min: 0,
                        max: 100,
                        stepSize: 10
                    }
                }]
            }
        }
    });
    return chart
}
</script>

<style>
</style>
