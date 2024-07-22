<template>
    <v-app>
        <v-main>
            <div v-if="notes.length < 1">
                <!-- TODO: add padding -->
                <p class="text-center text-h5 nonote">You currently do not have any notes.</p>
                <v-row justify="center">
                    <v-col cols="auto">
                        <router-link :to="{ path: '/noteeditor' }"
                        ><v-btn class="nonote" text="Start Writing"></v-btn></router-link>
                    </v-col>
                </v-row>
            </div>
            <v-row v-else dense>
                <v-col v-for="(note, i) in notes" :key="i" cols="12" md="3">
                    <v-card class="mx-auto" color="surface-variant" max-width="344" variant="tonal">
                        <v-card-title>{{ note.title }}</v-card-title>
                        <v-card-subtitle>{{ note.content.substring(0, 20) }}</v-card-subtitle>
                        <template v-slot:actions>
                            <v-btn text=""></v-btn>
                            <p class="notedate">Edited {{ note.time_modified }}</p>
                        </template>
                    </v-card>

                    <div class="text-center text-caption"></div>
                </v-col>
            </v-row>
        </v-main>
    </v-app>
</template>

<script>
import { firebaseApp } from "@/firebasehandler";
import { useUserStore } from "@/stores/user";
import { getFirestore } from "firebase/firestore";

export default {
    data: () => ({
        notes: [],
    }),
    setup() {
        const store = useUserStore();
        const db = getFirestore(firebaseApp);
    },
};
</script>
<style>

.notedate {
    font-size: 0.8rem;
    color: #a8a8a8;
    opacity: 0.5;
    margin-top: 0;
    margin-left: 30%;
}
.nonote {
    margin-top: 5vh;
  
}
</style>
