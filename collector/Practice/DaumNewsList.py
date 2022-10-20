import requests
from bs4 import BeautifulSoup
from collector.Practice.CollectorService import get_daum_news
# <a (앵커 태그)

# = : 대입 연산자
url = 'https://news.daum.net/breakingnews/digital'

# SSL Error → requests.get(url, verify = False)

result = requests.get(url)      # result : 소스코드가 있음

doc = BeautifulSoup(result.text, 'html.parser')     # html.parser : html 형식으로 읽어내라

# <a href = "url> : a 태그는 클릭했을 때 해당 url로 이동
# len() : list[]의 갯수를 알려주는 함수

title_list = doc.select('ul.list_news2 a.link_txt')

# pprint.pprint(title_list)       # pretty print 약자
# print(len(title_list))

# enumerate() : 반복하면서 index 번호와 item을 가져옴
# list[]의 index의 0번부터 시작
# len(list) = 15, index = 0~14
for i, title in enumerate(title_list):
    print(f'인덱스 : {i}, url : {title["href"]}')      # ["href"] : title 속의 href 속성 값을 가져옴
                                                    # title.get_text : 제목만 가져옴
    get_daum_news(title["href"])

