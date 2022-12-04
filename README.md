Fast API & Flask
-
Python의 WAS 프레임워크인 Fast API와 Flask를 간단하게 연습해 본 코드입니다.

#### 개발 환경
- Python 3.7

#### Business Flow
- Flask (Front Application) → Fast API (API) → Database

#### Setting

```shell
pip3 install Flask
pip3 install fastapi
pip3 install "uvicorn[standard]"

pip3 install sqlalchemy
pip3 install requests

pip3 install mysql #MySQL 사용시
pip3 install psycopg2-binary #PostgreSQL 사용시
```

`/fast_api/database.py` 의 5번째 line에 사용할 DB의 주소를 넣을 것
`/fast_api/models.py` 의 내용을 참고하여 `product` 라는 이름의 테이블을 만들 것

#### 실행

1. `fast_api` 경로에서 `uvicorn app:app --reload` 명령어로 API 실행
2. `flask` 경로에서 `python3 app` 명령어로 Front Application 실행
3. `http://127.0.0.1:5000` 주소로 접속
4. API 문서는 `http://127.0.0.1:8000/docs` 로 접속