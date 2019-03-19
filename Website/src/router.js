import Vue from 'vue'
import VueRouter from 'vue-router'
import LandingPage from './pages/LandingPage'
import MeasurementsPage from './pages/MeasurementsPage'
import LabsPage from './pages/LabsPage'
import PageNotFound from './pages/PageNotFound'
import Lab1Page from './pages/labs/Lab1Page'
import Lab2Page from './pages/labs/Lab2Page'
import Lab3Page from './pages/labs/Lab3Page'
import Lab4Page from './pages/labs/Lab4Page'

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
    path: '/measurements', 
    name: 'measurements-page',
    component: MeasurementsPage 
  },
  {
    path: '/labs/:id',
    name: 'lab1-page',
    component: Lab1Page,
    params: true
  },
  {
    path: '/labs/:id',
    name: 'lab2-page',
    component: Lab2Page,
    params: true
  },
  {
    path: '/labs/:id',
    name: 'lab3-page',
    component: Lab3Page,
    params: true
  },
  {
    path: '/labs/:id',
    name: 'lab4-page',
    component: Lab4Page,
    params: true
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
