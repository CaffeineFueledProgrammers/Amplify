<template>
    <v-card class="my-10" max-width="100vw">
        <v-list :items="items"></v-list>
    </v-card>
</template>
<script>
export default {
    data: () => ({
        items: [
            {
                icon: "mdi-card-multiple-outline",
                title: "Anki Flahcards",
                value: 0,
            },
            {
                icon: "mdi-file-multiple",
                title: "Item #1",
                value: 1,
            },
            {
                icon: "mdi-file-multiple",
                title: "Item #2",
                value: 2,
            },
            {
                icon: "mdi-file-multiple",
                title: "Item #3",
                value: 3,
            },
        ],
    }),
};
</script>
