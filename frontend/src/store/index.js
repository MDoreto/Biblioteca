import Vue from 'vue';
import Vuex from 'vuex';
import createPersistedState from "vuex-persistedstate";
import * as Cookies from "js-cookie";

Vue.use(Vuex);
export default new Vuex.Store({
    state: {
        auth: false,
    },
    getters: {
        getRole: state => {
            return state.role;
        },
    },
    plugins: [
        createPersistedState({
            paths: ['auth'],
            storage: {
                getItem: (key) => Cookies.get(key),
                setItem: (key, value) =>
                    Cookies.set(key, value, { expires: 7 }),
                removeItem: (key) => Cookies.remove(key),
            },
        }),
    ],
    actions: {
        login({ commit }) {
            commit('SET_AUTH', true);
        },
        logout({ commit }) {
            commit('SET_AUTH', false);
        }
    },

    //to handle mutations
    mutations: {
        SET_AUTH(state, value) {
            state.auth = value
        }
    }
});