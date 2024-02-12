from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router(name='start-command')


@router.message(Command('start'))
async def start_cmd(message: Message):
    pass
