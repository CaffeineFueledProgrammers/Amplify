<template>
    <v-app >
        <v-main class="noteditorcom">
            <v-row justify="center">
                <v-col cols="20" md="60">
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
                            <div contenteditable="true" class="editor" @input="updateContent" id="editor"></div>
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

                                                        <router-link :to="{ path: '/billingpage' }"> <v-btn
                                                            class="text-none font-weight-bold ms-n4"
                                                            color="primary"
                                                            text="Get AmpliPro"
                                                            variant="text"
                                                        ></v-btn> </router-link>
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
            </v-row>
        </v-main>
    </v-app>
</template>

<script>
import { ref } from "vue";

export default {
    name: "NoteEditor",
    setup() {
        const editor = ref(null);
        const content = ref("");
        const title = ref("");

        const formatText = (command, value = null) => {
            document.execCommand(command, false, value);
        };

        const highlightText = () => {
            document.execCommand("hiliteColor", false, "#a8a8a8");
        };

        const updateContent = () => {
            content.value = editor.value.innerHTML;
        };

        const saveNote = () => {
            console.log(title.value);
            console.log(content.value);
            // TODO: save logic here
        };

        return {
            editor,
            formatText,
            highlightText,
            content,
            title,
            saveNote,
            updateContent,
        };
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
</style>
