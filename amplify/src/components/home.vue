<template>
    <v-app>
        <v-main>
            <v-app-home class="d-flex align-center justify-center flex-column">
                <div class="home">
                    <h1 class="home_amplify">AMPLIFY</h1>
                </div>
                <div class="home">
                    <h2>Make Powerful Notes</h2>
                </div>
                <div class="home_description">
                    <p>An AI-Powered Note-Taking Platform for Students</p>
                </div>
            </v-app-home>
        </v-main>
    </v-app>
</template>

<style>
v-app-home {
    height: 100vh;
    min-height: 100vh;
    background-image: url("@/assets/bg@2x.png");
    background-size: 100vw 100vh;
}
.home {
    font-size: 2rem;
    font-family: "Montserrat", sans-serif;
    font-weight: bolder;
    color: #fff;

    text-align: center;
}
.home_description {
    font-size: 1rem;
    font-family: "MuktaVaani", sans-serif;
    color: #a8a8a8;
    text-align: center;
}
.home_amplify {
    font-size: 6rem;
    font-family: "Montserrat", sans-serif;
    font-weight: 900;
    color: #ffffff;
    background: linear-gradient(to right, #4d4d4d 0, white 10%, #4d4d4d 20%);
    background-size: cover;
    background-position: 0;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: shine 3s infinite linear;
    animation-fill-mode: forwards;
}
@keyframes shine {
    0% {
        background-position: 0;
    }
    60% {
        background-position: 180px;
    }
    100% {
        background-position: 360px;
    }
}
@media screen and (max-width: 600px) {
    .home_amplify {
        font-size: 3rem;
    }
    .home {
        font-size: 1rem;
    }
    .home_description {
        font-size: 0.5rem;
    }
}
@media screen and (min-width: 600px) and (max-width: 1000px) {
    .home_amplify {
        font-size: 4rem;
    }
    .home {
        font-size: 1.5rem;
    }
    .home_description {
        font-size: 1rem;
    }
}
</style>
