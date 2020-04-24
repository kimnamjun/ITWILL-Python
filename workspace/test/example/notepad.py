import hashlib
import pymysql
import uuid
import re

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

id = 'user5'
pwd = 'password'
salt = re.sub('-', '', str(uuid.uuid4()))
print(len(salt))
pwd_salt = pwd + salt
print('pwd_salt :', pwd_salt)
sha256.update(pwd_salt.encode())
pwd_salt = sha256.hexdigest()
cursor.execute(f"""INSERT INTO user(id, password, salt) VALUE('{id}', '{pwd_salt}', '{salt}')""")
conn.commit()