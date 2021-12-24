import axios from 'axios';
import router from './router';
import store from './store'

function apiService() {

    var a = axios.create({
        baseURL: process.env.VUE_APP_ROOT_API,
        withCredentials: true,
        credentials: "same-origin",
        headers: {
            "X-CSRF-TOKEN": getCookie("csrf_access_token"),
        },
    })
    a.interceptors.response.use(
        (response) => response,
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