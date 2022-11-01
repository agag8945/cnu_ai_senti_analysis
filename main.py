from collector.collector_naver_movie_review import movie_review_crawler

# 메인으로 동작하는 파일
# 실질적으로 프로그램이 실행되는 곳
# 필요한 기능들을 호출해서 사용!

# 제목 동작하는 것을 review 쪽으로 이동
# main → collector.collector_naver_movie_review → collector.collector_naver_movie_title 호출이 되고 함수를 실행
# 이때 실행만 하지않고 return도 실행됨 → return으로 '값'을 전달 [title = return 으로 바뀜]
# → collector.collector_naver_movie_review → title 실행
movie_code = '190694'       # 네이버 영화 코드

movie_review_crawler(movie_code)