'''
문제3) 다음과 같은 메뉴를 이용하여 goods 테이블을 관리하시오.
    [레코드 처리 메뉴 ]
1. 레코드 조회
2. 레코드 추가
3. 레코드 수정
4. 레코드 삭제
5. 프로그램 종료
    메뉴번호 입력 : 
'''    
import pymysql

config = {
    'host' : '127.0.0.1',
    'user' : 'scott',
    'password' : 'tiger',
    'database' : 'work',
    'port' : 3306,
    'charset':'utf8',
    'use_unicode' : True}

try:
    # db 연결 객체 생성 
    conn = pymysql.connect(**config)
    # SQL 실행 객체 생성 
    cursor = conn.cursor()    
    
    while True :  # 무한루프 
        print('\t[레코드 처리 메뉴 ]')
        print('1. 레코드 조회')
        print('2. 레코드 추가')
        print('3. 레코드 수정')
        print('4. 레코드 삭제')
        print('5. 프로그램 종료')    
        menu = int(input('\t메뉴번호 입력 : '))
        
        if menu == 1 :
            cursor.execute("SELECT * FROM goods")
            dataset = cursor.fetchall()
            for row in dataset:
                print(row)

        elif menu == 2:
            code = int(input("code : "))
            name = input("name : ")
            num = int(input("num : "))
            price = int(input("price : "))
            cursor.execute(f"INSERT INTO goods VALUES({code}, '{name}', {num}, {price})")
            conn.commit()

        elif menu == 3:
            code = int(input('수정 code : '))
            num = int(input('수정 num : '))
            price = int(input('수정 price : '))
            cursor.execute(f"SELECT * FROM goods WHERE code = {code}")
            row = cursor.fetchone()

            if row:
                cursor.execute(f"UPDATE goods SET num = {num}, price = {price} WHERE code = {code}")
                conn.commit()
            else:
                print('해당 코드 없음')

        elif menu == 4:
            code = int(input('삭제 code : '))
            cursor.execute(f"SELECT * FROM goods WHERE code = {code}")
            row = cursor.fetchone()

            if row:
                cursor.execute(f"DELETE FROM goods WHERE code = {code}")
                conn.commit()
            else:
                print('해당 코드 없음')
        elif menu == 5 :
            print('프로그램 종료')
            break # 반복 exit
        else :
            print('해당 메뉴는 없습니다.')
        
# DB 연결 예외 처리          
except Exception as e :
    print('db 연동 오류 : ', e)
    conn.rollback()
finally:
    cursor.close()
    conn.close() 
