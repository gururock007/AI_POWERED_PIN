from PIL import Image
from io import BytesIO
from dotenv import load_dotenv
import json
import requests
import base64
import os


def get_image(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for non-200 status codes
        with BytesIO() as buffer:
            Image.open(BytesIO(response.content)).save(buffer, format="JPEG")
            return base64.b64encode(buffer.getvalue()).decode()
    except requests.exceptions.RequestException as e:
        print(f"Error getting image: {e}")
        return None

ai_url = 'http://127.0.0.1:5000/'
image_url = 'https://picsum.photos/500'

text = "I'm Blind, Be My guide and eye, This image is taken by me Now what's In front of me? Be detail I dont Wannt to Know past or the history"
image_data = get_image(image_url)

if image_data:
    data = {'text': text, 'image': image_data}
    json_data = json.dumps(data)
    headers = {'Content-type': 'application/json'}
    try:
        response = requests.post(url=ai_url, data=json_data, headers=headers)
        if response.status_code == 200:
            try:
                data = json.loads(response.text)
                print("Server response:", data['Result'])
            except json.JSONDecodeError:
                print("Error decoding server response")
        else:
            print(f"Server error: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error sending request: {e}")
else:
    print("Error downloading image")
