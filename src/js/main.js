import Vue from 'vue'
import jQuery from 'jquery'
import BootstrapVue from 'bootstrap-vue'
Vue.use(BootstrapVue);

import Web3Box from '../components/Web3Box.vue'
import NavbarHome from '../components/NavbarHome.vue'
Vue.component('navbar-home',NavbarHome);

if($("#app").length != 0) {
    new Vue({
          el: '#app',
          template: '<Web3Box/>',
          components: { Web3Box }
    })
}

if($("#home").length != 0) {
    new Vue({
          el: '#home',
          template: '<navbar-home/>',
          components: { NavbarHome }
    })
}
