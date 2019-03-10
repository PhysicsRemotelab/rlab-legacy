import Vue from 'vue'
import VueRouter from 'vue-router'
import LandingPage from './pages/LandingPage'
import ManualPage from './pages/ManualPage'
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
    path: '/manual', 
    name: 'manual-page',
    component: ManualPage 
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
