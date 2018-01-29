import Vue from 'vue'
import NavbarComponent from '../components/navbarComponent.vue'
import PageHeadingComponent from '../components/PageHeadingComponent.vue'
//import SubmitContract from '../components/submitContract.vue'
Vue.component('navbar-component',NavbarComponent)
Vue.component('pagehead-component',PageHeadingComponent)
//Vue.component('submit-contract',SubmitContract)

new Vue({
      el: '#app',
})

