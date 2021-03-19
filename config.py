from dotenv import load_dotenv, find_dotenv
from pathlib import Path
import os

load_dotenv(find_dotenv())

SECRET_KEY = os.getenv('SECRET_KEY')
YT_DEVELOPER_KEY = os.getenv('YT_DEVELOPER_KEY')
FIREBASE_URL = os.getenv('FIREBASE_URL')
