# todocal 설정 과정

python 3 설치

- brew install python

virtual 환경 설정

- python3 -m venv myvenv
- 그냥 python으로 하면 venv module이 없다고 함.

venv 실행

- source myvenv/bin/activate

(venv에서) 장고 설치 (최신이 설치됨. 2016/8/9 기준 1.10)

- pip install django

git init 후 remote add origin git@github.com:ErickRyu/todocal.git

- 즉 startproject는 할 필요 없음.

마이그레이션

- python manage.py migrate

서버 시작해봄으로써 테스트

- python manage.py runserver
