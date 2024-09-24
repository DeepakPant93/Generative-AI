# Copyright (c) 2024 AwesomeHelpersInc. All rights reserved.
# This file is part of the Image-Generator project.

import os

from dotenv import load_dotenv
from flask import Flask
from openai import OpenAI

from src.app.routes import main_bp

load_dotenv()


def create_app():
    app = Flask(__name__, template_folder="templates")
    app.config['OPENAI_API_KEY'] = os.getenv("OPENAI_API_KEY")
    app.openai_client = OpenAI(api_key=app.config['OPENAI_API_KEY'])

    app.register_blueprint(main_bp)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host='0.0.0.0', port=8080, debug=True)
