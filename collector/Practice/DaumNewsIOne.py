# 주석 → 개발자의 메모장, 파이썬이 주석은 실행X
#파이썬의 경로
#1. 프로젝트(cun_ai_senti_analiysis-main)
#2. python package(collector)
#3. Python file(test.py, DaumNewsOne.py)
# -python package 는 python file들을 모아두는 폴더
#                 → 폴더아이콘안에 구멍 뚫려있음

# import와 Library(module)
# -python 코드를 직접 작성해서 개발할 수도 있지만 -다른 개발자가 이미 만들어 놓은 코드를 사용하면 편리함
# → 이미 개발되어 있는 코드들의 묶음 = Library (module)
# 1. built in library: Python 설치하면 자동으로 제공 (예: math, sys, os 등)
# 2. 외부 Library: 여러분이 직접 추가해서 사용(예: requests, beautifulsoup)

# Library를 사용하기 위해서는 import 작업 진행 → import는 도서관에서 필요한 책을 빌려오는 개념

# Library를 사용 중이지 않으면 회색으로 비활성화 상태를 표시함

import requests                     # 책 전체를 빌려온 것
from bs4 import BeautifulSoup       # bs4라는 책에서 BeautifulSoup라는 1개의 파트만 빌려온 것

# 목표: Daum 뉴스 웹페이지의 제목과 본문 데이터를 수집
# f12키로 개발자 환경 화면으로 html로 이루어진 코드를 확인 가능
# 1) requests로 해당 url의 전체 소스코드를 가지고 옴
# 2) Beautifulsoup(bs4)에게 전체소스코드 전달 → doc
# 3) bs4가 전체소스코드에서 원하는 데이터만 select


# 1. url: https://v.daum.net/v/20221006105536962
url = 'https://v.daum.net/v/20221006105536962'
# 2. requests(->전체 소스코드를 가져옴)로 해당 url의 html 전체 코드를 수집!
result = requests.get(url)
# print(result.text) #<Response [200]> → 200 : 성공했다는 뜻


# 3. beautifulsoup을 통해서 '제목'과 '본문'만을 추출
doc = BeautifulSoup(result.text, 'html.parser')
# python은 []: List Type
# index   0  1  2  3   4
#       -[5, 6, 9, 10, 15] : List 내에는 다양한 데이터 저장 가능
# [5] : ,가 없으면 데이터가 하나의 값으로 묶어 있는 것

title = doc.select('h3.tit_view')[0].get_text()     # 코드에 물결표시가 빨간 색이면 오류, 노란색/초록색: 실행을 되지만 좀 불편
                                                    # → 코딩 컨벤션을 지켜야 함(주석은 두칸 띄고, 함수는 한 칸 엔터치고)
                                                    # h3 태그 중에 이름이 tit_view를 갖는 select
                                                    # [0] : 대괄호[]가 없어짐, get_text() : txt값만 가져옴,
                                                    # .select: ~을 선택하기
# html → tag + 선택자 (h3 + tit_view)
#        -tag : 기본적으로 정의 되어 있음 (h3, p, div, span, ...)
# 뒤에 선택자가 없으면 소속 관계를 지정 해서 편하게 불러올 수 있음

print(f'뉴스제목 : {title}') #예쁘게 출력!

contents = doc.select('section p')           # section 태그를 부모로 둔 모든 자식 p 태그를 select 하라
                                                        # title과 달리 s가 붙어있음 : section 아래의 p태그가 여러개 있음

# contents = [<p1>, <p2>, <p3>, <p4>, ...] : 복수의 본문 포함
# <p1> = <p> 111111</p> :111111만 떼와야 함
# <p2> = <p> 222222</p> :222222만 떼와야 함
# <p3> = <p> 333333</p> :333333만 떼와야 함
# <p4> = <p> 444444</p> :444444만 떼와야 함
# <p5> = <p> 555555</p> :555555만 떼와야 함
# 반복적인 작업 → for 문

content = ''

for line in contents:           # 순서대로 <p>를 가져와서 line에 넣고 다음 코드 실행
    # line = <p> 111111</p>
    content += line.get_text()
    # 111111 : 텍스트 값만 뽑아옴
    # 반복 → 1111112222223333333444444555555
print(f'뉴스본문 : {content}')




