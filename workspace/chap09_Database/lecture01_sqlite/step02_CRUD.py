'''
CRUD : Create, Read, Update, Delete
'''
import sqlite3

try:
    conn = sqlite3.connect('../data/sqlite.db')
    cursor = conn.cursor()

    sql = """CREATE TABLE IF NOT EXISTS goods(
            code INTEGER PRIMARY KEY,
            name TEXT(30) UNIQUE NOT NULL,
            num INTEGER DEFAULT 0,
            price REAL DEFAULT 0.0);"""
    cursor.execute(sql)

    # 레코드 추가
    # cursor.execute("INSERT INTO goods VALUES(1, '냉장고', 2, 850000)")
    # cursor.execute("INSERT INTO goods VALUES(2, '세탁기', 3, 550000)")
    # cursor.execute("INSERT INTO goods(code, name) VALUES(3, '전자레인지')")
    # cursor.execute("INSERT INTO goods(code, name, price) VALUES(4, 'HDTV', 1500000)")
    conn.commit()

    # 레코드 수정
    sql = "UPDATE goods SET name = '테스트' WHERE code = 4;"
    cursor.execute(sql)
    conn.commit()

    # 입력 레코드 수정
    # code = int(input("수정할 상품 코드 입력 : "))
    # num = int(input("수량 입력 : "))
    # price = int(input("단가 입력 : "))
    # sql = f"UPDATE goods SET num = {num}, price = {price} WHERE code = {code};"
    # cursor.execute(sql)
    # conn.commit()

    # 레코드 삭제
    # code = int(input("수정할 상품 코드 입력 : "))
    # sql = f"SELECT * FROM goods WHERE code = {code}"
    # cursor.execute(sql)
    # dataset = cursor.fetchall()
    # if dataset:
    #     sql = f"DELETE FROM goods where code = {code}"
    #     cursor.execute(sql)
    #     conn.commit()
    # else:
    #     print('해당 코드 없음')

    # 레코드 조회
    cursor.execute("SELECT * FROM goods")
    dataset = cursor.fetchall()
    for row in dataset:
        print(row)
    print(f'전체 레코드 수 : {len(dataset)}')

    # 키보드 입력 -> 검색
    # name = input('검색할 상품명 입력 : ')
    # cursor.execute(f"SELECT * FROM goods WHERE name LIKE '%{name}%'")
    # dataset = cursor.fetchall()
    # if dataset:
    #     for row in dataset:
    #         print(row)
    # else:
    #     print('검색된 상품 없음')
    # print(f'검색된 레코드 수 : {len(dataset)}')

except Exception as e:
    print('Error')
    conn.rollback()
    raise e
finally:
    cursor.close()
    conn.close()
