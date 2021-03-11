from dotenv import load_dotenv
from pathlib import Path
import os


env_path = Path('src') / '.env'
load_dotenv(dotenv_path=env_path)


class Config:
    DEBUG = os.getenv('DEBUG')
    SECRET_KEY = os.getenv('SECRET_KEY')
    YT_DEVELOPER_KEY = os.getenv('YT_DEVELOPER_KEY')
