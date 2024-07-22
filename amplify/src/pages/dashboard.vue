<template>
    <v-app>
        <v-main>
            <sidebar />
        </v-main>
    </v-app>
</template>

<script>
import { useRouter } from "vue-router";
import { useUserStore } from "@/stores/user";

export default {
    setup() {
        const router = useRouter();
        const store = useUserStore();

        if (!store.isLoggedIn) {
            router.push("/");
        }
    },
};
</script>
