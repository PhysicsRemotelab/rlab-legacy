import axios from 'axios'
import { REST_SERVICE } from '../constants'

const apiClient = axios.create({
    baseURL: REST_SERVICE,
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
    },
    freeLab(data) {
        return apiClient.post('/free_lab/', data)
    }
}
