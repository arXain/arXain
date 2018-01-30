import Vue from 'vue'
import NavbarComponent from '../components/navbarComponent.vue'
import PageHeadingComponent from '../components/PageHeadingComponent.vue'
import SubmitContract from '../components/submitContract.vue'
import StatusContract from '../components/statusContract.vue'
import AmendContract from '../components/amendContract.vue'
import CommentsContract from '../components/commentsContract.vue'
Vue.component('navbar-component',NavbarComponent)
Vue.component('pagehead-component',PageHeadingComponent)
Vue.component('submit-contract',SubmitContract)
Vue.component('status-contract',StatusContract)
Vue.component('amend-contract',AmendContract)
Vue.component('comments-contract',CommentsContract)

new Vue({
      el: '#app',
})

