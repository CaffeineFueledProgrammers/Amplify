import { defineStore } from "pinia";

export const useUserStore = defineStore("user", {
    state: () => ({
        // Initialize state from localStorage if available
        _isLoggedIn: JSON.parse(localStorage.getItem("isLoggedIn")) || false,
        _userData: JSON.parse(localStorage.getItem("userData")) || null,
    }),
    getters: {
        isLoggedIn: (state) => state._isLoggedIn,
        userData: (state) => state._userData,
    },
    actions: {
        login(userData) {
            this._isLoggedIn = true;
            this._userData = userData;
            // Persist to localStorage
            localStorage.setItem("isLoggedIn", JSON.stringify(true));
            localStorage.setItem("userData", JSON.stringify(userData));
        },
        logout() {
            this._isLoggedIn = false;
            this._userData = null;
            // Clear from localStorage
            localStorage.setItem("isLoggedIn", JSON.stringify(false));
            localStorage.removeItem("userData");
        },
    },
});
