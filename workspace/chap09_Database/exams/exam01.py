'''
문제1) goods 테이블을 이용하여 다음과 같은 형식으로 출력하시오.  
 <조건1> 전자레인지 수량, 단가 수정 
 <조건2> HDTV 수량 수정 

    [ goods 테이블 현황 ]
1 냉장고 2 850000
2 세탁기 3 550000
3 전자레인지 5  600000 <- 수량, 단가 수정
4 HDTV 2 1500000  <- 수량 수정
전체 레코드 수 : 4
'''
import sqlite3

try :
    conn = sqlite3.connect('../data/sqlite.db')
    cursor = conn.cursor()

    cursor.execute("DELETE FROM goods")
    cursor.execute("INSERT INTO goods VALUES(1, '냉장고', 2, 850000)")
    cursor.execute("INSERT INTO goods VALUES(2, '세탁기', 3, 550000)")
    cursor.execute("INSERT INTO goods VALUES(3, '전자레인지', 1, 100000)")
    cursor.execute("INSERT INTO goods VALUES(4, 'HDTV', 1, 1500000)")

    num, price = map(int, input('전자레인지 수량, 단가 입력 : ').split())
    cursor.execute(f"UPDATE goods SET num = {num}, price = {price} WHERE code = 3")
    num = int(input('HDTV 수량 입력 : '))
    cursor.execute(f"UPDATE goods SET num = {num} WHERE code = 4")
    conn.commit()

    cursor.execute("SELECT * FROM goods")
    dataset = cursor.fetchall()
    for row in dataset:
        print(row)

except Exception as e :
    print('ERROR')
    raise e

finally:
    print('프로그램 종료')
    cursor.close()
    conn.close()



