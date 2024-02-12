import asyncio
import logging
import traceback

from aiogram import Dispatcher, Bot
from aiogram.types import ErrorEvent

from bot.handlers import start_command
from config import logger, BOT_TOKEN


async def main():
    logging.basicConfig(
        filename='logs.log',
        format='%(asctime)s - %(levelname)s - %(funcName)s - %(message)s  ',
        datefmt='%d-%b-%y %H:%M:%S',
        level=logging.INFO
    )

    dp = Dispatcher()

    dp.include_routers(start_command.router)

    @dp.error()
    async def error_handler(event: ErrorEvent):
        logger.error(traceback.format_exc())

    await dp.start_polling(bot)


if __name__ == '__main__':
    bot = Bot(BOT_TOKEN)
    asyncio.run(main())
