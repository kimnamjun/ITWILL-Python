'''
text 파일을 DB에 저장

< 작업 순서 >
1. table 생성
2. zipcode.txt -> readline(서울) -> 레코드 저장
3. table 저장 -> 동으로 검색

  code  city      gu      dong   detail
135-806	서울	강남구	개포1동 경남아파트		1
135-807	서울	강남구	개포1동 우성3차아파트	(1∼6동)	2
'''
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

    ''' # 테이블 생성
    cursor.execute("""CREATE TABLE zipcode_tab(
                    code CHAR(14) NOT NULL,
                    city CHAR(20) NOT NULL,
                    gu VARCHAR(20) NOT NULL,
                    dong VARCHAR(80) NOT NULL,
                    detail VARCHAR(50))""")
    print('1. table 작성 완료~~~')
    '''

    cursor.execute("SELECT * FROM zipcode_tab")
    data = cursor.fetchall()

    if data:
        for row in data:
            print("[%s] %s %s %s %s"%row)
        print(f'전체 레코드 수 : {len(data)}')

        dong = input("검색할 동 입력 : ")
        sql = f"SELECT * FROM zipcode_tab WHERE dong LIKE '%{dong}%'"
        cursor.execute(sql)
        data = cursor.fetchall()
        if data:
            for row in data:
                print(row)
        else:
            print('동 없음')

    else:
        with open('../data/zipcode.txt', encoding='UTF-8') as file:
            line = file.readline()
            while line:
                row = line.split('\t')
                if row[1] == '서울':
                    code = row[0]
                    city = row[1]
                    gu = row[2]
                    dong = row[3]
                    detail = row[4]

                    if detail:
                        sql = f"""INSERT INTO zipcode_tab(code, city, gu, dong, detail)
                                  VALUES ('{code}', '{city}', '{gu}', '{dong}', '{detail}')"""
                    else:
                        sql = f"""INSERT INTO zipcode_tab(code, city, gu, dong)
                                  VALUES ('{code}', '{city}', '{gu}', '{dong}')"""
                    cursor.execute(sql)
                    conn.commit()
                    line = file.readline()
            print('2. 레코드 추가 성공~~')


except Exception as e:
    conn.rollback()
    raise e
finally:
    cursor.close()
    conn.close()