import VueRouter from 'vue-router'
import LandingPage from './pages/LandingPage'
import InfoPage from './pages/InfoPage'
import LabsPage from './pages/LabsPage'
import ResultsPage from './pages/ResultsPage'

const routes = [
  { path: '/', component: LandingPage },
  { path: '/info', component: InfoPage },
  { path: '/labs', component: LabsPage },
  { path: '/results', component: ResultsPage }
]

const router = new VueRouter({
  mode: 'history',
  routes
})

export default router
