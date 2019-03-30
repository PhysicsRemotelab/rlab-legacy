<template>
    <div>
        <AppHeader />
        <div class="jumbotron">
            <h1 class="display-4">Labor {{ id }} - {{ lab.name }}</h1>
            <hr class="my-4">
            <div class="row">
                <div class="col-sm-4 p-2">
                    <CameraCard url='http://localhost:4000/video_feed' />
                </div>
                <div class="col-sm-4 p-2">
                    <div class="card h-100">
                        <div class="card-body">
                            <h5 class="card-title">Algandmed</h5>
                            <div class="form-group">
                                <label for="measurementsCount">Mõõtmiste arv</label>
                                <select id="measurementsCount" v-model='measurementsCount' class="form-control">
                                    <option>1</option>
                                    <option>2</option>
                                    <option>3</option>
                                    <option>4</option>
                                    <option>5</option>
                                </select>
                            </div>
                            <div class="form-group row">
                                <div class="col-sm-10">
                                    <button type="submit" class="btn btn-outline-success" :disabled='beginButtonDisabled' @click='begin'>Alusta</button>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="col-sm-4 p-2">
                    <div class="card h-100">
                        <div class="card-body">
                            <h5 class="card-title">Tulemused</h5>
                            <table class="table">
                                <thead>
                                    <tr>
                                        <th scope="col">Nr</th>
                                        <th scope="col">Tulemus</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr v-for='m in measurements' :key='m.id'>
                                        <th scope="row">{{ m.id }}</th>
                                        <td>{{ m.dist }}</td>
                                    </tr>
                                </tbody>
                            </table>
                            <div class="col-sm-10">
                                <button type="submit" class="btn btn-outline-success" :disabled='saveButtonDisabled' @click='save'>{{ saveButtonName }}</button>
                            </div>
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
import CameraCard from '../../components/CameraCard'
import io from 'socket.io-client'

var data = {
    measurementsCount: 3,
    measurements: [],
    beginButtonDisabled: false,
    saveButtonDisabled: true,
    saveButtonName: 'Salvesta andmebaasi'
}

export default {
    components: {
        AppHeader,
        CameraCard
    },
    props: {
        id: {
            type: Number,
            required: true
        },
        confirmed: {
            type: Boolean,
            default: false
        }
    },
    data() {
        return data
    },
    computed: {
        lab() {
            return this.$store.getters.getLab
        }
    },
    created() {
        this.$store.dispatch('fetchLab', { id: this.id })
    },
    beforeRouteLeave(to, from, next) {
        if (this.confirmed) {
            this.$store.dispatch('updateLabAvailable', this.lab)
            next()
        } else {
            if (confirm('Soovid katkestada?')) {
                this.$store.dispatch('updateLabAvailable', this.lab)
                next()
            } else {
                next(false)
            }
        }
    },
    methods: {
        begin: function() {
            const socket = io('http://localhost:4500')
            console.log(this.measurementsCount)
            socket.emit('start_measurement', JSON.stringify({count:this.measurementsCount}))
            data.measurements = []
            data.beginButtonDisabled = true
            socket.on('sensor', function (data2, msg) {
                data.measurements.push(data2)
                console.log(data)
            })
            socket.on('finished', function (data2, msg) {
                console.log('finished')
                data.beginButtonDisabled = false
                data.saveButtonDisabled = false
                data.saveButtonName = 'Salvesta andmebaasi'
            })
        },
        save: function() {
            const formData = {
                lab_id: this.lab.id,
                user_id: 1,
                results: data.measurements
            }
            RestService.postMeasurementsAPI(formData)
                .then(res => {
                    console.log(res)
                    data.saveButtonDisabled = true
                    data.saveButtonName = 'Salvestatud'
                })
                .catch(error => console.log(error))
        }
    }
}
</script>

<style>
</style>
