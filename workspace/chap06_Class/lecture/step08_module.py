'''
패키지(package) : 폴더 유사함
- 유사한 모듈 파일을 저장하는 공간
모듈(module) : 파일 유사함
- 파이썬 파일(*.py)
클래스, 함수
- 모듈에 포함되는 단위
'''

from chap06_Class.package_test.module01 import adder, Sub

sub = Sub(10, 20)
print(f'sub = {sub.calc()}')

print(f'add = {adder(10, 30)}')