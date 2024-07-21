import { defineStore } from "pinia";

// You can name the return value of `defineStore()` anything you want,
// but it's best to use the name of the store and surround it with `use`
// and `Store` (e.g. `useUserStore`, `useCartStore`, `useProductStore`)
// the first argument is a unique id of the store across your application
export const useUserStore = defineStore("user", {
    state: () => ({ username: null, notes: [] }),
    getters: {
        first_name: (state) => state.first_name,
        last_name: (state) => state.last_name,
        email: (state) => state.email,
        notes: (state) => state.notes,
    },
    actions: {
        setEmail(email) {
            this.email = email;
        },
        addNote(note) {
            this.notes.push(note);
        },
        getNote(index) {
            return this.notes[index];
        },
        removeNote(index) {
            this.notes.splice(index, 1);
        },
        clearNotes() {
            this.notes = [];
        },
    },
});
