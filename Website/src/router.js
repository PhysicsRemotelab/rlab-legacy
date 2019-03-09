import Vue from 'vue'
import VueRouter from 'vue-router'
import LandingPage from './pages/LandingPage'
import InfoPage from './pages/InfoPage'
import LabsPage from './pages/LabsPage'
import LabPage from './pages/LabPage'
import ResultsPage from './pages/ResultsPage'

Vue.use(VueRouter)

const routes = [
  { 
    path: '/', 
    name: 'landing-page',
    component: LandingPage 
  },
  { 
    path: '/info', 
    name: 'info-page',
    component: InfoPage 
  },
  { 
    path: '/labs', 
    name: 'labs-page',
    component: LabsPage 
  },
  { 
    path: '/results', 
    name: 'results-page',
    component: ResultsPage 
  },
  { 
    path: '/lab/:id', 
    name: 'lab-page',
    component: LabPage,
    props: true
  }
]

const router = new VueRouter({
  mode: 'history',
  routes
})

export default router
