# 제어문 : 조건문(if), 반복문(while, for)

# python 블럭 : 콜론과 들여쓰기

var = 10
if var >= 10:
    print('var =', var)
    print('var는 10보다 크거나 같다.')
print('항상 실행되는 영역')

var = 2
if var >= 5:
    print('var는 5보다 크거나 같다.')
else:
    print('var는 5보다 작다.')

# 키보드 정수 입력 -> 60점 이상 : 합격, 미만 : 불합격
score = int(input('점수 입력 : '))
if score >= 60:
    print('합격')
else:
    print('불합격')

# 시간, 날짜 관련
import datetime  # module import
today = datetime.datetime.now()  # module.class.method()
print(today)

week = today.weekday()  # 0(월) ~ 6(일)
print(week)

if week >= 5:
    print('오늘은 휴일')
else:
    print('오늘은 평일')

# 키보드 score 입력 : A, B, C, D, F
score = int(input('점수 입력(0~100) : '))
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'

print(f'당신의 점수는 {score}이고, 등급은 {grade}이다.')

# 블럭 if vs 라인 if
num = 9
if num >= 5:
    result = num * 2
else:
    result = num + 2
print(result)

# 라인 if : 변수 = 참 if 조건 else 거짓
result = num * 2 if num >= 5 else num + 2