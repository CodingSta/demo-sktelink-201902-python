import re

from telegram.ext import Updater, Filters
from telegram.ext import CommandHandler, ConversationHandler, MessageHandler

import requests
from bs4 import BeautifulSoup

from sktelinklibs import tasks


def start(bot, update):
    chat_id = update.message.chat_id
    text = update.message.text
    bot.send_message(chat_id=chat_id, text="I'm a bot, please talk to me!")


def echo(bot, update):
    chat_id = update.message.chat_id
    text = update.message.text

    task_cls_list = [
        # tasks.TaskYa,
        tasks.Task_네이버_블로그_검색,
    ]

    try:
        for task_cls in task_cls_list:
            task = task_cls(text)
            if task.is_valid():
                response = task.proc()
                break
        else:
            response = '니가 무슨 말 하는 지 모르겠어. :('
    except Exception as e:
        response = str(e)

    bot.send_message(chat_id=chat_id, text=response)


def main(token):
    bot = Updater(token=TOKEN)

    handler = CommandHandler('start', start)
    bot.dispatcher.add_handler(handler)

    handler = MessageHandler(Filters.text, echo)
    bot.dispatcher.add_handler(handler)

    bot.start_polling()

    print('running telegram bot ...')
    bot.idle()


if __name__ == '__main__':
    # TODO: 필요한 라이브러리 설치 : pip install python-telegram-bot
    # FIXME: 각자의 Token을 적용해주세요.
    import os
    TOKEN = os.environ.get('TELEGRAM_TOKEN')
    main(TOKEN)
