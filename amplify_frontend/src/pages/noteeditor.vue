<template>  
    <v-app>
        <v-main>
         <noteeditorcom />  
        </v-main>
        </v-app>
</template>


<script>
import noteeditorcom from '@/components/noteeditorcom.vue';

export default {
  name: 'noteeditor',
  components: {
    noteeditorcom
  }
};
</script>
<style>

@import '@mdi/font/css/materialdesignicons.css';
@import 'vuetify/styles';

</style>