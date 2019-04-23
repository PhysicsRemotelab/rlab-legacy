import Vue from 'vue'
import VueRouter from 'vue-router'
import LandingPage from './pages/LandingPage'
import PageNotFound from './pages/PageNotFound'

import MeasurementsPage from './pages/MeasurementsPage'
import LabsPage from './pages/LabsPage'
import Lab1Page from './pages/labs/Lab1Page'
import Lab2Page from './pages/labs/Lab2Page'
import Lab3Page from './pages/labs/Lab3Page'

Vue.use(VueRouter)

const routes = [
  { 
    path: '/', 
    name: 'landing-page',
    component: LandingPage 
  },
  {
    path: '/measurements', 
    name: 'measurements-page',
    component: MeasurementsPage 
  },
  { 
    path: '/labs', 
    name: 'labs-page',
    component: LabsPage
  },
  {
    path: '/lab1',
    name: 'lab-page-1',
    component: Lab1Page,
    props: { id: 1 }
  },
  {
    path: '/lab2',
    name: 'lab-page-2',
    component: Lab2Page,
    props: { id: 2 }
  },
  {
    path: '/lab3',
    name: 'lab-page-3',
    component: Lab3Page,
    props: (route) => ({ id: 3, accessToken: route.query.access })
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
