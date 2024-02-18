import os
import google.generativeai as genai

from dotenv import load_dotenv

class extenstions :
    load_dotenv()
    

    def askAI(question, image):
        genai.configure(api_key=os.environ.get('GEMINI_API_KEY'))
        model = genai.GenerativeModel('gemini-pro-vision')
        try:
            response = model.generate_content([f"{question}", image]).text
        except Exception as e:
            print(e) 
            return "Error On generation" , 400
        return response, 200