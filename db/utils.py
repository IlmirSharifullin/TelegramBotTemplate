import traceback
from functools import wraps
from typing import Callable

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from utils.config import DB_URL

engine = create_async_engine(url=DB_URL, echo=False)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)


def with_session(func: Callable) -> Callable:
    @wraps(func)
    async def wrapper(*args, **kwargs):
        try:
            async with async_session_maker() as session:
                kwargs['session'] = session
                result = await func(*args, **kwargs)
                await session.commit()
            return result
        except Exception as ex:
            print(traceback.format_exc())

    return wrapper
