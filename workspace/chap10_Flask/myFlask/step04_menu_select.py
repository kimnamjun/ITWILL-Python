'''
get vs post
- 파라미터 전송 방식
- get : url에 노출(소량)
- post : body에 포함되어 전송(대량)

<작업순서>
1. index 페이지 : 메뉴 선택(radio or select) -> get 방식
2. flask server 파라미터 받기(메뉴 번호)
3. 메뉴 번호에 따라서 각 페이지로 이동
'''
from flask import Flask, render_template, request


def db_conn():
    import pymysql

    config = {
        'host': '127.0.0.1',
        'user': 'scott',
        'password': 'tiger',
        'database': 'work',
        'port': 3306,
        'charset': 'utf8',
        'use_unicode': True
    }

    conn = pymysql.connect(**config)
    cursor = conn.cursor()
    return conn, cursor


def select_func():
    conn, cursor = db_conn()
    cursor.execute("SELECT * FROM goods")
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return data


app = Flask(__name__)

@app.route('/')
def index():
    return render_template("/app04/index.html")

@app.route('/select', methods=['GET','POST'])
def select():
    # if request.method == 'GET': 이하 생략
    # GET은 args를 사용, POST는 form을 사용
    menu = request.args.get('menu')  # menu는 html 파일의 name
    print(menu)

    # 전체 레코드 조회
    if menu == 'read':
        data = select_func()
        return render_template("/app04/select.html", data=data)

    # 레코드 추가
    elif menu == 'create':
        return render_template("/app04/insert_form.html")

    # 레코드 수정
    elif menu == 'update':
        return render_template("/app04/update_form.html")

    # 레코드 삭제
    elif menu == 'delete':
        return render_template("/app04/delete_form.html")


@app.route('/insert', methods=['POST'])
def insert():
    try:
        code = request.form['code']
        name = request.form['name']
        num = request.form['num']
        price = request.form['price']

        conn, cursor = db_conn()
        cursor.execute(f"INSERT INTO goods VALUES({code}, '{name}', {num}, {price})")
        conn.commit()
        cursor.close()
        conn.close()

    except Exception as e:
        return render_template("/app04/message.html", error_info=e)

    data = select_func()
    return render_template('/app04/select.html', data=data)


@app.route('/update', methods=['POST'])
def update():
    try:
        code = request.form['code']
        num = request.form['num']
        price = request.form['price']

        conn, cursor = db_conn()
        cursor.execute(f"SELECT * FROM goods WHERE code = {code}")
        row = cursor.fetchone()

        if row:
            cursor.execute(f"UPDATE goods SET num = {num}, price = {price} WHERE code = {code}")
            conn.commit()
        cursor.close()
        conn.close()

    except Exception as e:
        return render_template("/app04/message.html", error_info=e)

    data = select_func()
    return render_template('/app04/select.html', data=data)


@app.route('/delete', methods=['POST'])
def delete():
    try:
        code = request.form['code']

        conn, cursor = db_conn()
        cursor.execute(f"SELECT * FROM goods WHERE code = {code}")
        row = cursor.fetchone()
        print(row)
        if row:
            cursor.execute(f"DELETE FROM goods WHERE code = {code}")
            conn.commit()
        cursor.close()
        conn.close()

    except Exception as e:
        return render_template("/app04/message.html", error_info=e)

    data = select_func()
    return render_template('/app04/select.html', data=data)


if __name__ == "__main__":
    app.run()
