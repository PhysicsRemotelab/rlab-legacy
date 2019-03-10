import Vue from 'vue'
import Vuex from 'vuex'
import LabService from '../services/LabService'

Vue.use(Vuex)

const store = new Vuex.Store({
    strict: true,
    state: {
        labs: [],
        measurements: []
    },
    getters: {
        labCount() {

        },
        availableLabs(state, getters) {
            return state.labs.filter(lab => lab.taken === false)
        },
        unavailableLabs(state, getters) {
            return state.labs.filter(lab => lab.taken === true)
        },
        getLabs(state, getters) {
            return state.labs
        },
        getMeasurements(state, getters) {
            return state.measurements
        }
    },
    actions: {
        fetchLabs({ commit }) {
            LabService.getLabs()
            .then(response => {
                commit('setLabs', response.data)
            })
            .catch(error => {
                console.log('Error:', error.response)
            })
        },
        fetchMeasurements({ commit }) {
            LabService.getMeasurements()
            .then(response => {
                commit('setMeasurements', response.data)
            })
            .catch(error => {
                console.log('Error:', error.response)
            })
        }
    },
    mutations: {
        setLabs(state, labs) {
            state.labs = labs
        },
        setMeasurements(state, measurements) {
            state.measurements = measurements
        }
    }
})

export default store
