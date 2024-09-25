# YogaGPT - Discord Bot for Yoga & Meditation

Welcome to **YogaGPT**, a powerful AI-based Discord bot designed to help users with personalized yoga and meditation suggestions. This bot integrates with the ChatGPT API to provide real-time responses tailored to your well-being needs.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Setup](#setup)
- [Usage](#usage)
- [Commands](#commands)
- [Contributing](#contributing)
- [License](#license)

## Introduction

YogaGPT is your virtual yoga guide on Discord. Whether you’re looking for yoga postures to relieve stress, meditation techniques for relaxation, or suggestions on improving your overall wellness, YogaGPT is here to assist. Powered by OpenAI's ChatGPT API, it provides intelligent, dynamic, and thoughtful responses tailored to your unique needs.

## Features

- **Personalized Yoga Poses**: Get suggestions on yoga poses based on specific needs like stress relief, back pain, flexibility, or energy boost.
- **Guided Meditation**: Receive recommendations for meditation practices to improve mindfulness, focus, or relaxation.
- **Daily Wellness Tips**: YogaGPT can provide daily insights and wellness tips to promote mental and physical well-being.
- **Easy Discord Integration**: Interact seamlessly with YogaGPT in any Discord server, providing on-demand advice.

## Setup

Follow these steps to set up YogaGPT in your own Discord server:

1. **Clone the repository**:

   ```bash
   git clone https://github.com/your-username/YogaGPT.git
   cd YogaGPT
   ```

2. **Install dependencies**:

   Make sure you have `Python 3.8+` installed. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:

   Create a `.env` file in the root directory and add the following:

   ```env
   DISCORD_YOGAGPT_SECRET=your_discord_bot_token
   OPENAI_API_KEY=your_openai_api_key
   ```

4. **Run the bot**:

   Start YogaGPT by running:

   ```bash
   python3 main.py
   ```

5. **Invite the bot to your Discord server**:

   Generate an invite link for the bot and add it to your server.

   ```bash
   https://discord.com/oauth2/authorize?client_id=1287832751357165569&permissions=66624&integration_type=0&scope=bot
   ```

6. **Run the bot using Docker**:

   Start the bot using Docker.

    ```bash
    docker run -d \
     --name yoga-gpt \
     -e NAME=yoga-gpt \
     -e DISCORD_BOT_TOKEN=your_discord_bot_token \
     -e OPENAI_API_KEY=your_openai_api_key \
     deepak93p/yoga-gpt:latest
      ```
For setup instructions, see [Setup Guide](SETUP.md).

## Usage

Once YogaGPT is added to your Discord server, simply type commands in the chat to get yoga and meditation suggestions. YogaGPT responds with thoughtful and personalized recommendations based on your input.

### Commands

- **`/yoga [issue]`**: Get yoga pose suggestions for a specific issue (e.g., back pain, stress relief).
  - Example: `/yoga stress`
  
- **`/meditate [type]`**: Get a guided meditation recommendation (e.g., mindfulness, relaxation).
  - Example: `/meditate focus`
  
- **`/daily`**: Receive a daily yoga or wellness tip to start your day right.
  
- **`/help`**: List all available commands and learn how to use YogaGPT.