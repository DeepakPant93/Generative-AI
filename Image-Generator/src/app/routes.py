# Copyright (c) 2024 AwesomeHelpersInc. All rights reserved.
# This file is part of the Image-Generator project.


from flask import Blueprint, render_template, request, jsonify

from .utils import generate_images

main_bp = Blueprint('main', __name__)


@main_bp.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        prompt = request.form["prompt"]
        success, data = generate_images(prompt)
        return jsonify(data)
    return render_template("index.html")
