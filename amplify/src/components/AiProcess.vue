<template>
    <v-app>
        <v-main>
            <v-iptxt class="d-flex justify-center align-center">
                <img height="400px" width="400px" src="@/assets/feather@2x.png" />
                <h1>I Process</h1>
            </v-iptxt>
            <v-aiprocess
                class="d-flex align-center justify-center"
                data-aos="fade-up"
                data-aos-once="false"
                data-aos-duration="500"
            >
                <v-card height="400" max-width="350" color="#1e1e24" hover>
                    <v-card-item>
                        <v-card-title> Grammar Checking </v-card-title>
                    </v-card-item>
                    <v-img src="@/assets/grammar@2x.png" cover></v-img>
                    <v-card-text>
                        Refine your writing effortlessly with our AI-powered grammar checking, powered by LanguageTool.
                    </v-card-text>
                </v-card>
                <v-card class="ml-3" height="400" max-width="350" color="#1e1e24" hover>
                    <v-card-item>
                        <v-card-title> Paraphrasing Assistant </v-card-title>
                    </v-card-item>
                    <v-img src="@/assets/paraphrase@2x.png" cover></v-img>
                    <v-card-text>
                        Rephrase your sentences as needed to be more formal, fluent, casual, or concise.
                    </v-card-text>
                </v-card>
                <v-card class="ml-3" height="400" max-width="350" color="#1e1e24" hover>
                    <v-card-item>
                        <v-card-title> Definition of Terms </v-card-title>
                    </v-card-item>
                    <v-img src="@/assets/defination@2x.png" cover></v-img>
                    <v-card-text> Automatically identify important terms and provide definitions. </v-card-text>
                </v-card>
                <v-card class="ml-3" height="400" max-width="350" color="#1e1e24" hover>
                    <v-card-item>
                        <v-card-title> Information retrieval </v-card-title>
                    </v-card-item>
                    <v-img src="@/assets/info.png" cover></v-img>
                    <v-card-text>
                        Unlock rapid access to pertinent data with sophisticated information retrieval capabilities.
                    </v-card-text>
                </v-card>
            </v-aiprocess>
        </v-main>
    </v-app>
</template>
<script></script>

<style>
v-card-title {
    font-size: 2rem;
    font-family: "Montserrat", sans-serif;
    color: #fff;
    text-align: center;
}
v-card-subtitle {
    font-size: 1.2rem;
    font-family: "MuktaVaani", sans-serif;
    color: #a8a8a8;
    text-align: center;
}
v-card {
    color: #16171b;
}
v-aiprocess {
    margin-top: 2%;
    margin-left: 2%;
    margin-right: 2%;
}
v-iptxt {
    font-size: 3rem;
    font-family: "Montserrat", sans-serif;
    margin-top: 1%;
    text-align: center;
}
v-iptxt h1 {
    position: relative;
    left: -6%;
    font-size: 6rem;
    font-family: "Montserrat", sans-serif;
    font-weight: 900;
}
.v-card img {
    width: 400px;
    height: 200px;
}
@media screen and (max-width: 700px) {
    v-iptxt img {
        width: 200px;
        height: 200px;
    }

    v-iptxt h1 {
        font-size: 3rem;
        left: 0;
    }

    .v-card {
        width: 80vw;
        margin-top: 5%;
    }

    v-aiprocess {
        flex-direction: column;
    }
    v-card-title {
        font-size: 1rem;
    }
    v-card-subtitle {
        font-size: 0.5rem;
    }
}

@media screen and (min-width: 700px) and (max-width: 1100px) {
    v-iptxt img {
        width: 20vw;
        height: 20vw;
    }

    v-iptxt h1 {
        font-size: 5rem;
        left: -3%;
    }

    .v-card {
        width: 23vw;
        max-height: 45vh;
    }
    v-card-title {
        font-size: 1rem;
    }
    v-card-subtitle {
        font-size: 0.5rem;
    }
    .v-card img {
        width: 200px;
        height: 100px;
    }
}
</style>
