import traceback

from aiogram import Router
from aiogram.types import ErrorEvent

from utils.config import logger

router = Router(name='errors-handler')


@router.error()
async def errors_handler(event: ErrorEvent):
    logger.error(traceback.format_exc())
