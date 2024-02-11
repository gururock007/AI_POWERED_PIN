from flask import Flask, jsonify, request
from dotenv import load_dotenv
from PIL import Image
from io import BytesIO

import base64
import google.generativeai as genai
import os

load_dotenv()

app = Flask(__name__)

def askAI(question, image):
    try:
        response = model.generate_content([f"{question}", image]).text
    except Exception as e:
        print(e)
        print("Error On generation")
        return "Error On generation" , 400 
    return response 

genai.configure(api_key=os.environ.get('GEMINI_API_KEY'))
model = genai.GenerativeModel('gemini-pro-vision')

@app.route("/", methods = ['POST'])
def home():
    data = request.get_json()
    question = data.get('text')
    image_data = data.get('image')
    if image_data:
        try:
            image_bytes = base64.b64decode(image_data)
            image = Image.open(BytesIO(image_bytes))
            image.save("download.jpg")
            response = askAI(question, image)
            return jsonify({"answer": response}), 200
        except Exception as e:
            print(f"Error saving image: {e}")
            return jsonify({"error": "Failed to save image"}), 400
        
    return response

if __name__ == '__main__':
    app.run(debug=True)