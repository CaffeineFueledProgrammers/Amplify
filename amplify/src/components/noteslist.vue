<template>
    <v-app>
        <v-card>
            <v-layout>
                <v-navigation-drawer v-model="drawer" :rail="rail" permanent @click="rail = false">
                    <v-list-item :title="displayName" nav>
                        <template v-slot:append>
                            <v-btn
                                v-if="rail"
                                icon="mdi-chevron-right"
                                variant="text"
                                @click.stop="rail = false"
                            ></v-btn>
                            <v-btn v-else icon="mdi-chevron-left" variant="text" @click.stop="rail = true"></v-btn>
                        </template>
                    </v-list-item>

                    <v-divider></v-divider>

                    <v-list density="compact" nav>
                        <router-link :to="{ path: '/noteeditor' }"
                            ><v-list-item prepend-icon="mdi-note-multiple" title="Notes" value="notes"></v-list-item>
                        </router-link>
                        <v-list-item
                            prepend-icon="mdi-account-group-outline"
                            title="Shared With You"
                            value="sharedwithyou"
                        ></v-list-item>
                        <v-list-item
                            prepend-icon="mdi-card-multiple-outline"
                            title="Anki Flashcards"
                            value="flashcard"
                        ></v-list-item>
                        <v-list-item prepend-icon="mdi-account" title="Account Settings " value="account"></v-list-item>
                        <router-link :to="{ path: '/' }">
                            <v-list-item
                                prepend-icon="mdi-location-exit"
                                title="Sign Out"
                                value="signout"
                                @click="logout"
                            ></v-list-item>
                        </router-link>
                    </v-list>
            
                </v-navigation-drawer>
                 <v-main>
                    <div class="note">
                        <notes />
                        <sharedflashcard />
                    </div>
                </v-main>
            </v-layout>
        </v-card>
    </v-app>
</template>

<script>
import sharedflashcard from "./sharedflashcard";
import { useUserStore } from "@/stores/user";

export default {
    components: { sharedflashcard },
    data() {
        return {
            drawer: true,
            rail: true,
            displayName: "Amplify User",
        };
    },
    methods: {
        logout() {
            const store = useUserStore();
            store.logout();
            this.$router.push("/");
        },
    },
    mounted() {
        const store = useUserStore();

        this.displayName = store.userData.displayName;
    },
};
</script>
<style>
.navside {
    position: fixed;
    z-index: 1;
}
v-dashtitle {
    font-size: 5rem;
    font-weight: bold;
  
}
</style>
