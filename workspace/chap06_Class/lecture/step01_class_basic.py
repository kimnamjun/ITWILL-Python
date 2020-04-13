'''
클래스(class)
- 함수의 모임
- 역할 : 다수의 함수와 공유 자료를 묶어서 객체(object) 생성
- 구성 요소 : 멤버(member) + 생성자
- 멤버(member) : 변수(자료 저장) + 함수(메소드)(자료 처리)
- 생성자 : 객체 생성
형식)
class 클래스명:
    멤버변수  = 자료
    멤버메소드() : 자료 처리
    생성자 : 객체 생성
'''


# 1. 중첩 함수
def calc_func(a, b):  # outer : 자료 저장
    # 자료 저장
    x = a
    y = b

    # inner : 자료 처리(조작)
    def plus():
        return x + y

    def minus():
        return x - y

    return plus, minus


p, m = calc_func(20, 10)  # 일급 함수
print(f' plus = {p()}')
print(f'minus = {m()}')


# 2. 클래스 정의
class CalcClass:
    # 멤버 변수 : 자료 저장
    x = y = 0
    def __init__(self, a, b):
        # 멤버 변수 초기화
        self.x = a
        self.y = b

    # 멤버 메소드 : 클래스에서 정의한 함수
    def plus(self):
        return self.x + self.y

    def minus(self):
        return self.x - self.y


# 클래스(1) vs 객체(n)

# 생성자 -> 객체(Object)
obj1 = CalcClass(2, 1)  # 클래스명() : 생성자 -> 객체 생성
# object.member() : 멤버 메소드 호출
print(f' plus = {obj1.plus()}')
print(f'minus = {obj1.minus()}')
# object.member : 멤버 변수 호출
print(f'    x = {obj1.x}')
print(f'    y = {obj1.y}')

# 생성자 -> 객체2
obj2 = CalcClass(200, 100)
print(f' plus = {obj2.plus()}')
print(f'minus = {obj2.minus()}')
print(f'    x = {obj2.x}')
print(f'    y = {obj2.y}')

# 객체 주소 확인
print(id(obj1), id(obj2))  # 9560824 9560872


# 3. 라이브러리 클래스
from datetime import date
today = date(2020, 4, 13)  # 생성자

# object.member
print(f' year : {today.year}')
print(f'month : {today.month}')
print(f'  day : {today.day}')

# object.member() = method
week = today.weekday()
print(f' week : {week}')  # 0 -> 월요일
