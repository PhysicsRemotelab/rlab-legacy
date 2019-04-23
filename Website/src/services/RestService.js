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
    getLabsAPI() {
        return apiClient.get('/labs/')
    },
    getLabAPI(id) {
        return apiClient.get('/labs/' + id)
    },
    getMeasurementsAPI() {
        return apiClient.get('/measurements/')
    },
    updateLabAPI(data) {
        return apiClient.put('/labs/', data)
    },
    postMeasurementsAPI(data) {
        return apiClient.post('/measurements/', data)
    },
    deleteMeasurementAPI(id) {
        return apiClient.delete('/measurements/' + id)
    },
    accessToken(data) {
        return apiClient.post('/check_token/', data)
    }
}
