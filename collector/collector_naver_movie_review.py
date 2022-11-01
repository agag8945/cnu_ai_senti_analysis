import requests
from bs4 import BeautifulSoup

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
    print(f'제목 : {title}')

    # set {제목, 리뷰, 평점, 작성자, 작성일자}
