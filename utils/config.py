import os
from dotenv import load_dotenv

from logger import setup_logger

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
DB_URL = os.getenv('DB_URL')

logger = setup_logger()
