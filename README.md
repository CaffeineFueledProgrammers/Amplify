<div align="center">
    <img src="https://github.com/CaffeineFueledProgrammers/Amplify/raw/main/amplify_frontend/src/assets/A.png" alt="Amplify logo" width="128" />
    <h1>Amplify</h1>
</div>

<p align="center"><i>AI-Powered Note-Taking for Students.</i></p>

**Amplify** is a note-taking application inspired by [Obsidian](https://obsidian.md/) and [AnyType](https://anytype.io/) designed specifically for students. It integrates seamlessly with existing Google [Workspace](https://workspace.google.com/)/[Classroom](https://classroom.google.com/) features while offering an AI-powered enhancement layer powered by [OpenAI](https://openai.com/).

## Features

> **Roadmap**
>
> -   [x] Homepage
> -   [ ] Login System
>     -   [ ] Sharing/Collaboration System
>     -   [ ] Text/Note Editor
>         -   [ ] AI Notes Processor
>             -   [ ] Grammar Checking (via LanguageTool)
>             -   [ ] Paraphrasing Assistant (via OpenAI)
>             -   [ ] Definition of Terms (via Free Dictionary/OpenAI)
>             -   [ ] Information retrieval/Further Reading (via OpenAI)
>         -   [ ] Intelligent Flashcard Generation (via OpenAI/Anki)

-   **Enhanced Note-Taking**: The students will take notes as they normally would, using text, images, or even voice recordings.
-   **AI Processing**: The system will use artificial intelligence to process the notes. This could involve:
    -   _Summarization_: Generating a summary of keypoints.
        -   _Structure detection_: Automatically organizing notes based on identified headings and subheadings.
        -   _Definition of Terms_: Identifying important terms and providing short definitions.
        -   _Information retrieval/Further Reading_: Finding relevant web content related to the notes.
-   **Intelligent Flashcard Generation:** Amplify analyzes notes and identifies key concepts. After that, it will automatically generate [Anki flashcards](https://apps.ankiweb.net/), a popular spaced repetition system for effective memorization.
-   **Sharing and Collaboration:** Users can share notes with classmates for group projects or study sessions. Collaborative features might include real-time editing and annotation.

## Development Setup

### Requirements

-   **Back-End**
    -   Python >= 3.10
    -   Poetry >= 1.8.3
-   **Front-end**
    -   NodeJS >= 22.2.0
    -   Node Package Manager (NPM) >= 10.7.0

### Back-end Development Setup

1. Clone the repository.

    ```bash
    git clone https://github.com/CaffeineFueledProgrammers/Amplify.git
    cd Amplify
    ```

2. Install the requirements.

    ```bash
    poetry install
    ```

3. Run the development server.

    ```bash
    poetry run python -m amplify_backend dev
    ```

4. The server will be running at `http://localhost:8081`.

### Front-end Development Setup

1. Clone the repository.

    ```bash
    git clone https://github.com/CaffeineFueledProgrammers/Amplify.git
    cd Amplify/amplify_frontend
    ```

2. Install the requirements.

    ```bash
    npm install
    ```

3. Run the development server.

    ```bash
    npm run dev
    ```

4. The server will be running at `http://localhost:8080`.
