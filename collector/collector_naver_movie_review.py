import requests
from bs4 import BeautifulSoup
import re
import math
from db.database import create_review

#################
# 1. 영화 제목 수집
#################
# movie_code : 네이버 영화 코드 (6자리 숫자)

# 제목 수집
#movie_title_crawler → 영화 제목만 모아주는 함수이름, movie_code에 영화코드를 전달하는 것
# 함수 생성,  함수는 생성하면 아무 동작 X
# 반드시 생성 후 호출을 통해서 사용해야 함!

def movie_title_crawler(movie_code):
    url = f'https://movie.naver.com/movie/bi/mi/point.naver?code={movie_code}'
    result = requests.get(url)
    doc = BeautifulSoup(result.text, 'html.parser')
    title = doc.select('h3.h_movie > a')[0].get_text()        #h3태그의 이름이 h_movie의 자신인 a태그를 가져와라
    return title        # return : 함수의 값을 누군가에게 전달할 때


    # pass → 함수에 아무것도 안써도 오류 안뜨게 하는 것(빈 깡통으로 만드는 것)


# 리뷰 수집 (리뷰, 평점, 작성자, 작성일자) + 영화 제목
def movie_review_crawler(movie_code):
    title = movie_title_crawler(movie_code) # : 제목 수집
    print(f'\n>> Start collecting movie for {title} <<')

    # 리뷰를 수집하는 코드 작성!
    # naver.point 의 url은 다른 페이지의 정보를 끌어온 것이나 똑같아서
    # 개발자 모드에서 2page, 3page 부분으로 커서를 옮기고 해당 url로 접근해야 함
    # set {제목, 리뷰, 평점, 작성자, 작성일자}
    # 리뷰만 모아져있는 url임

    url = f'https://movie.naver.com/movie/bi/mi/pointWriteFormList.naver?code={movie_code}&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false&page=1'

    result = requests.get(url)
    doc = BeautifulSoup(result.text, 'html.parser')
    all_count = doc.select('strong.total > em')[0].get_text()       #리뷰 전체 수
    # 2480건 / 10
    # all_count의 type = str => "2480"
    # print(int(all_count)) → Erorr가 남! "2480" → 2480 (가능!) "2,480" → 2480 (','인 문자가 포함되어 있어서 불가능)
    # 1.숫자만 추출 : 정규식 (정규식은 찾아서 많이 사용함!)
    numbers = re.sub(r'[^0-9]', '', all_count)
    pages = math.ceil(int(numbers) / 10)            # 반올림 해줌!
    print(f'The total nuber of pages to collect is {pages}\n')

    # 해당 페이지 리뷰 수집!
                 # 전체 리뷰 수를 count

    for page in range(1, (pages+1)):              # 시작 페이지와 끝페이지(pages)를 알려줌
        url = f'https://movie.naver.com/movie/bi/mi/pointWriteFormList.naver?code={movie_code}&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false&page={page}'
        result = requests.get(url)
        print(result)
        doc = BeautifulSoup(result.text, 'html.parser')
        review_list = doc.select('div.score_result > ul > li')    # 한 페이지의 리뷰 10건을 가져올 예정
        print(review_list)

        for i, one in enumerate(review_list):                         # 리뷰 한 건씩 수집
            # 리뷰, 평점, 작성자, 작성일자'
            review = one.select('div.score_reple > p > span')[-1].get_text().strip()    # strip() : 여백 지워주는 함수
            score = one.select('div.star_score > em')[0].get_text()


            # 날짜 시간 → 시간 없이 날짜만 추출
            # 예 : 2022.10.19 19:43 → 2022.10.19 (모든 작성일자 데이터의 규격이 똑같음!)
            # 이때 한자리수 개월이나 날짜도 01, 03 등으로 표기 되는지 확인!
            # - 날짜는 항상 16글자로 구성
            original_date = one.select('div.score_reple dt > em')[1].get_text()
            # 문자열 추출
            # [시작:끝], 끝은 포함X
            # [:15] 0~14
            # [3:] 3~끝까지
            date = original_date[:10]   #문자열 추출



            # 아이디의 익명 표시 (***) 제거!, 닉네임이 없는 경우는 그냥 *** 표시가 되어있음
            original_writer = one.select('div.score_reple dt > em')[0].get_text().strip()
            idx_end = original_writer.find('(')     # ( 의 인덱스 번호, 가변적인 인덱스로 추출할때 find() 함수를 사용
            writer = original_writer[:idx_end]      # 괄호'()'가 시작 되기 전까지 추출





            all_count =+ 1  #?? 오류남! 깃허브에서 코드 확인

            print(f'\n################## {i+1}번째 리뷰 ####################################################################')
            print(f'# Review : {review}')
            print(f'# Score : {score}')
            print(f'# Date : {date}')
            print(f'# Writer : {writer}\n')

            # Review data 생성
            # → 규격 (format) → JSON
            # JSON → 데이터 주고받을 때 많이 사용하는 타입
            # MongDB → BSON(Binary JSON) = JSON
            # Python의 Dictionary 타입 = JSON
            #
            # ※ Python Dictionary = JSON = BSON
            # JSON 포맷
            # {Key : value, Key : value, Key : value, ...}

            # dic type은 데이터 꺼낼때 key 값을 이용
            # list type은 데이터 꺼낼때 index 값을 이용
            # 이외 튜플, set 과 같은 자료형 존재
            data = {
                'title': title,
                'score': score,
                'review': review,
                'writer': writer,
                'date': date
            }

            create_review(data)

