'''
table 전체 조회 -> 생성 및 조회
1. 없는 경우 : table 생성
2. 있는 경우 : table 조회
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

    # 1. 전체 테이블 조회
    cursor.execute("SHOW TABLES")
    tables = cursor.fetchall()

    sw = False
    if tables:
        for t in tables:
            # print(t[0])
            if t[0] == 'emp':
                sw = True
    if not sw:
        # print('emp 테이블 없음')
        sql1 = """CREATE TABLE emp(
                eno INT PRIMARY KEY AUTO_INCREMENT,
                ename VARCHAR(20) NOT NULL,
                hiredate DATE NOT NULL,
                sal INT,
                bonus INT DEFAULT 0,
                job VARCHAR(20) NOT NULL,
                dno INT)"""
        cursor.execute(sql1)

        sql2 = "ALTER TABLE emp AUTO_INCREMENT = 1001"
        cursor.execute(sql2)

        sql3 = """INSERT INTO emp(ename, hiredate, sal, bonus, job, dno)
                VALUES('홍길동', '2010-10-20', 300, 35, '관리자', 10)"""
        cursor.execute(sql3)
        sql4 = """INSERT INTO emp(ename, hiredate, sal, job, dno)
                        VALUES('강호동', '2015-09-20', 250, '사원', 20)"""
        cursor.execute(sql4)
        sql5 = """INSERT INTO emp(ename, hiredate, sal, job, dno)
                        VALUES('유관순', '2020-10-20', 220, '사원', 10)"""
        cursor.execute(sql5)
        conn.commit()
    else:
        sql = "SELECT * FROM emp"
        cursor.execute(sql)
        data = cursor.fetchall()
        for row in data:
            print(row)
        print(f'전체 레코드 수 : {len(data)}')

        # 사원 조회 : 키보드(이름) -> 사번, 이름, 부서, 칼럼 출력 or '없음'
        name = input('사원 이름 입력 : ')
        sql = f"SELECT eno, ename, dno FROM emp WHERE ename = '{name}'"
        cursor.execute(sql)
        data = cursor.fetchall()
        if data:
            for row in data:
                print(row)
        else:
            print('없음')

        # 삭제도 반복이라 생략

        # 사원 수정 : 키보드(사번, 급여, 보너스) -> 급여 보너스 수정
        no = input('사원 번호 입력 : ')
        sal = input('급여 입력 : ')
        bonus = input('보너스 입력 : ')
        sql = f"UPDATE emp SET sal = {sal}, bonus = {bonus} WHERE eno = {no}"
        cursor.execute(sql)
        conn.commit()

except Exception as e:
    conn.rollback()
    raise e
finally:
    print('프로그램 종료')
    cursor.close()
    conn.close()