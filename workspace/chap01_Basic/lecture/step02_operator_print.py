# 연산자
# 1. 변수에 값 할당(=)
# 2. 연산자 : 산술, 관계, 논리
# 3. print 형식
# 4. input : 키보드 입력

# 1. 변수에 값 할당(=)
i = tot = 10
i += 1
tot += i
print(f'i = {i}')
print(f'tot = {tot}')

v1, v2 = 100, 200
print(f'v1 = {v1}, v2 = {v2}')
v1, v2 = v2, v1
print(f'v1 = {v1}, v2 = {v2}')

# 패킹(packing) 할당
lst = [1, 2, 3, 4, 5]  # vector: 1차원
v1, *v2 = lst
print(f'v1 = {v1}, v2 = {v2}')
*v1, v2 = lst
print(f'v1 = {v1}, v2 = {v2}')


# 2. 연산자 : 산술, 관계, 논리
num1 = 100 # 피연산자1
num2 = 20.5  # 피연산자2

# 산술 연산자
add = num1 + num2
sub = num1 - num2
mul = num1 * num2
div = num1 / num2
div2 = num1 // num2
div3 = num1 % num2
square = num1 ** num2
print(add, sub, mul)
print(div, div2, div3)
print(square)

# 관계 연산자
# 1) 동등 비교
bool_re = num1 == num2
print(bool_re)

# 2) 대소 관계
bool_re = num1 >= num2
print(bool_re)

# 3) 논리 연산자 : and, or, not
bool_re = num1 >= num2 and num1 <= 10
print(bool_re)

bool_re = num1 >= num2 or num1 <= 10
print(bool_re)

bool_re = not num1 >= num2 or num1 <= 10
print(bool_re)


# 3. print 형식
help(print)
# package > module > function or class
# Help on built-in function print in module builtins
# print(value, ..., sep=' ', end='\n', ...)
# module builtins : 기본 모듈(python 설치 시 자동으로 설치되는 모듈)

# 1) 기본 인수
print('values =', 10 + 20 + 30)
print("출력1", end = ', ')
print("출력2")
print("010", "1111", "2222", sep='-')

# 2) format(value, '형식')
print("원주율=", format(3.14159, "8.3f"))
print("금액 =", format(10000, "10d"))
print("금액 =", format(125000, "3,d"))  # 금액 = 125,000

# 3) print("양식문자", %(값)) 양식문자 p22
num1 = 10; num2 = 20
tot = num1 + num2
print("%d + %d = %d" %(num1, num2, tot))
print("8진수 : %o, 16진수 : %x" %(num1, num1))
print("%s : %8.3f" %('PI', 3.14159))

# 4) 외부 상수 받기
# '{}, {}'.format(value)
print('name : {}, age : {}'.format('홍길동', 35))
print('name : {1}, age : {0}'.format(35, '홍길동'))

# fstring : select * from emp where name = '홍길동'
name = '홍길동'
age = 35
sql = f"SELECT * FROM emp WHERE name = '{name}' and age = {age}"
print(sql)


# 4. input("prompt") : 키보드 입력(문자 인식)
'''
형 변환 관련 함수
int(value) : value -> integer
float(value) : value -> float
str(value) : value -> string
bool(value) : value -> bool
'''

# 간단 예제
a = int(input("첫 번째 숫자 입력 : "))
b = int(input("두 번째 숫자 입력 : "))
print("a + b = ", a + b)

a = float(input("첫 번째 숫자 입력 : "))
b = float(input("두 번째 숫자 입력 : "))
print("a + b = ", a + b)

# boolean -> int
print(int(False)) # 0
print(int(True))  # 1

# int -> boolean
print(bool(1))  # True
print(bool(0))  # False
print(bool(-1)) # True
