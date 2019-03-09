import Vue from 'vue'
import Vuex from 'vuex'
import LabService from '../services/LabService'

Vue.use(Vuex)

const store = new Vuex.Store({
    strict: true,
    state: {
        labs: []
    },
    getters: {
        labCount() {

        },
        availableLabs(state, getters) {
            return state.labs.filter(lab => lab.taken === false)
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
        }
    },
    mutations: {
        setLabs(state, labs) {
            state.labs = labs
        }
    }
})

export default store
