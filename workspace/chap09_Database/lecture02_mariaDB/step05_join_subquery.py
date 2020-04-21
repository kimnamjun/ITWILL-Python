'''
emp join dept
subquery : emp vs dept
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

    # 1. join
    sal = input("join 조건 급여 : ")
    sql = f"""SELECT e.eno, e.ename, e.sal, d.dname
    FROM emp e INNER JOIN dept d ON e.dno = d.dno
    WHERE e.sal >= {sal}"""
    cursor.execute(sql)
    data = cursor.fetchall()
    for row in data:
        print(row)

    # 2. subquery : 부서번호(dept) -> 사원정보(emp)
    dno = input("부서 번호 입력 : ")
    sql = f"""SELECT eno, ename, hiredate, dno FROM emp
            WHERE dno = (SELECT dno FROM dept WHERE dno = {dno})"""
    cursor.execute(sql)
    data = cursor.fetchall()
    for row in data:
        print(row)

except Exception as e:
    conn.rollback()
    raise e
finally:
    print('프로그램 종료')
    cursor.close()
    conn.close()