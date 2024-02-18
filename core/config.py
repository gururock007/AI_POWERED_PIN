import os
from dotenv import load_dotenv

load_dotenv()
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    GEMINAI_API_KEY = os.environ.get('GEMINAI_API_KEY')
    VOICE_API_KEY = os.environ.get('VOICE_API_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False