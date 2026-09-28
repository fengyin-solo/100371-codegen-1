import { createRouter, createWebHistory } from 'vue-router'

import Dashboard from '@/views/Dashboard.vue'
const Tower = () => import('@/views/tower/index.vue')
const Grid = () => import('@/views/grid/index.vue')
const Hotspot = () => import('@/views/hotspot/index.vue')
const Brigade = () => import('@/views/brigade/index.vue')
const Supply = () => import('@/views/supply/index.vue')
const Heli = () => import('@/views/heli/index.vue')
const Fireline = () => import('@/views/fireline/index.vue')
const Fireweather = () => import('@/views/fireweather/index.vue')
const Drone = () => import('@/views/drone/index.vue')
const Road = () => import('@/views/road/index.vue')
const Checkpoint = () => import('@/views/checkpoint/index.vue')
const Publicity = () => import('@/views/publicity/index.vue')
const Burntarea = () => import('@/views/burntarea/index.vue')
const Review = () => import('@/views/review/index.vue')
const Fireperiod = () => import('@/views/fireperiod/index.vue')
const Drill = () => import('@/views/drill/index.vue')
const Duty = () => import('@/views/duty/index.vue')
const Danger = () => import('@/views/danger/index.vue')

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', name: 'dashboard', component: Dashboard },
    { path: '/tower', name: 'tower', component: Tower },
    { path: '/grid', name: 'grid', component: Grid },
    { path: '/hotspot', name: 'hotspot', component: Hotspot },
    { path: '/brigade', name: 'brigade', component: Brigade },
    { path: '/supply', name: 'supply', component: Supply },
    { path: '/heli', name: 'heli', component: Heli },
    { path: '/fireline', name: 'fireline', component: Fireline },
    { path: '/fireweather', name: 'fireweather', component: Fireweather },
    { path: '/drone', name: 'drone', component: Drone },
    { path: '/road', name: 'road', component: Road },
    { path: '/checkpoint', name: 'checkpoint', component: Checkpoint },
    { path: '/publicity', name: 'publicity', component: Publicity },
    { path: '/burntarea', name: 'burntarea', component: Burntarea },
    { path: '/review', name: 'review', component: Review },
    { path: '/fireperiod', name: 'fireperiod', component: Fireperiod },
    { path: '/drill', name: 'drill', component: Drill },
    { path: '/duty', name: 'duty', component: Duty },
    { path: '/danger', name: 'danger', component: Danger },
  ],
})

export default router
