from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

router = Router(name='start-command')


@router.message(CommandStart())
async def start_cmd(message: Message):
    pass
