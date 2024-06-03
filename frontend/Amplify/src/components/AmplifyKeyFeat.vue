<template>
    <v-app>
        <v-main >
        
            <v-keyfeat class="d-flex align-center flex-column">
               
                   <v-keyfeat_title class="d-flex justify-center">
             <img src="@/assets/A.png" alt="Amplify Logo" class="logo" />

                <v-keyfeattxt class="d-flex align-center flex-column ">
                <div class="mplify">MPLIFY
                      </div> 
                <div class="keyfeatures">Key Features</div>
                <b class="download-now">DOWNLOAD NOW</b>
                </v-keyfeattxt>
            </v-keyfeat_title>
                <div class="d-flex align-center justify-center">
                    <v-row >
                        <v-col order="1">
                                <div class="d-flex align-center justify-center flex-column pa-2 ma-2">
                                    <p class="title">Enhanced Note-Taking Note-Taking</p>
                                    <div class="key_description">
                                        Write your notes in Markdown, and Amplify will automatically organize and
                                        enhance them.
                                    </div>
                                </div>
                        </v-col>
                        <v-col order="2">
                            
                                <div class="d-flex align-center justify-center flex-column pa-2 ma-2">
                                    <p class="title">Sharing and Collaboration</p>

                                    <div class="key_description">
                                        Share your notes and flashcards with other Amplify users or publish them online.
                                    </div>
                                </div>
                         
                        </v-col>

                        <v-col order="3">
                            
                                <div class="d-flex align-center justify-center flex-column pa-2 ma-2">
                                    <p class="title">Intelligent Flashcard</p>
                                    <div class="key_description">
                                        Amplify will analyze your notes to generate Anki flashcards.
                                    </div>
                                </div>
                        </v-col>
                    </v-row>
                </div>
            </v-keyfeat>
        </v-main>
    </v-app>
</template>
<style>
main {
    min-width: 100vw;
    max-height: 100vh;
    background-color: #1e1e24;
}

.title{
    font-size: 2rem;
    color: #fff;
    text-align: center;

}
.key_description {
    font-size: 1.2rem;
    color: #a8a8a8;
    text-align: center;
}
.mplify {
    margin-top: 50%;
    font-size: 4rem;
    color: #ffffff;
}

</style>
