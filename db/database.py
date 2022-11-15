from pymongo import MongoClient

# 회원
# - 회원가입 (Create)
# - 회원목록 (Raed)
# - 회원수정 (Update)
# - 회원삭제 (Delete)

# 상품
# - 상품등록 (Create)
# - 상품목록 (Raed)
# - 상품수정 (Update)
# - 상품삭제 (Delete)

# 게시글
# - 게시글등록 (Create)
# - 게시글목록 (Raed)
# - 게시글수정 (Update)
# - 게시글삭제 (Delete)

# → CRUD 작업 (Create, Read, Update, Delete) DAO(Data Access Object)를 만듦
# 게시글 → BoardDAO.py : 게시글의 CRUD 작업이 담긴 파일
# 회원 → MemberDAO.py : 회원의 CRUD 작업이 담긴 파일




# 진짜 코드!


# 1. Connection 작업 (공통: Common)
def db_conn():
    client = MongoClient('127.0.0.1', 27017)    # MongoDB 찾아감
    db = client['movie']                        # Database 선택
    collection = db.get_collection('review')    # Collection 선택
    return collection


# 2. Review 저장 (Create)
def create_review(data):
    collection = db_conn()                      # MongDB Connection
    collection.insert_one(data)


# 3. Review 조회 (Read) 보통 get으로 표시..
def read_review():
    collection = db_conn()                      # MongDB Connection

# 깃허브에 올릴때는 밑에 공백은 한줄만 남기는 것이 규칙...