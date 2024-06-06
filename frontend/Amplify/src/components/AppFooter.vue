<template>
    <v-footer height="50vh">
        <v-amplify_footer class="d-flex justify-start">
            <v-img height="150px" width="150px" src="@/assets/logo1@2x.png"></v-img>
            <v-amplify_footertext class="d-flex align-start flex-column">
                <h1 class="title">Amplify</h1>
                <h2 class="tagline">Make Powerful Notes</h2>
            </v-amplify_footertext>
        </v-amplify_footer>
        <a
            v-for="item in items"
            :key="item.title"
            :href="item.href"
            :title="item.title"
            class="d-inline-block mx-2 social-link"
            rel="noopener noreferrer"
            target="_blank"
        >
            <v-icon :icon="item.icon" :size="item.icon === '$vuetify' ? 24 : 16" />
        </a>
        <div class="text-caption text-disabled" style="position: absolute; right: 16px">
            &copy; 2016-{{ new Date().getFullYear() }} <span class="d-none d-sm-inline-block">Amplify</span>
            —
            <a
                class="text-decoration-none on-surface"
                href="https://vuetifyjs.com/about/licensing/"
                rel="noopener noreferrer"
                target="_blank"
            >
                MIT License
            </a>
        </div>
    </v-footer>
</template>

<script setup>
const items = [
    {
        title: "Vuetify Documentation",
        icon: `$vuetify`,
        href: "https://vuetifyjs.com/",
    },
    {
        title: "Vuetify Support",
        icon: "mdi-shield-star-outline",
        href: "https://support.vuetifyjs.com/",
    },
    {
        title: "Vuetify X",
        icon: `svg:M2.04875 3.00002L9.77052 13.3248L1.99998 21.7192H3.74882L10.5519 14.3697L16.0486 21.7192H22L13.8437 10.8137L21.0765 3.00002H19.3277L13.0624 9.76874L8.0001 3.00002H2.04875ZM4.62054 4.28821H7.35461L19.4278 20.4308H16.6937L4.62054 4.28821Z`,
        href: "https://x.com/vuetifyjs",
    },
    {
        title: "Vuetify GitHub",
        icon: `mdi-github`,
        href: "https://github.com/vuetifyjs/vuetify",
    },
    {
        title: "Vuetify Discord",
        icon: `mdi-discord`,
        href: "https://community.vuetifyjs.com/",
    },
    {
        title: "Vuetify Reddit",
        icon: `mdi-reddit`,
        href: "https://reddit.com/r/vuetifyjs",
    },
];
</script>

<style scoped lang="sass">
.social-link :deep(.v-icon)
  color: rgba(var(--v-theme-on-background), var(--v-disabled-opacity))
  text-decoration: none
  transition: .2s ease-in-out

  &:hover
    color: rgba(25, 118, 210, 1)
</style>

<style>
v-amplify_footer {
    margin-left: 10%;
    background-image: url();
}

v-amplify_footertext {
    width: 20vh;
    margin-top: 10%;
    margin-left: 5%;
}
.title {
    font-size: 1.5rem;
    font-family: "Montserrat", sans-serif;
    font-weight: bolder;
    color: #fff;
    text-align: start;
}
.tagline {
    font-size: 1rem;
    font-family: "MuktaVaani", sans-serif;
    color: #a8a8a8;
}
</style>
