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

def get_mp3(url, text):
    load_dotenv()
    params = {'key': os.environ.get('VOICE_API_KEY'), 'src' : text,'hl' : 'en-us', 'c' : 'MP3', 'b64':'true'}
    try:
        response = requests.get(url=url, params=params)
        print(os.environ.get('VOICE_API_KEY'))

        if response.content:
           with open("output.mp3", "wb") as f:
                f.write(base64.b64decode(response.content))
                print("MP3 saved successfully")
        else:
            print("Error: Unexpected response format")
    except requests.exceptions.RequestException as e:
        print(f"Error getting MP3: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

ai_url = 'http://127.0.0.1:5000/'
image_url = 'https://picsum.photos/500'
voice_url = 'https://api.voicerss.org/'

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
                print("Server response:", data)
                get_mp3(voice_url, response.text)
            except json.JSONDecodeError:
                print("Error decoding server response")
        else:
            print(f"Server error: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error sending request: {e}")
else:
    print("Error downloading image")
