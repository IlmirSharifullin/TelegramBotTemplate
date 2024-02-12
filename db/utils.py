import traceback
from functools import wraps
from typing import Callable

from config import async_session_maker


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
