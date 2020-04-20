import pymysql

print(pymysql.version_info)

config = {
    'host' : '127.0.0.1',
    'user' : 'scott',
    'password' : 'tiger',
    'database' : 'work',
    'port' : 3306,
    'charset':'utf8',
    'use_unicode' : True
}

try:
    # DB 연동 객체
    conn = pymysql.connect(**config)  # 전에 배웠던 dict 가변인수

    # SQL 실행 객체
    cursor = conn.cursor()

    # SQL 실행
    cursor.execute("SELECT * FROM goods")
    dataset = cursor.fetchall()

    for row in dataset:
        print(row)

except Exception as e:
    conn.rollback()
    raise e
finally:
    print('프로그램 종료')
    cursor.close()
    conn.close()