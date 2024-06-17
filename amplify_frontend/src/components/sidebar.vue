<template>
<v-app>
  <v-card>
    <v-layout>
      <v-navigation-drawer
        v-model="drawer"
        :rail="rail"
        permanent
        @click="rail = false"
     
      >
        <v-list-item
   
          title="username"
          nav
        >
          <template v-slot:append >
            <v-btn 
              icon="mdi-chevron-left"
              variant="text"
              @click.stop="rail = !rail"
            ></v-btn>
          </template>
        </v-list-item>

        <v-divider></v-divider>

        <v-list density="compact" nav>
          <v-list-item prepend-icon="mdi-note-multiple" title="Notes" value="notes"></v-list-item>
             <v-list-item prepend-icon="mdi-account-group-outline" title="Shared With You" value="sharedwithyou"></v-list-item>
              <v-list-item prepend-icon="mdi-card-multiple-outline" title="Anki Flashcards" value="flashcard"></v-list-item>
          <v-list-item prepend-icon="mdi-account" title="Account Settings " value="account"></v-list-item>
          <v-list-item prepend-icon="mdi-cash" title="Subsriptions" value="subscribe"></v-list-item>
             <v-list-item prepend-icon="mdi-location-exit" title="Sign Out" value="signout"></v-list-item>
        </v-list>
      </v-navigation-drawer>
      <v-main style="height: 100vh"> 
        <div class= "note" >
        <v-dashtitle >
          AMPLIFY NOTES
        </v-dashtitle>
        <notes />
        <sharedflashcar/>
        </div>
      </v-main>
    </v-layout>
  </v-card>
  </v-app>
</template>

<script>
import sharedflashcar from './sharedflashcar.vue'
  export default {
  components: { sharedflashcar },
    data () {
      return {
        drawer: true,
        rail: true,
      }
    },
  }
</script>
<style>
.navside {
  position: fixed;
z-index: 1;


}
v-dashtitle {
  font-size: 5rem;
  font-weight: bold;
  margin: 20px;
}
</style>