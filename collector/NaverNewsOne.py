import requests
from bs4 import BeautifulSoup

url = 'https://n.news.naver.com/mnews/ranking/article/001/0013494648?ntype=RANKING'

headers = {'User-Agent' : 'Mozilla/5.0 (Window NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, liek  Gecko) Chrome/92.0.4515.131 Safari/537.36'}
# requests(headers+body)랑 같이 보내야 함
# 파이썬의 라이브러리인 requests는 body 파일만 보내서 로봇인 게 티남 따라서 headers파일을 붙여서 requests를 보냄

result = requests.get(url, headers = headers)

doc = BeautifulSoup(result.text, 'html.parser')

# 파이썬은 '', "" 구분하지 않음 (java, c언어는 구분함)
title = doc.select('h2.media_end_head_headline')[0].get_text()

print(f'뉴스제목 : {title}')


