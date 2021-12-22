import axios from 'axios';

function apiService() {
    return axios.create({
        baseURL: process.env.VUE_APP_ROOT_API,
        withCredentials: true,
        xsrfCookieName: 'csrf_access_token',
        credentials: "same-origin",
        headers: {
            "Content-Type": "application/json",
            "X-CSRF-TOKEN": getCookie("csrf_access_token"),
        },
    })
}

function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
}
export { apiService };