'''
함수의 가변인수
- 한 개의 가인수로 여러 개의 실인수를 받는 이수
형식) def 함수명(*인수)
'''


# 1. tuple형으로 받는 가변인수
def func1(name, *names):
    print(name)
    print(names)


func1('Hello', 'My Name', 'is', 'Kim NamJun')

import scatter.scatter_module  # 방법1)
from scatter.scatter_module import avg, var_std  # 방법2)

data = [2, 3, 5, 6, 7, 8.5]

avg1 = scatter.scatter_module.avg(data)
avg2 = avg(data)
print(avg1)
print(avg2)


def statics(func, *data):
    if func == 'sum':
        return sum(data)
    if func == 'avg':
        return avg(data)
    if func == 'var':
        return var_std(data)
    if func == 'std':
        return var_std(data)
    else:
        return '해당 함수 없음'


print(statics('sum', 1, 2, 3, 4, 5))
var, _ = statics('var', 1, 2, 3, 4, 5)  # 변수 이름 _ 공간 채우기용 변수
_, std = statics('std', 1, 2, 3, 4, 5)


# 2. dict형 가변인수
def person(w, h, **other):
    print(f'weight = {w}')
    print(f'height = {h}')
    print(other)

person(65, 175, name='홍길동', age=35)


# 3. 함수를 인수로 받기
def sqaure(x):
    return x ** 2

def my_func(func, data):
    result = [func(d) for d in data]
    return result

dataset = [1,2,3,4,5]
print(my_func(sqaure, dataset))
