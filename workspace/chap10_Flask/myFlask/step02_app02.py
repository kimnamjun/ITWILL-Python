'''
python 객체(list, dict) -> 템플릿으로 보내기

JinJa2 템플릿 표현식
{{object}} : 단일 객체 출력
{% for 변수 in 열거형 객체 %} : 열거형 객체 출력
'''
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("/app02/index.html")

@app.route('/temp01')
def temp01():
    username = '홍길동'
    goodsList = ['딸기', '포도', '사과']
    return render_template('/app02/temp01_page.html', name=username, glist=goodsList)

@app.route('/temp02/<name>')  # < ... > 라우팅 파라미터 받기
def temp02(name):
    return render_template('/app02/temp02_page.html', uname=name)

if __name__ == "__main__":
    app.run()
