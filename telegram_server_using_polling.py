import re

from telegram.ext import Updater, Filters
from telegram.ext import CommandHandler, ConversationHandler, MessageHandler

import requests
from bs4 import BeautifulSoup


def start(bot, update):
    chat_id = update.message.chat_id
    text = update.message.text
    bot.send_message(chat_id=chat_id, text="I'm a bot, please talk to me!")


def echo(bot, update):
    chat_id = update.message.chat_id
    text = update.message.text

    if text == '야':
        response = '왜?'
    elif text == '네이버실검':
        res = requests.get("http://naver.com")
        html = res.text
        soup = BeautifulSoup(html, 'html.parser')
        tag_list = soup.select('.PM_CL_realtimeKeyword_rolling .ah_k')

        message_list = []

        for tag in tag_list:
            label = tag.text
            message_list.append(label)

        response = "\n".join(message_list)
    else:
        response = '니가 무슨 말 하는 지 모르겠어. :('

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
    TOKEN = "*********************************************"
    main(TOKEN)

