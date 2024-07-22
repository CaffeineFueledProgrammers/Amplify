<template>
    <v-app>
        <home />
        <AmplifyKeyFeat />
        <AiProcess />
        <flashcard />
        <sharecollab />
    </v-app>
</template>

<script>
import { useRouter } from "vue-router";
import { useUserStore } from "@/stores/user";

export default {
    setup() {
        const router = useRouter();
        const store = useUserStore();
        if (store.isLoggedIn) {
            router.push("/dashboard");
        }
    },
};
</script>
