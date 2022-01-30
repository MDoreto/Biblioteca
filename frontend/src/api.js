import axios from 'axios';
import store from './store'

function apiService() {

    var a = axios.create({
        baseURL: process.env.VUE_APP_ROOT_API,
        withCredentials: true,
        headers: {
            "X-CSRF-TOKEN": getCookie("csrf_access_token"),
        },
    })
    a.interceptors.request.use((config) => { store.commit("SET_ISLOADING", true); return config; })
    a.interceptors.response.use(
        (response) => { store.commit("SET_ISLOADING", false); return response; },
        (error) => {
            if (error.response.status === 401) {
                store.dispatch("logout");
            }
            return Promise.reject(error);
        }
    )
    return a
}

function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
}
export { apiService };