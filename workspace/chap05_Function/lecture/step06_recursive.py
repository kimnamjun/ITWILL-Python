'''
재귀호출(recursive call)
- 함수 내에서 자신의 함수를 반복적으로 호출하는 기법
- 반복적으로 변수의 값을 조정해서 연산 수행
ex) 1 ~ n (1 + 2 + ... + n)
- 반드시 종료조건 필요
'''

# 1. 카운터 : 1 ~ n
def counter(n):
    if n == 0:  # 종료 조건
        print('프로그램 종료')
        return 0  # 함수 종료
    else:
        counter(n-1)
        print(n, end=' ')

counter(5)
print()

# 2. snwjr(1 + 2 + ... + n)

def Adder(n):
    if n == 1:
        return 1
    else:
        return n + Adder(n-1)

print(Adder(2))