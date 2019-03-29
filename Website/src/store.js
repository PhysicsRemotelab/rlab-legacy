import Vue from 'vue'
import Vuex from 'vuex'
import RestService from './services/RestService'

Vue.use(Vuex)

const store = new Vuex.Store({
    strict: true,
    state: {
        labs: [],
        measurements: [],
        lab: []
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
        }
    }
})

export default store
