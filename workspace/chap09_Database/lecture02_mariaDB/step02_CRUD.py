import pymysql

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
    conn = pymysql.connect(**config)
    cursor = conn.cursor()

    # READ
    '''
    # 상품명 조회
    name = input('조회 상품명 입력 : ')
    cursor.execute(f"SELECT * FROM goods WHERE name LIKE '%{name}%'")
    dataset = cursor.fetchall()
    for row in dataset:
        print(row)

    # 상품명 조회
    code = input('조회 코드 입력 : ')
    cursor.execute(f"SELECT * FROM goods WHERE code = {code}")
    data = cursor.fetchone()  # 결과 값이 하나만 있을 때 fetchone 사용 / 자료형이 다름
    print(data)
    '''

    # DELETE
    '''
    code = int(input('삭제 code : '))
    cursor.execute(f"SELECT * FROM goods WHERE code = {code}")
    row = cursor.fetchone()

    if row:
        cursor.execute(f"DELETE FROM goods WHERE code = {code}")
        conn.commit()
    else:
        print('해당 코드 없음')
    '''

    # CREATE & UPDATE
    '''
    code = int(input("code : "))
    name = input("name : ")
    num = int(input("num : "))
    price = int(input("price : "))
    cursor.execute(f"INSERT INTO goods VALUES({code}, '{name}', {num}, {price})")
    conn.commit()
    '''

    # 전체 데이터 조회
    cursor.execute("SELECT * FROM goods")
    dataset = cursor.fetchall()
    for row in dataset:
        print(row)


except Exception as e:
    raise e
    conn.rollback()
finally:
    cursor.close()
    conn.close()