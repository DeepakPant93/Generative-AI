# Generative AI Applications Repository

Welcome to the **Generative AI Apps** repository! This repository contains various applications built using cutting-edge Generative AI models like OpenAI APIs, LangChain, DALL·E, and Whisper. These applications leverage the power of AI to create intelligent, interactive experiences such as Discord bots, image generation, and voice transcription.

## Table of Contents

- [Introduction](#introduction)
- [Applications](#applications)
  - [Discord Bot with AI Integration](#discord-bot-with-ai-integration)
  - [AI-Powered Image Generation (DALL·E)](#ai-powered-image-generation-dall-e)
  - [Speech-to-Text with Whisper](#speech-to-text-with-whisper)
  - [LangChain-Powered Text Processing](#langchain-powered-text-processing)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This repository is a collection of various applications that utilize generative AI models to deliver dynamic and intelligent experiences. From AI-powered bots on Discord to sophisticated image generation and voice transcription services, these applications showcase the versatility of Generative AI.

## Applications

### Discord Bot with AI Integration

A custom-built Discord bot that utilizes OpenAI APIs to interact with users in real-time. The bot can answer queries, generate images, and even transcribe voice messages.

- **Technologies**: Discord API, OpenAI APIs (ChatGPT, Whisper), LangChain
- **Features**:
  - Conversational AI with real-time responses
  - Image generation using DALL·E
  - Speech-to-text conversion with Whisper

### AI-Powered Image Generation (DALL·E)

An application that uses OpenAI’s DALL·E model to generate stunning and creative images based on textual input. Users can input prompts to get unique AI-generated images.

- **Technologies**: DALL·E API, Python, Flask
- **Features**:
  - Text-to-image generation
  - Customization of image outputs (resolution, style)

### Speech-to-Text with Whisper

A powerful speech-to-text transcription service that leverages OpenAI’s Whisper model to convert audio into accurate text.

- **Technologies**: Whisper API, FastAPI
- **Features**:
  - High-accuracy speech recognition
  - Real-time transcription for audio files

### LangChain-Powered Text Processing

An application utilizing LangChain to create complex chains of natural language processing tasks, such as text summarization, content generation, and more.

- **Technologies**: LangChain, OpenAI GPT models
- **Features**:
  - Complex text manipulation and generation
  - Multi-step workflows for document processing

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/your-username/Generative-AI.git
   cd Generative-AI
   ```

2. **Install dependencies**:

   Make sure you have `Python 3.8+` installed. Then, install required packages:

   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:

   Create a `.env` file in the root directory with the following:

   ```env
   OPENAI_API_KEY=your_openai_api_key
   ```

4. **Run the application**:

   ```bash
   python app.py
   ```

## Usage

- **Discord Bot**: Invite the bot to your Discord server and interact with it through natural language queries.
- **DALL·E App**: Enter text prompts to generate AI-created images.
- **Whisper Speech-to-Text**: Upload an audio file to receive a transcription.
- **LangChain App**: Input a document or text to process and watch how LangChain transforms it through multi-step workflows.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please open an issue or submit a pull request. Make sure to follow the contribution guidelines.

## License

This repository is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.