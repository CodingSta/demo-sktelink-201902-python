import re

from telegram.ext import Updater, Filters
from telegram.ext import CommandHandler, ConversationHandler, MessageHandler

import requests
from bs4 import BeautifulSoup


def 글자수_세기(문자열):
    return len(문자열)


def 단어수_세기(문자열):
    return len(문자열.split())


def 네이버_실검():
    res = requests.get("http://naver.com")
    html = res.text
    soup = BeautifulSoup(html, 'html.parser')
    tag_list = soup.select('.PM_CL_realtimeKeyword_rolling .ah_k')

    keyword_list = []

    for tag in tag_list:
        label = tag.text
        keyword_list.append(label)

    return keyword_list



def start(bot, update):
    chat_id = update.message.chat_id
    text = update.message.text
    bot.send_message(chat_id=chat_id, text="I'm a bot, please talk to me!")


def echo(bot, update):
    chat_id = update.message.chat_id
    text = update.message.text

    try:
        if text == '야':
            response = '왜?'
        elif text.startswith('글자수세어줘:'):
            문자열 = text[7:]
            글자수 = 글자수_세기(문자열)
            response = '글자수는 {}글자입니다.'.format(글자수)
        elif text.startswith('단어수세어줘:'):
            문자열 = text[7:]
            단어수 = 단어수_세기(문자열)
            response = '단어수는 {}글자입니다.'.format(단어수)
        elif text == '네이버실검':
            keyword_list = 네이버_실검()
            response = "\n".join(keyword_list)
            response = '네이버 실시간 검색어\n\n' + response
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
