import { initializeApp } from "firebase/app";
import { getFirestore, collection } from "firebase/firestore";

const config = {
    apiKey: "AIzaSyDxW3e9NfW75Oly4d9aFuWhEZmAW6KNS18",
    authDomain: "amplify-9dde5.firebaseapp.com",
    projectId: "amplify-9dde5",
    storageBucket: "amplify-9dde5.appspot.com",
    messagingSenderId: "844563357822",
    appId: "1:844563357822:web:ec31cd57172537b6e2f82f",
    measurementId: "G-GRFB6F8JNF",
};

export const firebaseApp = initializeApp(config);

export const db = getFirestore(firebaseApp);
