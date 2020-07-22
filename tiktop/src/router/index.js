import Vue from 'vue'
import Router from 'vue-router'
import index from '@/views/index'
import first from '@/views/first'
import enterText from '@/views/enterText'
import chooseHope from '@/views/chooseHope'
import result from '@/views/result'
import cheer from '@/views/cheer'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'index',
      component: index
    },
    {
      path: '/first',
      name: 'first',
      component: first
    },
    {
      path: '/enterText',
      name: 'enterText',
      component: enterText
    },
    {
      path: '/enterText/:isBack',
      name: 'enterText',
      component: enterText
    },
    {
      path: '/chooseHope',
      name: 'chooseHope',
      component: chooseHope
    },
    {
      path: '/result',
      name: 'result',
      component: result
    },
    {
      path: '/cheer',
      name: 'cheer',
      component: cheer
    },
  ]
})
