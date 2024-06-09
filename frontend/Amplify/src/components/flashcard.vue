<template>
    <v-app> 
        <div id="app">
            <img src="@/assets/bg@flash.png" class="bgflash">
            <h1 class=" d-flex justify-center align-center">Generate Flashcards</h1>
            <v-container class="flash" >
                <v-row class=" d-flex justify-center align-center"  data-aos="fade-up"  data-aos-once="false" data-aos-duration="1000" >
                    <v-col v-for="(flashcard, index) in flashcards" :key="index" cols="2" md="6">
                        <div class="flashcard" @mouseover="flipCard(index)" @mouseleave="flipCard(index)">
                            <div class="card-inner" :class="{ flipped: flashcard.flipped }">
                                <div class="card-front">
                                    {{ flashcard.front }}
                                </div>
                                <div class="card-back">
                                    {{ flashcard.back }}
                                </div>
                            </div>
                        </div>
                    </v-col>
                </v-row>
            </v-container>
        </div>
    </v-app>
</template>

<script>

    import { onMounted } from 'vue';
import AOS from 'aos'
import 'aos/dist/aos.css'
export default {
  name: 'App',
  setup() {
    onMounted(() => {
      AOS.init();
    });
  },
  
    name: "App",
    data() {
        return {
            flashcards: [
                {
                    front: "ANKI SUPPORT",
                    back: "  Amplify allows you to export the flashcards into Anki-supported decks so you can integrate it with your Anki workflow.",
                    flipped: false,
                },
                {
                    front: "INTELLIGENT FLASHCARD GENERATION",
                    back: " Amplify helps you generate flashcards for you to use based on your notes.",
                    flipped: false,
                },
            ],
        };
    },
    methods: {
        flipCard(index) {
            this.flashcards[index].flipped = !this.flashcards[index].flipped;
        },
    },
};



</script>

<style scoped>
#app {
    background-color:#131419;
    height: 100vh;
}
#app h1 {
 
    font-size: 5rem;
    font-family: "Montserrat", sans-serif;
    font-weight: 800;
    color: #fff;
    text-align: center;
    margin-bottom:5% ; 
    margin-top: 5%;
}
.flashcard {
    width: 500px;
    height: 350px;
    perspective: 1000px;
    margin: 10px auto;
}
.card-inner {
    position: relative;
    width: 100%;
    height: 100%;
    text-align: center;
    transition: transform 0.6s;
    transform-style: preserve-3d;
}
.card-inner.flipped {
    transform: rotateX(180deg);
}
.card-front,
.card-back {
    position: absolute;
    width: 100%;
    height: 100%;
    backface-visibility: hidden;
    display: flex;
    justify-content: center;
    align-items: center;
}
.card-front {
    background: rgb(69, 80, 135);
    background: radial-gradient(circle, rgba(69, 80, 135, 1) 6%, rgba(16, 16, 28, 1) 75%);
    font-family: "Montserrat", sans-serif;
    font-size: 1rem;
    font-weight: 600;
}
.card-back {
    background: #1e1e24;
    transform: rotateX(180deg);
    font-family: "Montserrat", sans-serif;

    font-size: 1rem;
    font-weight: 200;
    font-optical-sizing: auto;
}
.bgflash{
    position: absolute;
    top: -20%;
    right: -20%;
    width: 100%;
    height: 100%;
    z-index: 0;

}
@media screen and (max-width: 800px){
    .flashcard {
        width:300px;
        height: 200px;
      
    }
.flash{
      display: flex;
        flex-direction: column;
}
}
</style>
