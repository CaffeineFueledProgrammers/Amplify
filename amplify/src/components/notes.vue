<template>
    <v-app>
        <v-main>
            <!-- TODO: do not span whole viewport width -->
            <v-alert v-for="alert in alerts" :key="alert.id" :type="alert.type" closable @close="removeAlert(alert.id)">
                {{ alert.message }}
            </v-alert>
            <div v-if="notes.length < 1">
                <!-- TODO: add padding -->
                <p class="text-center text-h5 nonote">You currently do not have any notes.</p>
                <v-row justify="center">
                    <v-col cols="auto">
                        <router-link :to="{ path: '/noteeditor' }"
                            ><v-btn class="nonote" text="Start Writing"></v-btn
                        ></router-link>
                    </v-col>
                </v-row>
            </div>
            <v-row v-else dense>
                <v-col v-for="(note, i) in notes" :key="i" cols="12" md="3">
                    <v-card class="mx-auto" color="surface-variant" max-width="344" variant="tonal">
                        <v-card-title>{{ note.title }}</v-card-title>
                        <v-card-subtitle>{{ note.content.substring(0, 20) }}</v-card-subtitle>
                        <template v-slot:actions>
                            <v-btn text="✎ Edit" :id="note.id" @click="editNote(note.id)"></v-btn>
                            <p class="notedate">Edited {{ formatTimeModified(note.time_modified) }}</p>
                        </template>
                    </v-card>

                    <div class="text-center text-caption"></div>
                </v-col>
            </v-row>
        </v-main>
    </v-app>
</template>

<script>
import { firebaseApp, notesRef } from "@/firebasehandler";
import { useUserStore } from "@/stores/user";
import { getFirestore, collection, getDocs, where, query } from "firebase/firestore";

export default {
    data: () => ({
        notes: [],
        alerts: [],
    }),
    methods: {
        addAlert(type, message) {
            const alert = {
                id: this.alerts.length,
                type,
                message,
            };
            this.alerts.push(alert);

            // Automatically remove the alert after 5 seconds
            setTimeout(() => {
                this.removeAlert(alert.id);
            }, 5000);
        },
        removeAlert(alertId) {
            this.alerts = this.alerts.filter((alert) => alert.id !== alertId);
        },
        formatTimeModified(timestamp) {
            return new Date(timestamp.seconds * 1000 + timestamp.nanoseconds / 1000000).toLocaleDateString();
        },
        editNote(note_id) {
            this.$router.push({ path: "/noteeditor", query: { id: note_id } });
        },
    },
    async created() {
        const store = useUserStore();

        try {
            const querySnapshot = await getDocs(query(notesRef, where("owner", "==", store.userData.uid)));
            const notes = querySnapshot.docs.map((doc) => ({
                id: doc.id,
                ...doc.data(),
            }));
            this.notes = notes;
        } catch (error) {
            this.addAlert("error", "Error fetching notes:" + error);
        }
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
