'''
문) emp 테이블을 대상으로 사원명을 조회하는 application 을 구현하시오.
  조건1> index 페이지에서 사원명을 입력받아서 post 방식 전송
  조건2> 해당 사원이 있으면 result 페이지에 사번, 이름, 직책, 부서번호 칼럼 출력
  조건3> 해당 사원이 없으면 result 페이지에 '해당 사원 없음' 이라고 출력
'''
import pymysql
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("/exam01/index.html")

@app.route('/result', methods=['POST'])
def search():
    employee = request.form['employee']

    config = {
        'host': '127.0.0.1',
        'user': 'scott',
        'password': 'tiger',
        'database': 'work',
        'port': 3306,
        'charset': 'utf8',
        'use_unicode': True
    }

    try:
        conn = pymysql.connect(**config)
        cursor = conn.cursor()

        sql = f"SELECT * FROM emp WHERE ename LIKE '%{employee}%'"
        cursor.execute(sql)
        data = cursor.fetchall()
        if data:
            for row in data:
                print(row)
        else:
            print('해당 사원 없음')

    except Exception as e:
        conn.rollback()
        raise e
    finally:
        cursor.close()
        conn.close()
    return render_template('/exam01/result.html', employee= employee, data= data)


if __name__ == "__main__":
    app.run()
