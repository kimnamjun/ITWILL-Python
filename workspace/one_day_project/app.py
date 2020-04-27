from flask import Flask, render_template, request, session
import pymongo
import hashlib
import uuid
import re
from datetime import datetime

app = Flask(__name__)
app.secret_key = b'123456'

host = "mongodb+srv://scott:tiger@mycluster-8i5m0.mongodb.net/test?retryWrites=true&w=majority"
conn = pymongo.MongoClient(host)

db = conn["oneday"]
cUser = db["user"]
cRoom = db['room']
cChat = db['chat']
cInvite = db['invite']
cInfo = db['info']

@app.route('/', methods=['GET', 'POST'])
def index():
    try:
        cmd = request.form['cmd']
    except Exception as e:
        cmd = None

    if cmd == "signup":
        id = request.form['id']
        pwd = request.form['pwd']
        pwdc = request.form['pwdc']

        if len(id) < 4:
            error = '아이디가 너무 짧습니다. 4자 이상으로 입력해주세요.'
            return render_template("/message.html", msg=error)
        if pwd != pwdc:
            error = '비밀번호가 서로 다릅니다. 다시 한 번 확인해주세요.'
            return render_template("/message.html", msg=error)
        if len(pwd) < 6:
            error = '비밀번호가 너무 짧습니다. 6자 이상으로 입력해주세요.'
            return render_template("/message.html", msg=error)

        user = [row for row in cUser.find({"id": id})]
        if user:
            error = '아이디가 중복되었습니다. 다른 아이디를 입력해주세요.'
            return render_template("/message.html", msg=error)

        salt = str(uuid.uuid4())
        pwd_salt = pwd + salt
        sha256 = hashlib.sha256()
        sha256.update(pwd_salt.encode())
        pwd_encrypt = sha256.hexdigest()

        cUser.insert({
            "id": id,
            "pwd": pwd_encrypt,
            "salt": salt,
            "nickname": ''
        })

        session['id'] = id

    elif cmd == "login":
        id = request.form['id']
        pwd = request.form['pwd']

        user = cUser.find_one({"id": id})
        if user:
            salt = user['salt']
            pwd_salt = pwd + salt
            sha256 = hashlib.sha256()
            sha256.update(pwd_salt.encode())
            pwd_encrypt = sha256.hexdigest()

            if pwd_encrypt == user['pwd']:
                session['id'] = id
            else:
                error = '해당 아이디를 찾을 수 없습니다.'
                return render_template("/message.html", msg=error)

        else:
            error = '해당 아이디를 찾을 수 없습니다.'
            return render_template("/message.html", msg=error)

    elif cmd == "exit":
        no = int(request.form['no'])
        sess = session['id']
        cRoom.update_one({"no": no}, {"$pull": {"users": sess}})

    elif cmd == "logout":session.pop('id', None)

    try:
        sess = session['id']
    except Exception:
        sess = None

    if sess and cmd == "invite":
        no = int(request.form['no'])
        cInvite.delete_many({"ivt_to": sess, "no": no})
        cRoom.update_one({"no": no}, {"$push": {"users": sess}})

    invite = [row for row in cInvite.find({"ivt_to": sess})]
    room = [row for row in cRoom.find() if sess in row['users']]

    return render_template("/index.html", sess=sess, invite=invite, room=room)

@app.route('/message', methods=['POST'])
def msg():
    return render_template("/message.html")

@app.route('/create', methods=['POST'])
def create():
    return render_template("/create.html")

@app.route('/signup', methods=['POST'])
def signup():
    return render_template("/signup.html")

@app.route('/login', methods=['POST'])
def login():
    return render_template("/login.html")

@app.route('/room', methods=['POST'])
def room():
    try:
        cmd = request.form['cmd']
    except Exception:
        cmd = None

    no = 0
    if cmd == 'create':
        room_name = request.form['room_name']
        room_name = re.sub(r'[^\w_ ]+', '', room_name)
        sess = session['id']
        no = cInfo.find_one()['next_room_no']
        cInfo.update_one({}, {"$inc":{"next_room_no": 1}})
        cRoom.insert_one({
            "no": no,
            "room_name": room_name,
            "users": [sess]
        })

    elif cmd == "send":
        no = int(request.form['no'])
        text = request.form['text']
        try:
            sess = session['id']
        except Exception:
            sess = None

        cChat.insert({
            "cid": 1,
            "id": sess,
            "no": no,
            "time": datetime.now(),
            "text": text
        })

    elif cmd == "invite":
        no = int(request.form['no'])
        ivt_from = request.form['ivt_from']
        try:
            ivt_to = request.form['ivt_to']
        except Exception:
            ivt_to = None
        cInvite.insert_one({
            "no": no,
            "ivt_from": ivt_from,
            "ivt_to": ivt_to
        })

    elif cmd == "join":
        no = int(request.form['no'])

    sess = session['id']
    name = cRoom.find_one({"no": no})['room_name']

    data = [row for row in cChat.find({"no": no})]
    return render_template("/room.html", id=sess, no=no, name=name, chat=data)

if __name__ == "__main__":
    app.run()
