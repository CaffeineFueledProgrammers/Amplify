import { getAuth } from "firebase/auth";
import { firebaseApp } from "@/firebasehandler";

// Initialize Firebase Authentication and get a reference to the service
export const auth = getAuth(firebaseApp);
