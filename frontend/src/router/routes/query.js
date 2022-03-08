export default [
  {
    path: '/query',
    name: 'query',
    component: () =>
      import(/* webpackChunkName: "about" */ '@/components/Query.vue')
  }
]
