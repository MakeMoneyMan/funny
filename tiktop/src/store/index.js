import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

const store = new Vuex.Store({
  state: {
    count: 0,
    imageData: '',
    chooseHope: 1
  },
  mutations: {
    increment (state) {
      state.count++
    },
    setImage (state, data) {
      state.imageData = data
    },
    setChooseHope (state, data) {
      state.chooseHope = data
    }
  },
  actions: {
    setImageFun(context, data){
      context.commit('setImage', data)
    },
    setChooseHopeFun(context, data){
      context.commit('setChooseHope', data)
    }
  }
})

export default store