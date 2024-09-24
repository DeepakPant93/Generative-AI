# Copyright (c) 2024 AwesomeHelpersInc. All rights reserved.
# This file is part of the Image-Generator project.


import random

from flask import current_app

fallback_images = [
    "https://via.placeholder.com/1024x1024.png?text=Something+went+wrong",
    "https://via.placeholder.com/1024x1024.png?text=Something+went+wrong",
    "https://via.placeholder.com/1024x1024.png?text=Something+went+wrong"
]


def generate_images(prompt):
    try:
        print(prompt)
        response = current_app.openai_client.images.generate(
            model="dall-e-3",
            prompt=prompt,
            n=1,
            size="1024x1024"
        )
        image_urls = [img.url for img in response.data]
        return True, {"success": True, "images": image_urls}
    except Exception as e:
        print(e)
        return False, {
            "success": True,
            "images": get_fallback_images(),
            "message": "An error occurred. Showing placeholder images."
        }


def get_fallback_images(count=3):
    return random.sample(fallback_images, count)
