# Copyright (c) 2024 AwesomeHelpersInc. All rights reserved.
# This file is part of the YogaGPT project.

if __name__ == "__main__":
    from src.chatgpt.app import start_chat as start_chatgpt
    from src.ollama.app import start_chat as start_ollama

    ## Happy Chatting...

    ## Start ChatGPT
    start_chatgpt() ## Use this line if you want to use ChatGPT

    ## Start Ollama
    # start_ollama() ## Uncomment this line if you want to use Ollama
