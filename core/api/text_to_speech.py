import requests
import base64

from config import Config

def api_config(text):
    url = 'https://api.voicerss.org/'
    params = {'key': Config.VOICE_API_KEY, 'src' : text,'hl' : 'en-us', 'c' : 'MP3', 'b64':'true'}
    return (url, params)

def get_mp3(text):
    url, params = api_config(text)
    try:
        response = requests.get(url=url, params=params)
        if response.content:
           with open("output.mp3", "wb") as f:
                f.write(base64.b64decode(response.content))
                print("MP3 saved successfully")
                return ("MP3 saved successfully", 200)
        else:
            print("Error: Unexpected response format")
            return ("Unexpected response format", 422)
    except requests.exceptions.RequestException as e:
        print(f"Error getting MP3: {e}")
        return ("Error getting MP3", 503)
    except Exception as e:
        print(f"Unexpected error: {e}")
        return ("Unexpected error", 500)
