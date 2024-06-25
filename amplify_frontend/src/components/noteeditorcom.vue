<template>
  <v-container>
    <v-row justify="center">
      <v-col cols="12" md="8">
        <v-card>
          <v-card-title>
            Note Taking App
          </v-card-title>
          <v-card-text>
            <div>
              <v-btn icon @click="formatText('bold')">
                <v-icon>mdi-format-bold</v-icon>
              </v-btn>
              <v-btn icon @click="formatText('italic')">
                <v-icon>mdi-format-italic</v-icon>
              </v-btn>
              <v-btn icon @click="formatText('underline')">
                <v-icon>mdi-format-underline</v-icon>
              </v-btn>
              <v-btn icon @click="formatText('insertOrderedList')">
                <v-icon>mdi-format-list-numbered</v-icon>
              </v-btn>
              <v-btn icon @click="formatText('insertUnorderedList')">
                <v-icon>mdi-format-list-bulleted</v-icon>
              </v-btn>
              <v-btn icon @click="formatText('formatBlock', 'H1')">
                <v-icon>mdi-format-header-1</v-icon>
              </v-btn>
              <v-btn icon @click="formatText('formatBlock', 'H2')">
                <v-icon>mdi-format-header-2</v-icon>
              </v-btn>
              <v-btn icon @click="highlightText">
                <v-icon>mdi-marker</v-icon>
              </v-btn>
            </div>
            <div
              contenteditable="true"
              ref="editor"
              class="editor"
              @input="updateContent"
            ></div>
          </v-card-text>
          <v-card-actions>
            <v-btn color="primary" @click="saveNote">Save Note</v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import { ref } from 'vue';

export default {
  name: 'NoteEditor',
  setup() {
    const editor = ref(null);
    const content = ref('');

    const formatText = (command, value = null) => {
      document.execCommand(command, false, value);
    };

    const highlightText = () => {
      document.execCommand('hiliteColor', false, 'yellow');
    };

    const updateContent = () => {
      content.value = editor.value.innerHTML;
    };

    const saveNote = () => {
      console.log(content.value);
      // Add your save logic here
    };

    return {
      editor,
      formatText,
      highlightText,
      content,
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
}
</style>
