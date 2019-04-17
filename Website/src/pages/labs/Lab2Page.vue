<template>
    <div>
        <AppHeader />
        <div class="jumbotron">
            <h1 class="display-4">Labor {{ $route.params.id }}</h1>
            <p class="lead">Spektromeeter</p>
            <div class="row">
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
                            <div class="form-group">
                                <label for="samples">Mõõtmiste arv</label>
                                <select id="samples" v-model='samples' class="form-control">
                                    <option>10</option>
                                    <option>20</option>
                                    <option>30</option>
                                    <option>40</option>
                                    <option>50</option>
                                </select>
                            </div>
                            <div class="form-group">
                                <label for="interval">Aeg mõõtmiste vahel</label>
                                <select id="interval" v-model='interval' class="form-control">
                                    <option>1</option>
                                    <option>2</option>
                                    <option>3</option>
                                    <option>4</option>
                                    <option>5</option>
                                </select>
                            </div>
                            <button type="submit" class="btn btn-outline-success" @click='begin'>Start</button>
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
import io from 'socket.io-client'
import Chart from 'chart.js';

var data = {
    spectrometerData: [],
    samples: 10,
    interval: 2
}

function setChartData(chart, label, data) {
    chart.data.datasets[0].data = data
    chart.update();
}


export default {
    components: {
        AppHeader
    },
    data() {
        return data
    },
    methods: {
        begin: function() {
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
                                min: 0,
                                max: 287,
                                stepSize: 50
                            }
                        }],
                        yAxes: [{
                            display: true,
                            ticks: {
                                min: 0,
                                max: 1100,
                                stepSize: 100
                            }
                        }]
                    }
                }
            });
            const socket = io('http://localhost:4600')
            socket.emit('start_spectrometer', JSON.stringify({'samples':data.samples,'interval':data.interval}))
            socket.on('spectrometer', function (d, msg) {
                data.spectrometerData = d.data
                setChartData(chart, '', data.spectrometerData)
            })
            socket.on('finished', function (d, msg) {
                console.log('finished')
                socket.close()
            })

        }
    }
}
</script>

<style>
</style>
