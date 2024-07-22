<template>
    <v-app>
        <v-main>
            <v-fill>
                <v-billtitle>Billing Information</v-billtitle>
                <v-container>
                    <v-form>
                        <v-radio-group v-model="paymentMethod" label="Select Payment Method" required>
                            <v-radio label="Gcash" value="gcash"></v-radio>
                            <v-radio label="Bank Transfer" value="bankTransfer"></v-radio>
                        </v-radio-group>

                        <v-container v-if="paymentMethod === 'gcash'">
                            <v-text-field v-model="gcashNumber" label="Gcash Number" required></v-text-field>
                            <v-text-field v-model="gcashName" label="Name" required></v-text-field>
                            <v-text-field v-model="gcashRefNumber" label="Reference Number" required></v-text-field>
                        </v-container>

                        <v-container v-if="paymentMethod === 'bankTransfer'">
                            <v-text-field v-model="bankAccountNumber" label="Account Number" required></v-text-field>
                            <v-text-field v-model="bankAccountName" label="Account Name" required></v-text-field>
                            <v-text-field v-model="bankRefNumber" label="Reference Number" required></v-text-field>
                        </v-container>

                        <v-btn class="btnbill" @click="submit">Submit</v-btn>
                        <v-btn @click="showQRCode = true" class="btnbill">Show QR Code</v-btn>

                        <v-dialog v-model="showQRCode" width="30vw" max-width="50vw">
                            <v-card>
                                <v-card-title>QR Code</v-card-title>
                                <v-card-text>
                                    <v-img
                                        :src="qrCodeSrc"
                                        height="25vh"
                                        width="25vw"
                                        max-width="40vw"
                                        v-if="qrCodeSrc"
                                    ></v-img>
                                    <div v-if="paymentMethod === 'gcash'">
                                        <v-payinfo> Name : Amplify </v-payinfo>
                                        <v-payinfo> Gcash Number : 094544248455 </v-payinfo>
                                    </div>
                                    <div v-else-if="paymentMethod === 'bankTransfer'">
                                        <v-payinfo> Bank : RCBC Bankard </v-payinfo>
                                        <v-payinfo> Account Name : Amplify </v-payinfo>
                                        <v-payinfo> Account Number : 094544248455 </v-payinfo>
                                    </div>
                                    <div v-else>No QR Code available</div>
                                </v-card-text>
                                <v-card-actions>
                                    <v-btn color="primary" text @click="showQRCode = false">Close</v-btn>
                                </v-card-actions>
                            </v-card>
                        </v-dialog>

                        <v-dialog v-model="showProcessing" max-width="500">
                            <v-card background-color="#1e1e24">
                                <v-card-title>Processing Payment</v-card-title>
                                <v-card-text>Please wait for the email confirmation.</v-card-text>
                                <v-card-actions>
                                    <v-btn color="#566498" text @click="closeProcessingDialog">Close</v-btn>
                                </v-card-actions>
                            </v-card>
                        </v-dialog>
                    </v-form>
                </v-container>
            </v-fill>
        </v-main>
    </v-app>
</template>

<script>
export default {
    data() {
        return {
            paymentMethod: "",
            gcashNumber: "",
            gcashName: "",
            gcashRefNumber: "",
            bankAccountNumber: "",
            bankAccountName: "",
            bankRefNumber: "",
            showQRCode: false,
            qrCodeSrc: "",
            showProcessing: false,
        };
    },
    watch: {
        paymentMethod(newVal) {
            this.qrCodeSrc =
                newVal === "gcash"
                    ? "https://via.placeholder.com/150?text=Gcash+QR"
                    : "https://via.placeholder.com/150?text=Bank+QR";
        },
    },
    methods: {
        submit() {
            const paymentData = {
                method: this.paymentMethod,
                details:
                    this.paymentMethod === "gcash"
                        ? {
                              number: this.gcashNumber,
                              name: this.gcashName,
                              reference: this.gcashRefNumber,
                          }
                        : {
                              accountNumber: this.bankAccountNumber,
                              accountName: this.bankAccountName,
                              reference: this.bankRefNumber,
                          },
            };

            console.log("Payment Data:", paymentData);
            this.showProcessing = true;
            // Perform your form submission or processing logic here
        },
        closeProcessingDialog() {
            this.showProcessing = false;
            this.paymentMethod = "";
            this.gcashNumber = "";
            this.gcashName = "";
            this.gcashRefNumber = "";
            this.bankAccountNumber = "";
            this.bankAccountName = "";
            this.bankRefNumber = "";
        },
    },
};
</script>

<style scoped>
v-fill {
    color: #000;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    height: 80vh;
    width: 80vw;
    background-color: beige;
    margin-left: 10vw;
    margin-top: 5vh;
    border-radius: 5px;
}

v-fill,
v-form {
    color: #000;
}

v-form {
    width: 100%;
    max-width: 400px;
    padding: 20px;
    border-radius: 5px;
    color: #000;
}
v-payinfo {
    color: beige;
    font-size: 1rem;
    font-family: poppins;
    margin-top: 20px;
    margin-left: 10px;
    display: flex;
    flex-direction: column;
    align-items: center;
}
.btnbill {
    background-color: #566498;
    color: beige;
    margin-top: 20px;
    margin-left: 10px;
}
v-billtitle {
    font-size: 3rem;
    font-family: "Montserrat", sans-serif;
    color: #566498;
    text-align: center;
    font-weight: bolder;
}
</style>
