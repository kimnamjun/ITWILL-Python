import pymysql
from flask import Flask, render_template, request

def db_conn():

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
    return render_template("/app05/main.html")


@app.route('/docForm')
def docForm():
    return render_template("/app05/docForm.html")


@app.route('/docPro', methods=['GET','POST'])
def docPro():
    if request.method == 'POST':
        doc_id = request.form['id']
        major = request.form['major']

        conn, cursor = db_conn()
        cursor.execute(f"SELECT * FROM doctors WHERE doc_id = {doc_id} and major_treat = '{major}'")
        row = cursor.fetchone()
        size = 0
        data = 0
        if row:
            cursor.execute(f"""SELECT doc_id, pat_id, treat_contents, tread_date
                               FROM doctors NATURAL JOIN treatments WHERE doc_id = {doc_id}""")
            data = cursor.fetchall()
            if data:
                size = len(data)
                for row in data:
                    print(row)
            return render_template("/app05/docPro.html", dataset= data, size=size)

    return render_template("/app05/message.html", info="ID 또는 진료 과목 확인")


@app.route('/nurseForm')
def nurseForm():
    return render_template("/app05/nurseForm.html")


@app.route('/nursePro', methods=['GET','POST'])
def nursePro():
    if request.method == 'POST':
        nurse_id = request.form['id']

        conn, cursor = db_conn()
        cursor.execute(f"SELECT * FROM nurses WHERE nur_id = {nurse_id}")
        row = cursor.fetchone()
        size = 0
        data = 0
        if row:
            cursor.execute(f"""SELECT nur_id, pat_id, pat_name, pat_phone
                               FROM nurses NATURAL JOIN patients WHERE nur_id = {nurse_id}""")
            data = cursor.fetchall()
            if data:
                size = len(data)
                for row in data:
                    print(row)
        return render_template("/app05/nursePro.html", dataset= data, size=size)

    return render_template("/app05/message.html", info="ID 확인")


if __name__ == "__main__":
    app.run()
