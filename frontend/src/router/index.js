import Vue from 'vue'
import Router from 'vue-router'
import Checkout from '@/components/Checkout'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Checkout',
      component: Checkout
    }
  ]
})
