<template>
    <v-app>
        <v-main>
            <v-container>
                <v-row align="center" justify="center">
                    <v-col cols="12" sm="10">
                        <!-- TODO: do not span whole viewport width -->
                        <v-alert
                            v-for="alert in alerts"
                            :key="alert.id"
                            :type="alert.type"
                            closable
                            @close="removeAlert(alert.id)"
                        >
                            {{ alert.message }}
                        </v-alert>
                        <v-card class="elevation-6 mt-10 logincard">
                            <v-window v-model="step">
                                <v-window-item :value="1">
                                    <v-row>
                                        <v-col cols="12" md="6">
                                            <v-card-text class="mt-12">
                                                <h3 class="text-center" style="font-family: 'montserrat'">
                                                    Login in to Your Account
                                                </h3>
                                                <h4 class="text-center grey--text" style="font-family: 'Mukta Vaani'">
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
                                                            v-model="login_email"
                                                        />
                                                        <v-text-field
                                                            label="Password"
                                                            outlined
                                                            dense
                                                            color="blue"
                                                            autocomplete="false"
                                                            type="password"
                                                            v-model="login_password"
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
                                                                <!-- TODO: cursor not changing on hover -->
                                                                <span
                                                                    class="caption blue--text"
                                                                    @click="sendRecoveryEmail"
                                                                    >Forgot password</span
                                                                >
                                                            </v-col>
                                                        </v-row>
                                                        <v-btn color="blue" dark block tile @click="login">Login</v-btn>
                                                        <h4
                                                            class="text-center grey--text mt-4 mb-3"
                                                            style= "font-family: 'montserrat'"
                                                        >
                                                            Login with
                                                        </h4>
                                                        <div
                                                            class="d-flex justify-space-between align-center mx-2 mt-2 " 
                                                        >
                                                            <v-btn depressed outlined color="grey" @click="googleLogin" width="8.5vw">
                                                                <v-icon icon="mdi-google" color="red"></v-icon>
                                                            </v-btn>
                                                            <v-btn depressed outlined color="grey" @click="githubLogin" width="8.5vw">
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
                                                            font-family: 'montserrat';
                                                            color: #1e1e24;
                                                            margin-bottom: 10px;
                                                        "
                                                    >
                                                        Don't Have an Account Yet?
                                                    </h2>
                                                    <h4
                                                        class="text-center"
                                                        style="font-family: 'Mukta Vaani'; color: #1e1e24"
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
                                                            font-family: 'montserrat';
                                                            color: #1e1e24;
                                                            margin-bottom: 10px;
                                                        "
                                                    >
                                                        Already Signed up?
                                                    </h2>
                                                    <h4
                                                        class="text-center"
                                                        style="font-family: 'Mukta Vaani'; color: #1e1e24"
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
                                                <h3 class="text-center" style="font-family: 'montserrat'">
                                                    Sign Up for an Account
                                                </h3>
                                                <h5 class="text-center grey--text" style="font-family: 'Mukta Vaani'">
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
                                                                    v-model="signup_first_name"
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
                                                                    v-model="signup_last_name"
                                                                />
                                                            </v-col>
                                                        </v-row>
                                                        <v-text-field
                                                            label="Email"
                                                            outlined
                                                            dense
                                                            color="blue"
                                                            autocomplete="false"
                                                            v-model="signup_email"
                                                        />
                                                        <v-text-field
                                                            label="Password"
                                                            outlined
                                                            dense
                                                            color="blue"
                                                            autocomplete="false"
                                                            type="password"
                                                            v-model="signup_password"
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
                                                                    style="font-family: 'montserrat'"
                                                                    >Terms &Conditions</span
                                                                >
                                                            </v-col>
                                                        </v-row>
                                                        <v-btn color="blue" dark block tile @click="signup"
                                                            >Sign up</v-btn
                                                        >
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
import { useUserStore } from "@/stores/user";
import { auth } from "@/firebasehandler/auth";
import {
    getAuth,
    createUserWithEmailAndPassword,
    signInWithEmailAndPassword,
    updateProfile,
    GoogleAuthProvider,
    GithubAuthProvider,
    signInWithPopup,
    sendPasswordResetEmail,
} from "firebase/auth";

export default {
    data: () => ({
        step: 1,
        login_email: "",
        login_password: "",
        signup_first_name: "",
        signup_last_name: "",
        signup_email: "",
        signup_password: "",

        alerts: [],
    }),
    methods: {
        addAlert(type, message) {
            const alert = {
                id: this.alerts.length,
                type,
                message,
            };
            this.alerts.push(alert);

            // Automatically remove the alert after 5 seconds
            setTimeout(() => {
                this.removeAlert(alert.id);
            }, 5000);
        },
        removeAlert(alertId) {
            this.alerts = this.alerts.filter((alert) => alert.id !== alertId);
        },
        login() {
            // The email/password login method
            const store = useUserStore();

            signInWithEmailAndPassword(auth, this.login_email, this.login_password)
                .then((userCredential) => {
                    const user = userCredential.user;
                    store.login(user);
                    this.addAlert("success", "Login successful!");
                    this.$router.push("/dashboard");
                })
                .catch((error) => {
                    this.addAlert("error", error.message);
                    console.log(error);
                });
        },
        googleLogin() {
            // The Google login method
            const store = useUserStore();
            const provider = new GoogleAuthProvider();
            signInWithPopup(auth, provider)
                .then((result) => {
                    const user = result.user;
                    store.login(user);
                    this.addAlert("success", "Login successful!");
                    this.$router.push("/dashboard");
                })
                .catch((error) => {
                    this.addAlert("error", error.message);
                });
        },
        githubLogin() {
            // The Github login method
            const store = useUserStore();
            const provider = new GithubAuthProvider();
            signInWithPopup(auth, provider)
                .then((result) => {
                    const user = result.user;
                    store.login(user);
                    this.addAlert("success", "Login successful!");
                    this.$router.push("/dashboard");
                })
                .catch((error) => {
                    this.addAlert("error", error.message);
                });
        },
        signup() {
            // Create a new user account
            const store = useUserStore();

            createUserWithEmailAndPassword(auth, this.signup_email, this.signup_password)
                .then((userCredential) => {
                    const user = userCredential.user;
                    const auth = getAuth();

                    updateProfile(auth.currentUser, {
                        displayName: `${this.signup_first_name} ${this.signup_last_name}`,
                    })
                        .then(() => {
                            console.log("User profile updated successfully");
                        })
                        .catch((error) => {
                            console.log(error);
                        });
                    store.login(user);
                    this.addAlert("success", "Account created successfully!");
                    this.$router.push("/dashboard");
                })
                .catch((error) => {
                    this.addAlert("error", error.message);
                });
        },
        sendRecoveryEmail() {
            sendPasswordResetEmail(auth, this.login_email)
                .then(() => {
                    this.addAlert("success", "Password reset email sent! Please check your inbox.");
                })
                .catch((error) => {
                    this.addAlert("error", error.message);
                });
        },
    },
    mounted() {
        const store = useUserStore();

        if (store.isLoggedIn) {
            this.$router.push("/dashboard");
        }

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
    max-height: 80vh;
    min-height: 80vh;
}
.v-application .rounded-br-xl {
    border-bottom-right-radius: 300px !important;
    background-color: rgba(255, 240, 209, 0.8);
    max-height: 80vh;
    min-height: 80vh;
}
.logincard {
    max-height: 75vh;
    min-height: 75vh;
    min-width: 60vw;
    max-width: 70vw;
    
}
</style>
