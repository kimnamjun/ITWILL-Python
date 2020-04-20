'''
sqlite3
- 내장형 DBMS(database management system) : 기기 내부에서만 사용 가능
- 외부 접근 불가능
'''
import sqlite3
print(sqlite3.sqlite_version_info)

try:
    # database 생성
    conn = sqlite3.connect('../data/sqlite.db')
    # sql 실행 객체
    cursor = conn.cursor()

    # table 생성
    sql = """CREATE TABLE IF NOT EXISTS test_tab(
            name TEXT(10),
            phone TEXT(15),
            addr TEXT(50));"""
    cursor.execute(sql)  # table 생성

    # 레코드 추가
    cursor.execute("INSERT INTO test_tab VALUES('홍길동','010-1111-1111','서울')")
    cursor.execute("INSERT INTO test_tab VALUES('이순신','010-1111-1111','해남')")
    cursor.execute("INSERT INTO test_tab VALUES('유관순','010-1111-1111','충남')")
    conn.commit()

    # 레코드 조회
    cursor.execute("SELECT * FROM test_tab")
    dataset = cursor.fetchall()
    print('   이름        전화번호      주소')
    for row in dataset:
        print(row)

except sqlite3.OperationalError as e:
    print(f'DB 오류 : {e}')
    conn.rollback()

finally:
    cursor.close()
    conn.close()