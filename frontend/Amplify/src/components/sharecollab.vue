<template>
    <v-app>
        <v-main>
            <v-share class="d-flex  flex pa-3 ma-2">
                <v-note>
                <v-sheet rounded="rounded" class="mx-auto block justify-start align-start opacity-0.5">
                    <v-note_title>
                    <h2>NOTE</h2>
                    <h1>ADVANTAGE OF DIGITAL NOTE TAKING</h1>
                    </v-note_title>
                    <div class="note_content">
                        Digital note-taking has transformed the way individuals capture, organize, and utilize
                        information. Leveraging technology, it offers a plethora of advantages over traditional
                        pen-and-paper methods. Here are some of the most significant benefits of digital note-taking:<br /> <br/>                        Features like tagging, categorization, and folders help in systematically organizing
                        information. Moreover, the powerful search functions in these apps enable users to quickly
                        locate specific notes or keywords, making the retrieval of information far
                    </div>
                    <v-collaborators><h2>Collaborators</h2>
                        <v-sheet :elevation="6" color= "rgba(255, 240, 209, 0.4)" height="200" class=" d-flex align-center justify-center ma-0 ">
                            <img src="" />
                            
                            <v-btn >
                                <v-icon>mdi-history</v-icon>

                                <span>User 1</span>
                            </v-btn>

                            <v-btn >
                                <v-icon>mdi-heart</v-icon>

                                <span>User 2</span>
                            </v-btn>

                            <v-btn >
                                <v-icon>mdi-map-marker</v-icon>

                                <span>User 3</span>
                            </v-btn>
                            <v-btn >
                                <v-icon> mdi-share </v-icon>

                                <span>Invite</span>
                            </v-btn>
                        </v-sheet>
                    </v-collaborators>
                </v-sheet>
                </v-note>
                <v-sharetxt class= "d-flex flex-column" >
                <div class="share_title">
                <h1>Sharing</h1>
                <h1>Collaboration</h1>
                <h1>System</h1>
                </div>
                <div class="note_content">
                    Share your created notes with fellow Amplify users for viewing, and optionally, editing for
                    real-time collaboration. Amplify also allows you to publish your notes publicly to make them
                    accessible to internet users worldwide.
                </div>
                </v-sharetxt>
            </v-share>
        </v-main> 
        <AppFooter/>
    </v-app>
      
</template>
<style>

v-note{
    display: block;
    width: 50vw;
    max-width: 50vw;
    color:#1e1e24;
    opacity: 0.7;
}
v-note_title h1 {
    font-size: 1.5rem;
    padding-top: 10%;
    text-align: center;
}
v-note_title h2 {
    font-size: 1rem;
 padding-top: 5%;
 padding-left:5%;
    text-align: start;
}
v-share .note_content {
    font-size: 1rem;
   margin-top: 10%;
   padding-left: 10%;
   padding-right: 10%;
}

v-collaborators {
    display: block;
    margin-top: 15%;
    width: 50vw;
    min-width: 50vw;
    color: rgba(255, 240, 209, 0.4);
    

}
v-collaborators v-btn{
    align-items: center;
    justify-content: center;
   margin-left: 5%;
}
v-sharetxt {
    display: block;
    width: 40vw;
    min-width: 40vw;
    margin-left: 5%;
    align-self: center;}

v-sharetxt h1 {
    font-size: 3rem;
    text-align: start;
 
}
v-sharetxt .note_content {
    font-size: 1rem;
    margin-top: 10%;
}

</style>

