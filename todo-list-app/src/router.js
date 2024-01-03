import Vue from "vue";
import VueRouter from "vue-router";

import HomePage from "./components/HomePage.vue";

Vue.use(VueRouter);

const routes = [{ path: "/", component: HomePage }];

const router = new VueRouter({
  routes,
  mode: "history",
});

export default router;
