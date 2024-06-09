/**
 * plugins/index.js
 *
 * Automatically included in `./src/main.js`
 */

// Plugins
import router from "@/router";
import vuetify from "./vuetify";
import AOS from 'aos'
import 'aos/dist/aos.css'

export function registerPlugins(app) {
    app.use(vuetify).use(router);
}

