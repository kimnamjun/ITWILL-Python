import flask
from flask import Flask  # class
print(flask.__version__)  # 1.1.2

# flask application
app = Flask(__name__)  # 생성자 -> object(app)

# 함수 장식자 : 사용자 요청 URL
@app.route('/')  # http://127.0.0.1:5000/
def hello():
    return 'hello flask~~~'


# 프로그램 시작점
if __name__ == "__main__":
    app.run()  # application 실행
