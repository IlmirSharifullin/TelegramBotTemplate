import os
from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from logger import setup_logger

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
DB_URL = os.getenv('DB_URL')

engine = create_async_engine(url=DB_URL, echo=False)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)

logger = setup_logger()
