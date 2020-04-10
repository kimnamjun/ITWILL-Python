'''
 문4) 패토리얼(Factorial) 계산 함수를 정의하시오.
     예) 5! -> 5*4*3*2*1 : 120
'''
import time
from math import log10

def Factorial(n):
    return n * Factorial(n-1) if n > 1 else 1


def new_factorial(n, num=[1]):
    ret = num[-1]
    for i in range(len(num), n+1):
        ret *= i
        num.append(ret)
    return num[n], num


def simple_factorial(n):
    ret = 1
    for i in range(1, n+1):
        ret *= i
    return ret


a = time.time()
ret1 = Factorial(900)
b = time.time()
ret2 = new_factorial(40000)
c = time.time()
ret3 = new_factorial(48000, ret2[1])
d = time.time()
ret4 = simple_factorial(100000)
e = time.time()

print('값A :', log10(ret1))
print('값B :', log10(ret2[0]))
print('값C :', log10(ret3[0]))
print('값D :', log10(ret4))

print('재귀함수 시간 :', b-a)
print('처음 실행 시간 :', c-b)
print('다시 실행 시간 :', d-c)
print('간단 함수 출력 시간 :', e-d)
f = time.time()
print('출력 시간 :', f-e)