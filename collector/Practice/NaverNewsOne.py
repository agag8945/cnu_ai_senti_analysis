# 네이버 뉴스 주제와 본문 수집

import requests
from bs4 import BeautifulSoup

url = 'https://n.news.naver.com/article/005/0001559027?ntype=RANKING'

headers = {'User-Agent' : 'Mozilla/5.0 (Window NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, liek  Gecko) Chrome/92.0.4515.131 Safari/537.36'}
# requests(headers+body)랑 같이 보내야 함
# 파이썬의 라이브러리인 requests는 body 파일만 보내서 로봇인 게 티남 따라서 headers파일을 붙여서 requests를 보냄

result = requests.get(url, headers = headers)

doc = BeautifulSoup(result.text, 'html.parser')

# 파이썬은 '', "" 구분하지 않음 (but! java, c언어는 구분함)
title = doc.select('h2.media_end_head_headline')[0].get_text()

# get_text() : 태그를 제거, text만 추출
# strip() : 앞 뒤 공백을 제거 -> 가운데 여백은 사라지지 않음
# -회원가입 사이트 : .strip() 을 사용, 서비스 질을 높이기

contents = doc.select('div#dic_area')[0].get_text().strip()

print(f'뉴스 제목 : {title}')                   # fstring 표현법 -> 직관적
print('뉴스 본문 : {}' .format(contents))       # format - 요즘은 대부분 fstring 사용, format -> 옛날 방식


