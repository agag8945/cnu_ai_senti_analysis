# 주석 -> 개발자의 메모장, 파이썬이 주석은 실행X
#파이썬의 경로
#1. 프로젝트(cun_ai_senti_analiysis-main)
#2. python package(collector)
#3. Python file(test.py, DaumNewsOne.py)
# -python package 는 python file들을 모아두는 폴더
#                 -> 폴더아이콘안에 구멍 뚫려있음

# import와 Library(module)
# -python 코드를 직접 작성해서 개발할 수도 있지만 -다른 개발자가 이미 만들어 놓은 코드를 사용하면 편리함
# -> 이미 개발되어 있는 코드들의 묶음 = Library (module)
# 1. built in library: Python 설치하면 자동으로 제공 (예: math, sys, os 등)
# 2. 외부 Library: 여러분이 직접 추가해서 사용(예: requests, beautifulsoup)

# Library를 사용하기 위해서는 import 작업 진행 -> import는 도서관에서 필요한 책을 빌려오는 개념

# Library를 사용 중이지 않으면 회색으로 비활성화 상태를 표시함

import requests                     # 책 전체를 빌려온 것
from bs4 import BeautifulSoup       # bs4라는 책에서 BeautifulSoup라는 1개의 파트만 빌려온 것

# 목표: Daum 뉴스 웹페이지의 제목과 본문 데이터를 수집
# 1. url: https://v.daum.net/v/20221006105536962
url = 'https://v.daum.net/v/20221006105536962'
# 2. requests로 해당 url의 html 전체 코드를 수집!
result = requests.get(url)
# print(result.text) #<Response [200]> -> 200 : 성공했다는 뜻


# 3. beautifulsoup을 통해서 '제목'과 '본문'만을 추출
doc = BeautifulSoup(result.text, 'html.parser')
# python은 []: List Type
# index   0  1  2  3   4
#       -[5, 6, 9, 10, 15] : List 내에는 다양한 데이터 저장 가능
# [5] : ,가 없으면 데이터가 하나의 값으로 묶어 있는 것
title = doc.select('h3.tit_view')[0].get_text() #[0] : 대괄호[]가 없어짐, get_text() : txt값만 가져옴


print(f'뉴스제목 : {title}') #예쁘게 출력!

