<template>
  <v-app style="height: 100vh;">
    <v-main style="height: 100vh;">
      <v-row justify="center">
        <v-col cols="20" md="60">
          <v-card>
            <v-card-title>
              <input v-model="title" class="editable-title" placeholder="Note Title">
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
    </v-main>
  </v-app>
</template>

<script>
import { ref } from 'vue';

export default {
  name: 'NoteEditor',
  setup() {
    const editor = ref(null);
    const content = ref('');
    const title = ref('');

    const formatText = (command, value = null) => {
      document.execCommand(command, false, value);
    };

    const highlightText = () => {
      document.execCommand('hiliteColor', false, '#a8a8a8');
    };

    const updateContent = () => {
      content.value = editor.value.innerHTML;
    };

    const saveNote = () => {
      console.log(title.value);
      console.log(content.value);
      // Add your save logic here
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
.updatecontent{
  margin-left: 80px;
}
.editor {
  min-height: 100vh;
  margin-top: 10px;
  min-width: 80vw;
  

}
.editable-title {
  width: 100%;
  border: none;
  font-size: 24px;
  font-weight: bold;
  padding: 8px;
}
</style>