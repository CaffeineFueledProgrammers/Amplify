import { defineStore } from "pinia";

export const useUserStore = defineStore("user", {
    state: () => ({ _isLoggedIn: false, _userData: null }),
    getters: {
        isLoggedIn: (state) => state._isLoggedIn,
        userData: (state) => state._userData,
    },
    actions: {
        login(userData) {
            this._isLoggedIn = true;
            this._userData = userData;
        },
        logout() {
            this._isLoggedIn = false;
            this._userData = null;
        },
    },
});
