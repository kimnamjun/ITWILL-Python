'''
1. 축약함수(lambda)
- 한 줄 함수
- 형식) 변수 = lambda 인수 : 리턴값
'''

# 1. 축약함수 lambda
def adder(x, y):
    add = x + y
    return add


add = lambda x, y: x + y
# [lambda x, y: x + y for 변수 in 열거형 객체]

result = add(10, 20)
print(result)


'''
# 2. scope
- 전역변수 : 전 지역에서 사용되는 변수
- 특정 지역(함수)에서만 사용되는 변수
'''

x = 50
def local_function(x):
    x += 50

local_function(x)
print(x)

def global_function():
    global x
    x += 50
global_function()
print(x)
