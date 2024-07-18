<template>
<v-app>
    <v-main>
     
            
  <v-row dense>
    <v-col
      v-for="(variant, i) in variants"
      :key="i"
      cols="12"
      md="3"
    >
      <v-card
        :variant="variant"
        class="mx-auto"
        color="surface-variant"
        max-width="344"
        subtitle="Greyhound divisely hello coldly fonwderfully"
        title="Headline"
      >
        <template v-slot:actions>
          
          <v-btn text=""></v-btn>
            <p class="notedate"> Edited: 06/07/24 </p>
        </template>
      </v-card>

      <div class="text-center text-caption"></div>
    </v-col>
  </v-row>
    </v-main>
    </v-app>
</template>

<script>
  export default {
    data: () => ({
      variants: ['tonal', 'tonal', 'tonal', 'tonal', 'tonal', 'tonal', 'tonal', 'tonal','tonal'],
    }),
  }
</script>
<style>
.note{
    margin-top: 10%;

    }
  .notedate {
    font-size: 0.8rem;
    color: #a8a8a8;
    opacity: 0.5;
    margin-top: 0;
    margin-left: 30%;

  }
  </style>