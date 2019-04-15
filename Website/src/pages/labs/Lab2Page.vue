<template>
    <div>
        <AppHeader />
        <div class="jumbotron">
            <h1 class="display-4">Labor {{ $route.params.id }}</h1>
            <p class="lead">Spektromeeter</p>
            <div class="row">
                <div class="col-sm-4 p-2">
                    <div class="card h-100">
                        <div class="card-body">
                            <h5 class="card-title">Kaamera</h5>
                        </div>
                    </div>
                </div>
                <div class="col-sm-4 p-2">
                    <div class="card h-100">
                        <div class="card-body">
                            <h5 class="card-title">Graafik</h5>
                            <button type="submit" class="btn btn-outline-success" @click='begin'>Start</button>
                        </div>
                    </div>
                </div>
                <div class="col-sm-4 p-2">
                    <div class="card h-100">
                        <div class="card-body">
                            <h5 class="card-title">Salvesta</h5>
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

var data = {
    spectrometerData: []
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
            const socket = io('http://localhost:4600')
            socket.emit('start_spectrometer', '')
            socket.on('spectrometer', function (data2, msg) {
                console.log('got')
                console.log(data2)
            })
        }
    }
}
</script>

<style>
</style>
