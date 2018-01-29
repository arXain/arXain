import Vue from 'vue'
import NavbarComponent from '../components/navbarComponent.vue'
import PageHeadingComponent from '../components/PageHeadingComponent.vue'
Vue.component('navbar-component',NavbarComponent)
Vue.component('pagehead-component',PageHeadingComponent)

new Vue({
      el: '#app',
})

