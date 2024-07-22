<template>
    <v-app>
        <v-main class="noteditorcom">
            <v-row >

                <v-col cols="8">
                    <v-card>
                        <v-card-title>
                            <input v-model="title" class="editable-title" placeholder="Note Title" />
                        </v-card-title>
                        <v-card-text>
                            <div>
                                <v-btn class="noteeditbtn" icon @click="formatText('bold')">
                                    <v-icon>mdi-format-bold</v-icon>
                                </v-btn>
                                <v-btn class="noteeditbtn" icon @click="formatText('italic')">
                                    <v-icon>mdi-format-italic</v-icon>
                                </v-btn>
                                <v-btn class="noteeditbtn" icon @click="formatText('underline')">
                                    <v-icon>mdi-format-underline</v-icon>
                                </v-btn>
                                <v-btn class="noteeditbtn" icon @click="formatText('insertOrderedList')">
                                    <v-icon>mdi-format-list-numbered</v-icon>
                                </v-btn>
                                <v-btn class="noteeditbtn" icon @click="formatText('insertUnorderedList')">
                                    <v-icon>mdi-format-list-bulleted</v-icon>
                                </v-btn>
                                <v-btn class="noteeditbtn" icon @click="formatText('formatBlock', 'H1')">
                                    <v-icon>mdi-format-header-1</v-icon>
                                </v-btn>
                                <v-btn class="noteeditbtn" icon @click="formatText('formatBlock', 'H2')">
                                    <v-icon>mdi-format-header-2</v-icon>
                                </v-btn>
                                <v-btn class="noteeditbtn" icon @click="highlightText">
                                    <v-icon>mdi-marker</v-icon>
                                </v-btn>
                            </div>
                            <!-- <div class="textborder"> -->
                            <div contenteditable="true" class="editor" @input="updateContent" id="editor" v-if="note">
                                {{ note.content }}
                            </div>
                            <div contenteditable="true" class="editor" @input="updateContent" id="editor" v-else></div>
                            <!-- </div> -->
                        </v-card-text>
                        <v-card-actions>
                            <v-btn color="#5e6275" @click="saveNote">Save Note</v-btn>
                            <div class="pa-4 text-center">
                                <v-btn-group color="#5e6275" density="comfortable" rounded="pill" divided>
                                    <v-btn class="pe-2" prepend-icon="mdi-account-multiple-outline" variant="flat">
                                        <div class="text-none font-weight-regular">Share</div>

                                        <v-dialog activator="parent" max-width="500">
                                            <template v-slot:default="{ isActive }">
                                                <v-card rounded="lg">
                                                    <v-card-title class="d-flex justify-space-between align-center">
                                                        <div class="text-h5 text-medium-emphasis ps-2">
                                                            Invite Collaborators to connect
                                                        </div>

                                                        <v-btn
                                                            icon="mdi-close"
                                                            variant="text"
                                                            @click="isActive.value = false"
                                                        ></v-btn>
                                                    </v-card-title>

                                                    <v-divider class="mb-4"></v-divider>

                                                    <v-card-text>
                                                        <div class="text-medium-emphasis mb-4">
                                                            Invite collaborators to your notes and be more productive.
                                                        </div>

                                                        <div class="mb-2">Message (optional)</div>

                                                        <v-textarea
                                                            :counter="300"
                                                            class="mb-2"
                                                            rows="2"
                                                            variant="outlined"
                                                            persistent-counter
                                                        ></v-textarea>

                                                        <div class="text-overline mb-2">💎 PREMIUM</div>

                                                        <div class="text-medium-emphasis mb-1">
                                                            Share with unlimited people and get more insights about your
                                                            network. Get AmpliPro NOW!
                                                        </div>

                                                        <router-link :to="{ path: '/billingpage' }">
                                                            <v-btn
                                                                class="text-none font-weight-bold ms-n4"
                                                                color="primary"
                                                                text="Get AmpliPro"
                                                                variant="text"
                                                            ></v-btn>
                                                        </router-link>
                                                    </v-card-text>

                                                    <v-divider class="mt-2"></v-divider>

                                                    <v-card-actions class="my-2 d-flex justify-end">
                                                        <v-btn
                                                            class="text-none"
                                                            rounded="xl"
                                                            text="Cancel"
                                                            @click="isActive.value = false"
                                                        ></v-btn>

                                                        <v-btn
                                                            class="text-none"
                                                            color="primary"
                                                            rounded="xl"
                                                            text="Send"
                                                            variant="flat"
                                                            @click="isActive.value = false"
                                                        ></v-btn>
                                                    </v-card-actions>
                                                </v-card>
                                            </template>
                                        </v-dialog>
                                    </v-btn>

                                    <v-btn size="small" icon>
                                        <v-icon icon="mdi-menu-down"></v-icon>

                                        <v-menu activator="parent" location="bottom end" transition="fade-transition">
                                            <v-list density="compact" min-width="250" rounded="lg" slim>
                                                <v-list-item
                                                    prepend-icon="mdi-link"
                                                    title="Copy link"
                                                    link
                                                ></v-list-item>

                                                <v-divider class="my-2"></v-divider>

                                                <v-list-item min-height="24">
                                                    <template v-slot:subtitle>
                                                        <div class="text-caption">Shared with Collaborators</div>
                                                    </template>
                                                </v-list-item>
                                            </v-list>
                                        </v-menu>
                                    </v-btn>
                                </v-btn-group>
                            </div>
                        </v-card-actions>
                    </v-card>
                </v-col>
                <v-col cols="4">
            <v-card class="grammarchecker">
              <v-card-text>
            
                <p class="text-h4 font-weight-black">Grammar Checker</p>
                <p>Amplify</p>
             
              </v-card-text>
              <v-card-actions>
                <v-btn color="#566498" text="Check for Errors" variant="text" @click="reveal = true"></v-btn>
              </v-card-actions>
              <v-expand-transition>
                <v-card v-if="reveal" class="position-absolute w-100" height="100%" style="bottom: 0">
                  <v-card-text class="pb-0">
                    <p class="text-h4">Grammar Checker</p>
                    <p class="text-medium-emphasis">
                         <!-- Put the results of the grammar checker here -->


                    </p>
                  </v-card-text>
                  <v-card-actions class="pt-0">
                    <v-btn color="#566498" text="Close" variant="text" @click="reveal = false"></v-btn>
                  </v-card-actions>
                </v-card>
              </v-expand-transition>
            </v-card>
                         <v-alert 
                        class="notealert"
                        v-for="alert in alerts"
                        :key="alert.id"
                        :type="alert.type"
                        closable
                        @close="removeAlert(alert.id)"
                    >
                        {{ alert.message }}
                    </v-alert>
          </v-col>
            </v-row>
        </v-main>
    </v-app>
</template>

<script>
import { ref } from "vue";
import { useRoute } from "vue-router";
import { firebaseApp, db } from "@/firebasehandler";
import { useUserStore } from "@/stores/user";
import { getFirestore, serverTimestamp, addDoc, getDoc, updateDoc, doc, collection } from "firebase/firestore";
import axios from 'axios';

export default {
    name: "NoteEditor",
    data: () => ({
        note: null,
        alerts: [],
        title: "",
        content: "",
        alerts: [],
        reveal: false,
    }),
    methods: {
        addAlert(type, message) {
            const alert = {
                id: this.alerts.length +1,
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
        formatText(command, value = null) {
            document.execCommand(command, false, value);
        },
        highlightText() {
            document.execCommand("hiliteColor", false, "#a8a8a8");
        },
        updateContent() {
            var divContents = document.getElementById("editor").textContent;
            this.content = divContents;
        },
        async saveNote() {
            try {
                if (!this.note) {
                    // this is a new file.
                    const docRef = await addDoc(collection(db, "notes"), {
                        collaborators: [],
                        content: this.content,
                        owner: useUserStore().userData.uid,
                        time_created: serverTimestamp(),
                        time_modified: serverTimestamp(),
                        title: this.title,
                    });
                    console.log("Document written with ID: ", docRef.id);
                    this.addAlert("success", "Note created successfully! [Note ID: " + docRef.id + "]");
                } else {
                    const noteRef = doc(db, "notes", this.note.id);
                    await updateDoc(noteRef, {
                        title: this.title,
                        content: this.content,
                        time_modified: serverTimestamp(),
                    });
                    this.addAlert("success", "Note saved successfully!");
                }
            } catch (error) {
                this.addAlert("error", "Error saving note: " + error);
            }
        },
    },
    async created() {
        const route = useRoute();
        const note_id = route.query.note_id;

        if (note_id) {
            try {
                const docSnap = await getDoc(doc(db, "notes", note_id));
                if (docSnap.exists()) {
                    this.note = { id: docSnap.id, ...docSnap.data() };
                    this.title = this.note.title;
                    console.log(this.note);
                } else {
                    console.log("No such document!");
                    this.$router.push("/");
                }
            } catch (error) {
                console.error("Error fetching note:", error);
            }
        }
    },
};
</script>

<style>
.editor {
    min-height: 100vh;
    margin-top: 10px;
    min-width: 80vw;
    outline: none;
}
.content {
    border: 0px;
    padding-left: 20px;
}
.editable-title {
    width: 100%;
    border: none;
    font-size: 24px;
    font-weight: bold;
    padding: 8px;
}
.noteeditorcom {
    padding: 20px;
    max-height: 90vh;
    
}
.notealert {
    margin-top: 10px;
    width: 30vw;
    max-width: 35vw;
    z-index: 1;
}
.grammarchecker{
    max-height: 80vh;
    height: 50vh;
}
</style>
