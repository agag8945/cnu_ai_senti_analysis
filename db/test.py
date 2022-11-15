# mongodb 연결, 데이터 1건 저장 테스트
from pymongo import MongoClient
from database import create_review

create_review()


# 연결(Connection) 정보
# - DB_HOST : mongodb 접속 할 → IP + PORT
# - DB_ID : mongodb 계정
# - DB_PW : mongodb 암호

# Python ----------------연결---------------- MongoDB
# (1) 연결 (IP[mongodb가 설치된 컴퓨터를 찾음] + PORT[그 컴퓨터 안에서 mongdb를 찾음])
# (2) ID & PW
# 위의 두 작업이 끝나면 연결 완료!

# 127.0.0.1 = localhost 무조건 내 컴퓨터 ip (노출 걱정X)
# port번호 기본적으로 프로그램 고유 포트번호 (회사에서는 해킹 걱정으로 고유 포트번호 사용하지 않음)
# ssh : 22, http : 80, mariadb : 3386, mongodb : 27017

#client = MongoClient('127.0.0.1', 27017)

# DBMS : 데이터베이스 관리 시스템 → MongoDB
# DB(데이터 베이스) : 데이터 저장소 → 다수의 DB(Shop, Blog,...)
# DB : Shop
# - Collection(table) : 회원 정보
# - Collection(table) : 상품 정보
# - Collection(table) : 주문 정보
# - Collection(table) : 게시글 정보

# DB : movie
# ㄴ Collection : review
#db = client['movie'] #mongodb에 공간(db)를 만듬, collection:movie
#collection = db.get_collection('review')

#data = {"msg" : "몽고디비 데이터 테스트"}     # 데이터 1건 생성
#collection.insert_one(data)               # 1건의 데이터를 저장!