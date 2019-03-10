import axios from 'axios'

const apiClient = axios.create({
    baseURL: 'http://127.0.0.1:5000',
    withCredentials: false,
    headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }
})

export default {
    getLabs() {
        return apiClient.get('/labs/')
    },
    getLab(id) {
        return apiClient.get('/labs/' + id)
    },
    getMeasurements() {
        return apiClient.get('/measurements/')
    }
}
