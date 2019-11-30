import Vue from 'vue';
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
import App from './App.vue'
import './config/http'
import VueApexCharts from 'vue-apexcharts'

Vue.config.productionTip = false

Vue.use(ElementUI);
Vue.use(VueApexCharts)
Vue.component('apexchart', VueApexCharts)

new Vue({
  render: h => h(App),
}).$mount('#app')
