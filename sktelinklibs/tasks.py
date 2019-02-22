import re
from .utils import 네이버_블로그_검색


class Task_네이버_블로그_검색:
    def __init__(self, text):
        self.text = text
        self.matched = None

    def is_valid(self):
        self.matched = re.match('네이버에서(.+)검색', self.text)
        return bool(self.matched)

    def proc(self):
        검색어 = self.matched.groups()[0]
        post_list = 네이버_블로그_검색(검색어)
        line_list = []
        for post in post_list:
            line = '{}\n{}'.format(post['title'], post['url'])
            line_list.append(line)
        response = '\n\n'.join(line_list)
        return response


class TaskYa:
    def __init__(self, text):
        self.text = text

    def is_valid(self):
        return self.text == '야'

    def proc(self):
        return '왜?'





        # elif text == '야':
        #     response = '왜?'
        # elif text.startswith('글자수세어줘:'):
        #     문자열 = text[7:]
        #     글자수 = 글자수_세기(문자열)
        #     response = '글자수는 {}글자입니다.'.format(글자수)
        # elif text.startswith('단어수세어줘:'):
        #     문자열 = text[7:]
        #     단어수 = 단어수_세기(문자열)
        #     response = '단어수는 {}글자입니다.'.format(단어수)
        # elif text == '네이버실검':
        #     keyword_list = 네이버_실검()
        #     line_list = []
        #     rank = 1
        #     for keyword in keyword_list:
        #         line = '{}. {}'.format(rank, keyword)
        #         line_list.append(line)
        #         rank += 1
        #     response = "\n".join(line_list)
        #     response = '네이버 실시간 검색어\n\n' + response
        # elif text.startswith('네이버검색:'):
        #     검색어 = text[6:]
        #     post_list = 네이버_블로그_검색(검색어)
        #     line_list = []
        #     for post in post_list:
        #         line = '{}\n{}'.format(post['title'], post['url'])
        #         line_list.append(line)
        #     response = '\n\n'.join(line_list)
        # else:
        #     response = '니가 무슨 말 하는 지 모르겠어. :('