import asyncio
import logging

from aiogram import Bot
from aiogram import Dispatcher
from aiogram import types
from aiogram.client.default import DefaultBotProperties
from aiogram.filters import Command, CommandStart
from aiogram.utils import markdown
from aiogram.enums import ParseMode

from config import settings


BOT_TOKEN = settings.bot_token
dp = Dispatcher()

@dp.message(CommandStart())
async def handle_start(message: types.Message):
    pic_url = 'https://www.istockphoto.com/photo/cute-blue-robot-waving-hand-3d-gm1346150003-423999492?searchscope=image%2Cfilm'
    await message.answer(
        text=f'{markdown.hide_link(pic_url)}Hello, {markdown.hbold(message.from_user.full_name)}!',
        parse_mode=ParseMode.HTML,
    )

@dp.message(Command("help"))
async def handle_help(message: types.Message):
    # text = "I'm your bot.\nSend me any message"
    # entity_bold = types.MessageEntity(
    #     type='bold',
    #     offset=len("I'm your bot.\nSend me "),
    #     length=3,
    # )
    # entities = [entity_bold]
    # await message.answer(text=text, entities=entities)
    text = markdown.text(
        "I'm your bot\\.",
        "Send me *any* message",
        sep="\n",
    )
    await message.answer(text=text)

@dp.message(Command("code"))
async def handle_command_code(message: types.Message):
    text = markdown.text(
        "Here's Python code:",
        "",
        markdown.markdown_decoration.pre_language(
            markdown.text(
                "print('Hello World!')",
                "\n",
                "def foo():\n    return 'bar'",
                sep="\n",
            ),
            language="python",
        ),
        "And here's some Java code:",
        markdown.markdown_decoration.pre_language(
            markdown.text(
                "public class App extends Application {",
                "    @Override",
                "    public void start(Stage stage) {",
                "        Model.getInstance().getViewFactory().showLoginWindow();",
                "    }",
                "}",
                sep="\n"
            ),
            language="java",
        ),
        sep="\n",
    )

    await message.answer(text=text)


@dp.message()
async def echo_message(message: types.Message):

    await message.answer(
        text="Wait a second...",
        parse_mode=None
    )
    # if message.text:
    #     await message.answer(
    #         text=message.text,
    #         entities=message.entities
    #     )

    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.reply("something new)))")

async def main():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(
        token=BOT_TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.MARKDOWN_V2),
        # parse_mode=ParseMode.MARKDOWN_V2,
    )
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
