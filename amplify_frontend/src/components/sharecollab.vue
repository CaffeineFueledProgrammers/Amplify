<template>
    <v-app>
        <v-main>
            <v-share class="d-flex pa-3 ma-2">  
                 <v-sharetxt class="d-flex flex-column">
                    <div class="share_title">
                        <h1>Sharing</h1>
                        <h1 class="collab">Collaboration</h1>
                        <h1>System</h1>
                    </div>
                    <div class="note_content">
                        Share your created notes with fellow Amplify users for viewing, and optionally, editing for
                        real-time collaboration. Amplify also allows you to publish your notes publicly to make them
                        accessible to internet users worldwide.
                    </div>
                </v-sharetxt>
                <v-note   data-aos="fade-right"  data-aos-delay="200" data-aos-once="false"  data-aos-duration="1000" >
                    <v-sheet rounded="rounded" class="mx-auto block justify-start align-start opacity-0.5" >
                        <v-note_title>
                            <h2>NOTE</h2>
                            <h1>ADVANTAGE OF DIGITAL NOTE TAKING</h1>
                        </v-note_title>
                        <div class="note_content">
                            Digital note-taking has transformed the way individuals capture, organize, and utilize
                            information. Leveraging technology, it offers a plethora of advantages over traditional
                            pen-and-paper methods. Here are some of the most significant benefits of digital
                            note-taking:<br />
                            <br />
                            Features like tagging, categorization, and folders help in systematically organizing
                            information. Moreover, the powerful search functions in these apps enable users to quickly
                            locate specific notes or keywords, making the retrieval of information far
                        </div>
                        <v-collaborators>
                            <v-sheet color="#5e6275" elevation="3" rounded="lg">
                                <v-tabs
                                    v-model="tab"
                                    :items="tabs"
                                    align-tabs="center"
                                    color="white"
                                    height="60"
                                    slider-color="#0f1322"
                                >
                                    <template v-slot:tab="{ item }">
                                        <v-tab
                                            :prepend-icon="item.icon"
                                            :text="item.text"
                                            :value="item.value"
                                            class="text-none"
                                        ></v-tab>
                                    </template>

                                    <template v-slot:item="{ item }">
                                        <v-tabs-window-item
                                            :value="item.value"
                                            class="pa-01 justify-center align-center collab_tab"
                                            style="height: 150px"
                                        >
                                            <template v-if="item.value === 'tab-1'">
                                                <div class="d-flex justify-center align-center" style="margin-top: 5%">
                                                    <v-btn class="mr-5">
                                                        <v-icon>mdi-account</v-icon>
                                                        <span>User 1</span>
                                                    </v-btn>
                                                    <v-btn class="mr-5">
                                                        <v-icon>mdi-account</v-icon>
                                                        <span>User 2</span>
                                                    </v-btn>
                                                    <v-btn class="mr-5">
                                                        <v-icon>mdi-account</v-icon>
                                                        <span>User 3</span>
                                                    </v-btn>
                                                    <v-btn class="mr-5">
                                                        <v-icon>mdi-share</v-icon>
                                                        <span>Invite</span>
                                                    </v-btn>
                                                </div>
                                            </template>
                                            <template v-else>
                                                <!-- Content for tab 2 (Shared with you) -->
                                                <v-list>
                                                    <v-list-item v-for="user in users" :key="user">
                                                        <v-list-item-icon>
                                                            <v-icon icon="md:folder_open"></v-icon>
                                                        </v-list-item-icon>
                                                        <v-list-item-content>
                                                            <v-list-item-title>{{ user.name }}</v-list-item-title>
                                                        </v-list-item-content>
                                                    </v-list-item>
                                                    <v-list-item> </v-list-item>
                                                </v-list>
                                            </template>
                                        </v-tabs-window-item>
                                    </template>
                                </v-tabs>
                            </v-sheet>
                        </v-collaborators>
                    </v-sheet>
                </v-note>
             
            </v-share>
        </v-main>
        <AppFooter />
    </v-app>
</template>
<script>
export default {
    data: () => ({
        tab: "tab-1",
        tabs: [
            {
                icon: "mdi-book-open-page-variant",
                text: "COLLABORATION",
                value: "tab-1",
            },
            {
                icon: "mdi-handshake-outline",
                text: "SHARED WITH YOU",
                value: "tab-2",
            },
        ],
        users: [
            { id: 1, name: "NOTE 05/24/24" },
            { id: 2, name: "NOTE 05/28/24" },
            { id: 3, name: "NOTE 06/03/24" },
        ],
    }),
};
</script>

<style>
v-note {
    display: block;
    width: 40vw;
    max-width: 40vw;
    margin-left:10% ;
    color: #16171b;
}
v-note_title h1 {
    font-size: 1.5rem;
    padding-top: 10%;
    text-align: center;
}
v-note_title h2 {
    font-size: 1rem;
    padding-top: 5%;
    padding-left: 5%;
    text-align: start;
}
v-note .note_content {
    font-size: 1rem;
    margin-top: 10%;
    padding-left: 10%;
    padding-right: 10%;
}
v-collaborators {
    display: block;
    margin-top: 15%;
    width: 40vw;
    min-width: 40vw;
    color: #5e6275;
}
v-collaborators h2 {
    position: relative;
    top: 5px;
    color: #1e1e24;
    font-size: 1.2rem;
    font-family: "Montserrat", sans-serif;
    text-align: center;
    width: 25%;
    background-color: #5e6275;
    border-radius: 10%;
}
v-collaborators v-btn {
    align-items: center;
    justify-content: center;
    padding-left: 50%;
    margin-right: 50%;
}
v-sharetxt {
    display: block;
    width: 40vw;
    min-width: 40vw;
    margin-left: 5%;
    margin-top: 5%;
}
v-sharetxt h1 {
    font-family: "Montserrat", sans-serif;
    font-size: 4rem;
    font-weight: 900;
    text-align: start;
    position: relative;
}
v-sharetxt .note_content {
    font-family: "MuktaVaani", sans-serif;
    font-size: 1.2 rem;
    margin-top: 10%;
}
.collab:hover {
    color: #71b0e4;
}
@media (max-width: 600px) {
 v-share{
    flex-direction: column;
 }
 v-note{
    margin-left:2% ;
    margin-top: 5%;
     margin-bottom: 5%;
    width: 80vw;
    max-width: 80vw;
    height: 50vw;
    max-height: 50vw;
 }

v-note_title h1 {
    font-size: 1rem;
    padding-top: 5%;
    text-align: center;
}
v-note_title h2 {
    font-size: 0.5rem;
    padding-top: 3%;
}
v-note .note_content {
    font-size: 0.5rem;
    margin-top: 5%;
}
v-collaborators {
    display: block;
    margin-top: 5%;
    width: 80vw;
    height: 5vw;
    max-height: 5vw;
    color: #5e6275;
}
v-collaborators h2 {
    font-size: 0.5rem;
}
v-collaborators v-btn {
    align-items: center;
    justify-content: center;
    height: 3%;

}

v-sharetxt h1 {
    width: 80vw;
   margin-top: 0%;
    font-size: 3rem;

}
v-sharetxt .note_content {
  width: 80vw;
    font-size: 0.8rem;

}
v-tabs-window-item{
visibility:hidden;

}
}

@media (min-width: 1024px) {
    v-note {
        width: 40vw;
        max-width: 40vw;
    }
    v-collaborators {
        width: 40vw;
        min-width: 40vw;
    }
    v-sharetxt {
        width: 40vw;
        min-width: 40vw;
    }
}
</style>
