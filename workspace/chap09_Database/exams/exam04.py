'''
문제4) emp.csv 파일을 읽어서 다음과 같이 db 테이블에 저장하시오.
 <조건1> 테이블명 : emp_table
 <조건2> 사원 이름으로 레코드 조회(sql문 작성)
 
 <작업순서>
 1. table 생성 : emp_table(sql 폴더)
 2. python code : 레코드 추가 
 3. python code : 레코드 조회(사원이름)  
'''

import pymysql
import pandas as pd 

# 칼럼 단위 읽기 
emp = pd.read_csv("../data/emp.csv", encoding='utf-8')
# print(emp)
# No Name  Pay
no = emp.No
name = emp.Name
pay = emp.Pay
# print(no, name, pay)

config = {
    'host' : '127.0.0.1',
    'user' : 'scott',
    'password' : 'tiger',
    'database' : 'work',
    'port' : 3306,
    'charset':'utf8',
    'use_unicode' : True}

try:
    conn = pymysql.connect(**config)
    cursor = conn.cursor()

    # 테이블 생성 후 주석 처리
    # cursor.execute("CREATE TABLE emp_table(no INT PRIMARY KEY, name VARCHAR(10) NOT NULL, pay INT)")

    # 레코드 추가 후 주석 처리
    # for idx, val in enumerate(no):
    #     cursor.execute(f"INSERT INTO emp_table VALUES({no[idx]}, '{name[idx]}', {pay[idx]})")
    # conn.commit()

    employee = input("검색할 사원 이름 : ")
    cursor.execute(f"SELECT * FROM emp_table WHERE name = '{employee}'")
    data = cursor.fetchall()
    if data:
        for row in data:
            print(row)
    else:
        print('사원 없음')

except Exception as e:
    conn.rollback()
    raise e
finally:
    cursor.close()
    conn.close()