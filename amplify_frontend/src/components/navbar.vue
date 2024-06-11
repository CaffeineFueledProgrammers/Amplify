<template>
    <v-app-bar height="90">
        <img class="navlogo" src="@/assets/logo1@2x.png" alt="logo" width="80" height="80" />
        <v-spacer></v-spacer>
        <router-link :to="{ path: '/' }"><v-btn class="button">Home</v-btn></router-link>
        <router-link :to="{ path: '/login' }"><v-btn class="button">Log In</v-btn></router-link>
        <v-btn @click="goToSignUp" class="button">Sign Up</v-btn>
    </v-app-bar>
</template>

<style>
v-app-bar {
    position: sticky;
    top: 0%;
}
.button {
    font-family: "Montserrat", sans-serif;
    font-weight: bold;
}
.button:hover,
.button:focus {
    border: 2px solid #566498;
    box-shadow: 0 0.5em 0.5em -0.4em #566498;
    transform: translateY(-0.25em);
}
:hover,
:focus {
    border-color: #566498;
    color: #fff;
}
.navlogo {
    margin-left: 5%;
}
</style>

<script>
export default {
    methods: {
        goToSignUp() {
            this.$router.push({ path: "/login", query: { section: "signup" } });
        },
    },
};
</script>

