import logging

from aiogram import Bot, Dispatcher, executor, types

from Code.Utilities.config.config_util import ConfigUtil

API_TOKEN = ConfigUtil.get_config('telegram')['stockmarket0796_bot']

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    bot_message = "Hi, I'm StockBot!\nBelow are the services available for you!"
    await message.reply(bot_message)


@dp.message_handler()
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)
    if message.text.split()[0].split()[0] != '/':
        print(message.text.split()[0].split()[0])
        await message.answer(f"{message.text} is not a valid command")
    else:
        await message.answer(f"I'm sorry i did not understand the command {message.text}")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)