<template>
    <v-app>
        <v-main >
        
            <v-keyfeat class="d-flex align-center flex-column">
               
                   <v-keyfeat_title class="d-flex justify-center">
             <img src="@/assets/A.png" alt="Amplify Logo" class="logo" />

                <v-keyfeattxt class="d-flex align-center flex-column ">
                <v-keyfeattxt2 class="d-flex align-center ">
                <div class="mplify">MPLIFY</div> 
                <div class="keyfeatures">KeyFeatures</div>
                </v-keyfeattxt2>
                <b class="download_now">DOWNLOAD NOW</b>
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
                                <div class="d-flex align-center justify-center flex-column pa-2 ma-2" style="min-height: 50%;">
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
@import url(https://fonts.googleapis.com/css2?family=Montserrat:wght@300;700;800;900&display=swap);
@import url(https://fonts.googleapis.com/css2?family=MuktaVaani:wght@400;500;600;700;800&display=swap);
@import url(https://fonts.googleapis.com/css2?family=HindGuntur:wght@400;700&display=swap);

main {
    min-width: 100vw;
    max-height: 100vh;
    background-color: #16171b;
}

.title{
    font-size: 1.5rem;
    font-family: 'Montserrat',sans-serif ;
    font-weight: bolder;
    color: #fff;
    text-align: center;
    

}

.key_description {
    font-size: 1.2rem;
    font-family: 'MuktaVaani',sans-serif ;
    color: #a8a8a8;
    text-align: center;

}
.mplify {
    font-family: 'Montserrat',sans-serif ;
    font-weight: bolder;
    margin-top: 50%;
    font-size: 4rem;
    color: #ffffff;
}
.keyfeatures {
    font-family: 'HindGuntur',sans-serif ;
    font-size: 2rem;
    margin-top: 50%;
margin-left: 3%;
    color: #ffffff;
}
.download_now{
    font-family: 'HindGuntur',sans-serif ;
    font-size: 1.5rem;
    color: #ffffff;
    cursor: pointer;
}
.download_now:hover{
    
    color:#71b0e4;
}

</style>
