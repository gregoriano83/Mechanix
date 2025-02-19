import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import SignUp from '../views/SignUp.vue'
import LogIn from '../views/LogIn.vue'

import Orders from '../views/dashboard/Orders.vue'
import Order from '../views/dashboard/Order.vue'
import EditOrder from '../views/dashboard/EditOrder.vue'
import AddOrder from '../views/dashboard/AddOrder.vue'

import Client from '@/views/dashboard/Client.vue'
import ShowClient from '@/views/dashboard/ShowClient.vue'
import EditClient from '@/views/dashboard/EditClient.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/sign-up',
    name: 'SignUp',
    component: SignUp
  },
  {
    path: '/log-in',
    name: 'LogIn',
    component: LogIn
  },
  {
    path: '/dashboard/orders',
    name: 'Orders',
    component: Orders,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/dashboard/orders/:id',
    name: 'Order',
    component: Order,
    meta: {
      requireLogin: true
      }
    },
    {
    path: '/dashboard/orders/:id/edit',
    name: 'EditOrder',
    component: EditOrder,
    meta: {
      requireLogin: true
      }
    },
    {
      path: '/dashboard/orders/add',
      name: 'AddOrder',
      component: AddOrder,
      meta: {
        requireLogin: true
      }
    },
    {
      path: '/dashboard/client',
      name: 'Client',
      component: Client,
      meta: {
        requireLogin: true
      }
    },
    {
      path: '/dashboard/clients/:id',
      name: 'ShowClient',
      component: ShowClient,
      meta: {
        requireLogin: true
      }
    },
    {
      path: '/dashboard/clients/:id/edit',
      name: 'EditClient',
      component: EditClient,
      meta: {
        requireLogin: true
      }
    },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
