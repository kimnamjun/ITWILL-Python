'''
group by 집단 변수(범주형)
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

    # 1. 부서, 2. 직책
    gcol = input('1. 부서, 2. 직책 : ')
    if gcol == '1':
        sql="""SELECT dno, SUM(sal), ROUND(AVG(sal), 2)
                FROM emp
                GROUP BY dno
                ORDER BY dno"""
        cursor.execute(sql)
        data = cursor.fetchall()
        for row in data:
            print(f'dno:{row[0]} / sum:{row[1]} / avg:{row[2]}')

    elif gcol == '2':
        sql = """SELECT job, SUM(sal), ROUND(AVG(sal), 2)
                        FROM emp
                        GROUP BY job
                        ORDER BY job"""
        cursor.execute(sql)
        data = cursor.fetchall()
        for row in data:
            print(f'job:{row[0]} / sum:{row[1]} / avg:{row[2]}')
    else:
        print('잘못된 명령어')

except Exception as e:
    conn.rollback()
    raise e
finally:
    print('프로그램 종료')
    cursor.close()
    conn.close()