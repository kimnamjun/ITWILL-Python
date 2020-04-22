'''
1. templates 파일 작성
- 사용자 요청과 서버의 응답을 작성하는 html file
2. static 파일 작성
- 정적 파일 : image file, js, css 등
'''
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('/app01/index.html')  # templates 라는 폴더명은 자동으로 인식

@app.route('/info')
def info():
    return render_template('/app01/info.html')


# 프로그램 시작점
if __name__ == "__main__":
    app.run()  # application 실행
