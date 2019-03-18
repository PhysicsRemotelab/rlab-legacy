import Vue from 'vue'
import VueRouter from 'vue-router'
import LandingPage from './pages/LandingPage'
import MeasurementsPage from './pages/MeasurementsPage'
import LabsPage from './pages/LabsPage'
import LabPage from './pages/LabPage'
import PageNotFound from './pages/PageNotFound'

Vue.use(VueRouter)

const routes = [
  { 
    path: '/', 
    name: 'landing-page',
    component: LandingPage 
  },
  { 
    path: '/labs', 
    name: 'labs-page',
    component: LabsPage 
  },
  {
    path: '/labs/:id',
    name: 'lab-page',
    component: LabPage,
    props: true
  },
  {
    path: '/measurements', 
    name: 'measurements-page',
    component: MeasurementsPage 
  },
  { 
    path: '*', 
    component: PageNotFound
  }
]

const router = new VueRouter({
  mode: 'history',
  routes,
  linkExactActiveClass: 'active'
})

export default router
