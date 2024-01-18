import asyncio
import logging

from config import BOT_TOKEN
from aiogram import Bot, Dispatcher

from handlers import router as handler_router


dp = Dispatcher()


async def main() -> None:
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=BOT_TOKEN)
    dp.include_router(handler_router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
