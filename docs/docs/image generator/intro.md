# Image Generator App

This is a simple Flask-based web application that uses OpenAI's DALL·E model to generate images from text prompts. The app generates three images for each prompt provided by the user.

## Features

- **Generative AI**: Uses OpenAI's DALL·E model to create images based on user input.
- **Flask Application**: The web server is built using Flask and runs on port `8080`.
- **Multiple Results**: For every prompt, the app returns three unique image results.

## Getting Started

### Prerequisites

Before you start, make sure you have the following installed on your system:
- Python 3.8 or higher
- OpenAI API key

### Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/your-username/Generative-AI.git
    cd Image-Generator
    ```

2. **Install the dependencies**:

    Create a virtual environment (optional but recommended):

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

    Install the required dependencies using `pip`:

    ```bash
    pip install -r requirements.txt
    ```

3. **Set up environment variables**:

    Create a `.env` file in the root of your project and add your OpenAI API key:

    ```
    OPENAI_API_KEY=your_openai_api_key
    ```

4. **Start the Flask application**:

    To run the app, use the following command:

    ```bash
    python3 main.py
    ```

    The app will start and run on port `8080` by default.

5. **Access the app**:

    Open your browser and go to:

    ```
    http://localhost:8080
    ```

6. **Run the bot using Docker**:

   Start the bot using Docker.

    ```bash
    docker run -d \
     --name image-generator \
     -e NAME=image-generator \
     -e OPENAI_API_KEY=your_openai_api_key \
     deepak93p/image-generator:latest
      ```
For setup instructions, see [Setup Guide](SETUP.md).


## How to Use

1. After navigating to the app in your browser, you will see a text box where you can enter a prompt.
2. Enter a descriptive prompt (e.g., "a futuristic city in the clouds at sunset").
3. The app will generate three images based on the prompt using OpenAI's DALL·E model.
4. View or download the generated images from the results page.

## File Structure

```
Image-Generator/
.
├── Dockerfile                   # Dockerfile for building the image
├── Makefile                     # Commands related to the application
├── README.md                    # Application description
├── SETUP.md                     # Instructions for setting up the app
├── __init__.py               
├── __main.py__.py   
├── docker-compose.yml           # Docker Compose file
├── main.py                      # Flask application entry point
├── requirements.txt             # Dependencies
├── setup.py                     # Setup script
├── src                          # Source code
│         ├── __init__.py
│         └── app                # Application code
│             ├── __init__.py
│             ├── routes.py      # Routes for the application
│             └── utils.py       # Utility functions
└── templates                    # HTML templates
    └── index.html               # Index HTML template   

```

## API Details

- **Endpoint**: `/generate`
- **Method**: POST
- **Input**: A prompt provided by the user in the form of text.
- **Output**: Three generated images returned to the user.

## Example

If you enter the prompt `"a peaceful forest with a waterfall"`, the app will return three AI-generated images depicting various interpretations of the scene.

## Troubleshooting

- Make sure your OpenAI API key is valid and has sufficient quota to generate images.
- If the app doesn't start, check that Flask and required dependencies are installed properly.
- If the app doesn't generate images, check that the OpenAI API key is valid and has sufficient quota.

### Enjoy creating AI-generated art with the Image Generator App!