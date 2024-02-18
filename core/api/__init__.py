from flask import jsonify, request, Blueprint
from PIL import Image
from io import BytesIO

from .image_to_text import *
from .text_to_speech import *

import base64
bp = Blueprint('main',__name__,url_prefix='/')


@bp.route("/", methods = ['GET','POST'])
def home():
    data = request.get_json()
    question = data.get('text')
    image_data = data.get('image')
    if image_data:
        try:
            image_bytes = base64.b64decode(image_data)
            image = Image.open(BytesIO(image_bytes))
            image.save("download.jpg")
            text = askAI(question, image)
            responce = get_mp3(text=text)
            return jsonify(f"Result: {responce[0]}"),responce[1]
        except Exception as e:
            print(f"Error saving image: {e}")
            return jsonify({"error": "Failed to save image"}), 400
    return jsonify({"Error: image Not Found"}), 404