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


def 네이버_블로그_검색(검색어):
    url = "https://search.naver.com/search.naver"
    params = {
        'where': 'post',
        'sm': 'tab_jum',
        'query': 검색어,
    }

    res = requests.get(url, params=params)
    html = res.text
    soup = BeautifulSoup(html, 'html.parser')
    tag_list = soup.select('.sh_blog_title')

    post_list = []
    for tag in tag_list:
        post_url = tag['href']
        post_title = tag['title']
        post_list.append({
            'title': post_title,
            'url': post_url,
        })

    return post_list
