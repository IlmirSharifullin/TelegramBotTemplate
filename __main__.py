import asyncio
import logging
from aiogram import Dispatcher, Bot

from bot.handlers import start_command, errors
from utils.config import BOT_TOKEN


async def main():
    logging.basicConfig(
        filename='logs.log',
        format='%(asctime)s - %(levelname)s - %(funcName)s - %(message)s  ',
        datefmt='%d-%b-%y %H:%M:%S',
        level=logging.INFO
    )

    dp = Dispatcher()

    dp.include_routers(start_command.router, errors.router)

    await dp.start_polling(bot)


if __name__ == '__main__':
    bot = Bot(BOT_TOKEN)
    asyncio.run(main())
