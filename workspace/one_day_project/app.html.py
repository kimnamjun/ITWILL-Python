from flask import Flask, render_template, request
import pymysql
import hashlib
import uuid
import re

app = Flask(__name__)
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
sha256 = hashlib.sha256()

@app.route('/')
def index():
    cursor.execute(f"SELECT * FROM room")
    data = cursor.fetchall()
    return render_template("/index.html", room=data)

@app.route('/main')
def main():
    cursor.execute(f"SELECT * FROM room")
    data = cursor.fetchall()
    return render_template("/index.html", room=data)

@app.route('/message', methods = ['POST'])
def msg():
    return render_template("/message.html")

@app.route('/create', methods = ['POST'])
def create():
    return render_template("/create.html")

@app.route('/signup', methods = ['POST'])
def signup():
    return render_template("/signup.html")


@app.route('/create/submit', methods = ['POST'])
def create_submit():
    room_name = request.form['room_name']
    room_name = re.sub(r'[^\w_ ]+', '', room_name)
    user_id = 'user_id_test'
    cursor.execute(f"INSERT INTO room(room_name, users) VALUES('{room_name}', '{user_id}')")
    conn.commit()

    cursor.execute("SELECT LAST_INSERT_ID()")
    num = cursor.fetchone()

    return render_template("/room.html", no=num)


@app.route('/signup/submit', methods = ['POST'])
def signup_submit():
    id = request.form['id']
    pwd = request.form['pwd']
    pwdc = request.form['pwdc']

    if pwd != pwdc:
        error = '비밀번호가 서로 다릅니다. 다시 한 번 확인해주세요.'
        return render_template("/message.html", msg=error)
    if len(pwd) < 6:
        error = '비밀번호가 너무 짧습니다. 6자 이상으로 입력해주세요.'
        return render_template("/message.html", msg=error)
    cursor.execute(f"SELECT id FROM user WHERE id = '{id}'")
    if cursor.fetchall():
        error = '아이디가 중복되었습니다. 다른 아이디를 입력해주세요.'
        return render_template("/message.html", msg=error)
    salt = re.sub('-', '', str(uuid.uuid4()))
    pwd_salt = pwd + salt
    sha256.update(pwd_salt.encode())
    pwd_salt = sha256.hexdigest()
    cursor.execute(f"""INSERT INTO user(id, password, salt) VALUE('{id}', '{pwd_salt}', '{salt}')""")
    conn.commit()
    msg = "성공적으로 가입되었습니다."
    return render_template("/message.html", msg=msg)


@app.route('/room', methods = ['POST'])
def room():
    no = 1
    try:
        cmd = request.form['cmd']
    except Exception:
        cmd = None
        no = request.form['no']

    if cmd == 'create_room':
        room_name = request.form['room_name']
        room_name = re.sub(r'[^\w_ ]+', '', room_name)
        user_id = 'user_id_test'
        cursor.execute(f"INSERT INTO room(room_name, users) VALUES('{room_name}', '{user_id}')")
        conn.commit()
        cursor.execute("SELECT MAX(no) FROM room")
        no = cursor.fetchone()[0]

    cursor.execute(f"SELECT * FROM room WHERE no = {no}")
    name = cursor.fetchone()[1]

    cursor.execute(f"SELECT * FROM chat WHERE no = {no}")
    data = cursor.fetchall()

    return render_template("/room.html", no=no, name=name, chat=data)

@app.route('/room/send', methods = ['POST'])
def room_send():
    text = request.form['text']
    cursor.execute(f"INSERT INTO chat(id, no, time, text) VALUES('new_id', 1, NOW(), '{text}'")
    conn.commit()
    return render_template("/room.html")


if __name__ == "__main__":
    app.run()