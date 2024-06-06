<template>
  <v-footer height="20vh">
    <v-amplify_footer class="d-flex justify-start align-center">
    <v-img height="120px" width="120px" src="@/assets/logo1@2x.png"></v-img>
    <v-amplify_footertext class="d-flex align-start justify-center flex-column">
    <h1 class="title">Amplify</h1>
    <h2 class="tagline">Make Powerful Notes</h2>
    </v-amplify_footertext>
</v-amplify_footer>
    <a
      v-for="item in items"
      :key="item.title"
      :href="item.href"
      :title="item.title"
      class="d-flex mx-2  align-end justify-end amplify-social-link"
      rel="noopener noreferrer"
      target="_blank"
    >
      <v-icon
        :icon="item.icon"
        :size="item.icon === '$amplify' ? 24 : 16"
      />
    </a>

    <div
      class="text-caption text-disabled"
      style="position: absolute; right: 10%;"
    >
      &copy; {{ (new Date()).getFullYear() }} <span class="d-none d-sm-inline-block">Amplify</span>
      —
      <a
        class="text-decoration-none on-surface"
        href="https://vuetifyjs.com/about/licensing/"
        rel="noopener noreferrer"
        target="_blank"
      >
         License
      </a>
    </div>
  </v-footer>
</template>

<script setup>

</script>

<style>
v-amplify_footer{

  margin-left:10%;
  background-image: url();}

v-amplify_footertext{
  width: 30vh;
  margin-left: 5%;
  margin-bottom:10%;
}
.title{
  font-size: 1.5rem;
 font-family: 'Montserrat',sans-serif ;
  font-weight: bolder;
  color: #fff;
  text-align: start;
}
.tagline{
  font-size: 1rem;
 font-family: 'MuktaVaani',sans-serif ;

    color: #a8a8a8;
}

</style>