<
<template>
    <v-app>
        <v-main>
            <v-IPTxt class="d-flex justify-center">
                <h1>I Process</h1>
            </v-IPTxt>

            <v-aiprocess class="d-flex align-center justify-center">
                <v-card class="mx-auto" height="400" max-width="350" hover>
                    <v-card-item>
                        <v-card-title> Grammar Checking </v-card-title>
                    </v-card-item>
                    <v-img height="200px" src="@/assets/grammar@2x.png" cover></v-img>
                    <v-card-text>
                        Refine your writing effortlessly with our AI-powered grammar checking, powered by LanguageTool.
                    </v-card-text>
                </v-card>
                <v-card class="mx-auto" height="400" max-width="350" hover>
                    <v-card-item>
                        <v-card-title> Paraphrasing Assistant </v-card-title>
                    </v-card-item>
                    <v-img height="200px" src="@/assets/paraphrase@2x.png" cover></v-img>
                    <v-card-text>
                        Rephrase your sentences as needed to be more formal, fluent, casual, or concise.
                    </v-card-text>
                </v-card>
                <v-card class="mx-auto" height="400" max-width="350" hover>
                    <v-card-item>
                        <v-card-title> Definition of Terms </v-card-title>
                    </v-card-item>
                    <v-img height="200px" src="@/assets/defination@2x.png" cover></v-img>
                    <v-card-text> Automatically identify important terms and provide definitions. </v-card-text>
                </v-card color=#1e1e24>
                <v-card class="mx-auto" height="400" max-width="350" hover>
                    <v-card-item>
                        <v-card-title> Information retrieval </v-card-title>
                    </v-card-item>
                    <v-img height="200px" src="@/assets/info.png" cover></v-img>
                    <v-card-text>
                        Unlock rapid access to pertinent data with sophisticated information retrieval capabilities.
                    </v-card-text>
                </v-card>
            </v-aiprocess>
        </v-main>
    </v-app>
</template>

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
v-card{
    color: #16171b;
    
}
v-aiprocess{
    margin-top: 10%;
}

v-IPTxt {
    font-size: 3rem;
    font-family: "Montserrat", sans-serif;
    margin-top: 5%;
    text-align: center;
}
</style>
