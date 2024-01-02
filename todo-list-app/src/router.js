// src/router.js

import Vue from 'vue';
import VueRouter from 'vue-router';

// Import your components
import HelloWorld from './components/HelloWorld.vue';

Vue.use(VueRouter);

const routes = [
  { path: '/', component: HelloWorld },
];

const router = new VueRouter({
  routes,
  mode: 'history', // Use history mode for clean URLs (optional)
});

export default router;
