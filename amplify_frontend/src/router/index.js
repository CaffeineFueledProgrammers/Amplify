/**
 * router/index.ts
 *
 * Automatic routes for `./src/pages/*.vue`
 */

// Composables
import { createRouter, createWebHistory } from "vue-router/auto";

import index from "@/pages/index.vue";
import login from "@/pages/login.vue";
import dashboard from "@/pages/dashboard.vue";

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
});
const routes = [
    { path: "/", component: index },
    { path: "/login", component: login },
   {path: "/dashboard", component: dashboard} 
       
];

export default router;
