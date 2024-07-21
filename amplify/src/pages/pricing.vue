<template>
    <v-app>
        <v-main>
            <v-container>
                <v-row justify="center">
                    <!-- AmpliFree -->
                    <v-col cols="12" sm="6" md="4">
                        <v-card class="mx-auto my-8 amplifree" elevation="2">
                            <v-card-title class="text-center title-style">AmpliFree</v-card-title>
                            <v-card-subtitle class="text-center price-style">Free</v-card-subtitle>
                            <v-card-subtitle class="text-center billing-style"> You can access the basic features <br />
                                of Amplify for free.</v-card-subtitle>
                            <v-card-actions class="text-center">
                                <v-btn class="mx-2 signupbtn" @click="goToSignUp"  color="#566498">TRY NOW! </v-btn>
                            </v-card-actions>
                            <v-card-text class="text-center">
                                <v-list dense>
                                    <v-list-item>
                                        <v-list-item-content>Basic Note Taking </v-list-item-content>
                                    </v-list-item>
                                    <v-list-item>
                                        <v-list-item-content> Collaboration ( Limited to 3 Members)</v-list-item-content>
                                    </v-list-item>
                                </v-list>
                            </v-card-text>
                        </v-card>
                    </v-col>
                    <!-- AmpliPro -->
                    <v-col cols="12" sm="6" md="4">
                        <v-card class="mx-auto my-8 amplipro"  elevation="2">
                            <v-card-title class="text-center title-styleamplipro">AmpliPro</v-card-title>
                          <v-card-subtitle class="text-center price-style">₱ 300.00</v-card-subtitle>
                            <v-card-subtitle class="text-center billing-style"> per month</v-card-subtitle>
                            <v-card-actions class="text-center">
                               
                                 <router-link :to="{ path: '/billingpage' }"> <v-btn class="mx-2 subbtn" >Subscribe Now! </v-btn></router-link>
                            </v-card-actions>
                            <v-card-text class="text-center amplipro">
                                <v-list dense class="amplipro">
                                    <v-list-item>
                                        <v-list-item-content >Unlimited Notes</v-list-item-content>
                                    </v-list-item>
                                    <v-list-item>
                                        <v-list-item-content>Advance Paraphrasing</v-list-item-content>
                                    </v-list-item>
                                    <v-list-item>
                                        <v-list-item-content>Seamless Collaboration</v-list-item-content>
                                    </v-list-item>
                                    <v-list-item>
                                        <v-list-item-content> Word Definitions</v-list-item-content>
                                    </v-list-item>
                                    <v-list-item>
                                        <v-list-item-content> Anki Flashcard Generation</v-list-item-content>
                                    </v-list-item>
                                </v-list>
                            </v-card-text>
                        </v-card>
                
                    </v-col>
                </v-row>   
            </v-container>
        </v-main>
    </v-app>
</template>

<script>
export default {
    methods: {
        goToSignUp() {
            this.$router.push({ path: "/login", query: { section: "signup" } });
        },
    },
};
</script>

<style scoped >
.title-style {
 
    font-family: "Poppins", sans-serif;
    font-size: 40px;
    font-weight: 600;   
    margin-top:1.5vh;
}

.price-style {
    font-family: "Poppins", sans-serif;
    font-size: 20px;
    font-weight: 400;
}

.billing-style {
    font-family: "Poppins", sans-serif;
    font-size: 14px;
    font-weight: 300;
}

.v-card-actions {
    justify-content: center;
}


.v-list-item-content {
    font-family: "Poppins", sans-serif;
    font-size: 14px;

}
.title-styleamplipro{
    color: black;
    font-family: "Poppins", sans-serif;
    font-size: 40px;
    font-weight: 600;
    margin-top:1.5vh;
}
.amplifree, .amplipro {
    max-height: 80vh;
    min-height: 80vh;
}

.amplipro {
  
    background-color: beige;
    color: black;

}
.signupbtn {
    color: #566498 ;
    background-color: beige;
    font-weight: bold;
    width: 13vw;
    margin-top: 4vh;
}
.subbtn {
   color: white;
    background-color: #566498;
    width: 13vw;
    margin-top: 6vh;
}
</style>
