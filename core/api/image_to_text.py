import os
import google.generativeai as genai

from dotenv import load_dotenv
from config import Config


def model_config():
    load_dotenv()
    genai.configure(api_key=Config.GEMINAI_API_KEY)
    model = genai.GenerativeModel('gemini-pro-vision')
    return model

def askAI(question, image):
    try:
        model = model_config()
        response = model.generate_content([f"{question}", image]).text
    except Exception as e:
        print(e) 
        return "Error On generation" , 400
    
    return response, 200


