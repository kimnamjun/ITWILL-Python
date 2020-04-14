'''
문6) 다음과 같은 조건으로 모듈을 추가하고, 결과를 확인하시오.
   모듈 위치 : mymodule 패키지 
   모듈명 : module02.py
   함수 정의 : 사칙연산 수행 함수 (Add, Sub, Mul, Div)
   모듈 import : 방법2) 적용
   사칙연산 함수 호출하여 결과 확인
  
    <<출력 결과 예>>
  x = 10; y = 5 일 때
  Add= 15
  Sub= 5
  Mul= 50
  Div= 2.0
'''

from chap06_Class.package_test.module02 import add, sub, mul, div
x = 10; y = 5
print(f'Add = {add(x, y)}\nSub = {sub(x, y)}\nMul = {mul(x, y)}\nDiv = {div(x, y)}')