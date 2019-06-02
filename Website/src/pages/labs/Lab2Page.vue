<template>
    <div>
        <AppHeader />
        <div class="jumbotron">
            <div class="container">
                <div class="row">
                    <div class="col-sm-10">
                        <h1 class="display-4">Labor {{ id }} {{ lab.name }}</h1>
                    </div>
                    <div class="col-sm-2">
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
                            <img id='webcam2' class="card-img-top" :src=WEBCAM2_SERVICE>
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
                            <button v-if='!updatingGraph' class="btn btn-raised btn-success" @click='startInterval'>Joonista graafik</button>
                            <button v-else class="btn btn-raised btn-danger" @click='stopInterval'>Peata graafik</button>
                            <button class="btn btn-raised btn-success" @click='saveResult'>Salvesta andmebaasi</button>
                        </div>
                    </div>
                </div>
                <div class="col-sm-12 p-2">
                    <div class="card h-100">
                        <div class="card-body">
                            <h5 class="card-title">Graafik</h5>
                            <div id="chart"></div>
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
import { range } from '../../helpers/range'
import Chart from 'chart.js'
import ApexCharts from 'apexcharts'
import { WEBCAM2_SERVICE } from '../../constants'


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
            time: 0,
            WEBCAM2_SERVICE,
            updatingGraph: false,
            chart: null,
            graphData: {},
            accessToken: window.localStorage.getItem('access_token')
        }
    },
    created() {
        var apidata = { 'id': this.$props.id, 'access_token': this.accessToken }
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
        saveResult: function() {
            var csvData = []
            for(var i = 0; i < this.graphData.length; i++) {
                var obj = this.graphData[i]
                csvData.push([obj.x, obj.y])
            }
            csvData = csvData.join('\n')
            
            var apidata = { 'lab_id': this.$props.id, 'access_token': this.accessToken, 'results': csvData }
            RestService.postMeasurementsAPI(apidata)
            .then(response => {
                console.log(response.data)
            })
            .catch(error => {
                console.log('Error:', error.response)
            })
        },
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
        startInterval: function() {
            var data = []
            var options = getOptions(data)
            this.chart = new ApexCharts(document.querySelector("#chart"), options)

            const self = this
            
            this.interval = setInterval(self.drawApexGraph, 2000)
            this.updatingGraph = true
        },
        stopInterval: function() {
            clearInterval(this.interval)
            this.updatingGraph = false
        },
        drawGraph: function() {
            // 1. Get image location
            var output = document.getElementById('webcam2')
            var img = new Image()
            img.crossOrigin = 'Anonymous';
            img.src = output.src
            
            // 2. Create in memory canvas for image parsing
            var context = document.createElement('canvas').getContext('2d')
            context.drawImage(img, 0, 0)

            // 3. Define initial values
            var xc = 160
            var yc = 120
            var rvals = range(30, 80, 1)
            var phivals = range(0, 2 * Math.PI, 1 * Math.PI / 180)

            var rmeans = new Array(rvals.length).fill(0)
            var pxvals = 0
            // 4. Iterate over radius values
            for (var i = 0; i < rvals.length; i++) {
                // 5. Iterate over angle values
                for (var j = 0; j < phivals.length; j++) {
                    // 6. Calculate (x,y) pixel values
                    var xr = Math.round(rvals[i] * Math.sin(phivals[j]) + xc)
                    var yr = Math.round(rvals[i] * Math.cos(phivals[j]) + yc)
                    // 7. Find color value from image
                    var px = context.getImageData(xr, yr, 1, 1).data[0]
                    pxvals += px
                }
                // 8. Calculate average color value on radius
                rmeans[i] = pxvals / phivals.length
                pxvals = 0
            }
            // 9. Prepare data for graph
            var graphData = new Array(rvals.length).fill(0)
            for (var k = 0; k < rvals.length; k++) {
                graphData[k] = { x: rvals[k], y: rmeans[k] }
            }
            this.graphData = graphData



        },
        drawApexGraph: function() {

            
        }
    }
}


function getOptions(data) {
    var options = {
        chart: {
            height: 255,
            type: 'line',
            animations: {
                enabled: true,
                easing: 'linear',
                dynamicAnimation: {
                    speed: 1000
                }
            },
            toolbar: {
                show: false
            },
            zoom: {
                enabled: false
            }
            },
            dataLabels: {
                enabled: false
            },
            stroke: {
                curve: 'smooth'
            },
            series: [{
                data: data
            }],
            title: {
                text: 'Dynamic Updating Chart',
                align: 'left'
            },
            markers: {
                size: 0
            },
            xaxis: {
                min: 0,
                max: 50
            },
            yaxis: {
                min: 0,
                max: 255
            },
            legend: {
                show: false
            },
        }
    return options
}


</script>

<style>
</style>
