<
<template>
    <v-app>
        <v-main>
            <div class="d-flex align-center">
                <h1>I Process</h1>
            </div>

            <v-aiprocess class="d-flex align-center justify-center">
                <v-card class="mx-auto" height="400" max-width="350" hover>
                    <v-card-item>
                        <v-card-title> Grammar Checking </v-card-title>
                    </v-card-item>
                    <v-img height="100px" src=".\public\grammar@2x.png" cover></v-img>
                    <v-card-text>
                        Refine your writing effortlessly with our AI-powered grammar checking, powered by LanguageTool.
                    </v-card-text>
                </v-card>
                <v-card class="mx-auto" height="400" max-width="344" hover>
                    <v-card-item>
                        <v-card-title> Paraphrasing Assistant </v-card-title>

                        <v-card-subtitle> </v-card-subtitle>
                    </v-card-item>

                    <v-card-text>
                        Rephrase your sentences as needed to be more formal, fluent, casual, or concise.
                    </v-card-text>
                </v-card>
                <v-card class="mx-auto" height="400" max-width="344" hover>
                    <v-card-item>
                        <v-card-title> Definition of Terms </v-card-title>

                        <v-card-subtitle> </v-card-subtitle>
                    </v-card-item>

                    <v-card-text> Automatically identify important terms and provide definitions. </v-card-text>
                </v-card>
                <v-card class="mx-auto" height="400" max-width="344" hover>
                    <v-card-item>
                        <v-card-title> Information retrieval </v-card-title>

                        <v-card-subtitle> </v-card-subtitle>
                    </v-card-item>

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
    color: #fff;
    text-align: center;
}
v-card-subtitle {
    font-size: 1.2rem;
    color: #a8a8a8;
    text-align: center;
}
</style>
