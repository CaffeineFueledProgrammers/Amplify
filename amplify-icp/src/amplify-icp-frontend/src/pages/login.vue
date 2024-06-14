<template>
    <v-app>
        <v-main>
            <v-container>
                <v-row align="center" justify="center">
                    <v-col cols="12" sm="10">
                        <v-card class="elevation-6 mt-10">
                            <v-window v-model="step">
                                <v-window-item :value="1">
                                    <v-row>
                                        <v-col cols="12" md="6">
                                            <v-card-text class="mt-12">
                                                <h3 class="text-center" style="font-family: &quot;montserrat&quot;">
                                                    Login in to Your Account
                                                </h3>
                                                <h4
                                                    class="text-center grey--text"
                                                    style="font-family: &quot;Mukta Vaani&quot;"
                                                >
                                                    Log in to your account so you can continue builiding <br />and
                                                    editing your onboarding flows
                                                </h4>
                                                <v-row align="center" justify="center">
                                                    <v-col cols="12" sm="8">
                                                        <v-text-field
                                                            label="Email"
                                                            outlined
                                                            dense
                                                            color="blue"
                                                            autocomplete="false"
                                                            class="mt-16"
                                                        />
                                                        <v-text-field
                                                            label="Password"
                                                            outlined
                                                            dense
                                                            color="blue"
                                                            autocomplete="false"
                                                            type="password"
                                                        />
                                                        <v-row>
                                                            <v-col cols="12" sm="7">
                                                                <v-checkbox
                                                                    label="Remember Me"
                                                                    class="mt-n1"
                                                                    color="blue"
                                                                >
                                                                </v-checkbox>
                                                            </v-col>
                                                            <v-col cols="12" sm="5">
                                                                <span class="caption blue--text">Forgot password</span>
                                                            </v-col>
                                                        </v-row>
                                                        <v-btn color="blue" dark block tile>Login</v-btn>
                                                        <h4
                                                            class="text-center grey--text mt-4 mb-3"
                                                            style="font-family: &quot;montserrat&quot;"
                                                        >
                                                            Login with
                                                        </h4>
                                                        <div
                                                            class="d-flex justify-space-between align-center mx-10 mb-11"
                                                        >
                                                            <v-btn depressed outlined color="grey">
                                                                <v-icon icon="mdi-google" color="red"></v-icon>
                                                            </v-btn>
                                                            <v-btn depressed outlined color="grey">
                                                                <v-icon icon="mdi-facebook" color="blue"></v-icon>
                                                            </v-btn>
                                                            <v-btn depressed outlined color="grey">
                                                                <v-icon icon="mdi-github" color="black"></v-icon>
                                                            </v-btn>
                                                        </div>
                                                    </v-col>
                                                </v-row>
                                            </v-card-text>
                                        </v-col>
                                        <v-col cols="12" md="6" class="blue rounded-bl-xl">
                                            <div style="text-align: center; padding: 180px 0">
                                                <v-card-text class="white--text">
                                                    <h2
                                                        class="text-center"
                                                        style="
                                                            font-family: &quot;montserrat&quot;;
                                                            color: #1e1e24;
                                                            margin-bottom: 10px;
                                                        "
                                                    >
                                                        Don't Have an Account Yet?
                                                    </h2>
                                                    <h4
                                                        class="text-center"
                                                        style="font-family: &quot;Mukta Vaani&quot;; color: #1e1e24"
                                                    >
                                                        Let's get you all set up so you can start creating your your
                                                        first<br />
                                                        onboarding experience
                                                    </h4>
                                                </v-card-text>
                                                <div class="text-center">
                                                    <v-btn tile outlined dark @click="step++">SIGN UP</v-btn>
                                                </div>
                                            </div>
                                        </v-col>
                                    </v-row>
                                </v-window-item>
                                <v-window-item :value="2" id="target-component">
                                    <v-row>
                                        <v-col cols="12" md="6" class="blue rounded-br-xl">
                                            <div style="text-align: center; padding: 180px 0">
                                                <v-card-text class="white--text">
                                                    <h2
                                                        class="text-center"
                                                        style="
                                                            font-family: &quot;montserrat&quot;;
                                                            color: #1e1e24;
                                                            margin-bottom: 10px;
                                                        "
                                                    >
                                                        Already Signed up?
                                                    </h2>
                                                    <h4
                                                        class="text-center"
                                                        style="font-family: &quot;Mukta Vaani&quot;; color: #1e1e24"
                                                    >
                                                        Log in to your account so you can continue building and<br />
                                                        editing your onboarding flows
                                                    </h4>
                                                </v-card-text>
                                                <div class="text-center">
                                                    <v-btn tile outlined dark @click="step--">Log in</v-btn>
                                                </div>
                                            </div>
                                        </v-col>

                                        <v-col cols="12" md="6">
                                            <v-card-text class="mt-12">
                                                <h3 class="text-center" style="font-family: &quot;montserrat&quot;">
                                                    Sign Up for an Account
                                                </h3>
                                                <h5
                                                    class="text-center grey--text"
                                                    style="font-family: &quot;Mukta Vaani&quot;"
                                                >
                                                    Let's get you all set up so you can start creatin your <br />
                                                    first onboarding experiance
                                                </h5>
                                                <v-row align="center" justify="center">
                                                    <v-col cols="12" sm="8">
                                                        <v-row>
                                                            <v-col cols="12" sm="6">
                                                                <v-text-field
                                                                    label="First Name"
                                                                    outlined
                                                                    dense
                                                                    color="blue"
                                                                    autocomplete="false"
                                                                    class="mt-4"
                                                                />
                                                            </v-col>
                                                            <v-col cols="12" sm="6">
                                                                <v-text-field
                                                                    label="Last Name"
                                                                    outlined
                                                                    dense
                                                                    color="blue"
                                                                    autocomplete="false"
                                                                    class="mt-4"
                                                                />
                                                            </v-col>
                                                        </v-row>
                                                        <v-text-field
                                                            label="Email"
                                                            outlined
                                                            dense
                                                            color="blue"
                                                            autocomplete="false"
                                                        />
                                                        <v-text-field
                                                            label="Password"
                                                            outlined
                                                            dense
                                                            color="blue"
                                                            autocomplete="false"
                                                            type="password"
                                                        />
                                                        <v-row>
                                                            <v-col cols="12" sm="7">
                                                                <v-checkbox
                                                                    label="I Accept AAE"
                                                                    class="mt-n1"
                                                                    color="blue"
                                                                >
                                                                </v-checkbox>
                                                            </v-col>
                                                            <v-col cols="12" sm="5">
                                                                <span
                                                                    class="caption blue--text ml-n4"
                                                                    style="font-family: &quot;montserrat&quot;"
                                                                    >Terms &Conditions</span
                                                                >
                                                            </v-col>
                                                        </v-row>
                                                        <v-btn color="blue" dark block tile>Sign up</v-btn>

                                                        <h4
                                                            class="text-center grey--text mt-4 mb-3"
                                                            style="font-family: &quot;montserrat&quot;"
                                                        >
                                                            Or Sign up using
                                                        </h4>
                                                        <div
                                                            class="d-flex justify-space-between align-center mx-10 mb-11"
                                                        >
                                                            <v-btn depressed outlined color="grey">
                                                                <v-icon icon="mdi-google" color="red"></v-icon>
                                                            </v-btn>
                                                            <v-btn depressed outlined color="grey">
                                                                <v-icon icon="mdi-facebook" color="blue"></v-icon>
                                                            </v-btn>
                                                            <v-btn depressed outlined color="grey">
                                                                <v-icon icon="mdi-github" color="black"></v-icon>
                                                            </v-btn>
                                                        </div>
                                                    </v-col>
                                                </v-row>
                                            </v-card-text>
                                        </v-col>
                                    </v-row>
                                </v-window-item>
                            </v-window>
                        </v-card>
                    </v-col>
                </v-row>
            </v-container>
        </v-main>
    </v-app>
</template>

<script>
export default {
    data: () => ({
        step: 1,
    }),
    mounted() {
        if (this.$route.query.section === "signup") {
            this.step = 2;
        }
    },

    props: {
        source: String,
    },
};
</script>
<style scoped>
.v-application .rounded-bl-xl {
    border-bottom-left-radius: 300px !important;
    background-color: rgba(255, 240, 209, 0.8);
}
.v-application .rounded-br-xl {
    border-bottom-right-radius: 300px !important;
    background-color: rgba(255, 240, 209, 0.8);
}
</style>
