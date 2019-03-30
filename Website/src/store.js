import Vue from 'vue'
import Vuex from 'vuex'
import RestService from './services/RestService'

Vue.use(Vuex)

const store = new Vuex.Store({
    strict: true,
    state: {
        labs: [],
        measurements: [],
        lab: [],
        lab_taken: []
    },
    getters: {
        getLabs(state, getters) {
            return state.labs
        },
        getMeasurements(state, getters) {
            return state.measurements
        },
        getLab(state, getters) {
            return state.lab
        }
    },
    actions: {
        fetchLabs({ commit }) {
            RestService.getLabsAPI()
                .then(response => {
                    commit('setLabs', response.data)
                })
                .catch(error => {
                    console.log('Error:', error.response)
                })
        },
        fetchMeasurements({ commit }) {
            RestService.getMeasurementsAPI()
                .then(response => {
                    commit('setMeasurements', response.data)
                })
                .catch(error => {
                    console.log('Error:', error.response)
                })
        },
        fetchLab(context, data) {
            RestService.getLabAPI(data.id)
                .then(res => {
                    context.commit('setLab', res.data)
                    context.commit('setLabTaken', res.data)
                })
                .catch(error => {
                    console.log('Error:', error.response)
                })
        },
        updateLab(context, data) {
            RestService.updateLabAPI(data)
                .then(res => {
                    // console.log('Update success: ', res)
                })
                .catch(error => {
                    console.log('Error:', error.response)
                })
        },
        updateLabAvailable(context, data) {
            context.commit('setLabAvailable', data)
        },
        deleteMeasurement(context, data) {
            context.commit('setDeleteMeasurement', data)
            RestService.deleteMeasurementAPI(data)
                .then(res => {
                    console.log('Delete success: ', res)
                })
                .catch(error => {
                    console.log('Error:', error.response)
                })
        }
    },
    mutations: {
        setLabs(state, data) {
            state.labs = data
        },
        setMeasurements(state, data) {
            state.measurements = data
        },
        setLab(state, data) {
            state.lab = data
        },
        setLabTaken(state, data) {
            state.lab_taken = data
            state.lab_taken.taken = true
            this.dispatch('updateLab', state.lab_taken)
        },
        setLabAvailable(state, data) {
            state.lab_taken = data
            state.lab_taken.taken = false
            this.dispatch('updateLab', state.lab_taken)
        },
        setDeleteMeasurement(state, data) {
            var arrayId = state.measurements.findIndex(x => x.id === data)
            state.measurements.splice(arrayId, 1)
        }
    }
})

export default store
