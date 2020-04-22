'''
<작업 순서>
1. index 페이지 작성 -> 동 입력
2. flask server에서 동(파라미터) 받기
3. db 연동 -> 주소 조회
4. 조회 결과 -> result 페이지 출력
'''
import pymysql
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("/app03/index.html")


@app.route('/search', methods=['GET', 'POST'])  # GET도 가능하고 POST도 가능함
def search():
    if request.method == 'POST':
        dong = request.form['dong']  # form 안의 dong은 input TAG 안의 name임
        print(f'dong = {dong}')

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

            sql = f"SELECT * FROM zipcode_tab WHERE dong LIKE '%{dong}%'"
            cursor.execute(sql)
            data = cursor.fetchall()
            if data:
                for row in data:
                    print(row)
                size = len(data)
            else:
                print('동 없음')
                size = 0

        except Exception as e:
            conn.rollback()
            raise e
        finally:
            cursor.close()
            conn.close()
        return render_template('/app03/result.html', dong= dong, data= data, size= size)


if __name__ == "__main__":
    app.run()
