'''
중첩함수(inner function)

형식)
def outer_func(인수):
    실행문
    def inner_func(인수):
        실행문

    return inner_func
'''

# 1. 중첩 함수 예시
def a():
    print('a 함수')
    def b():
        print('b 함수')
    return b


b = a()  # outer 호출 - a 함수 = 일급함수
b()      # inner 호출 - b 함수


# 2. 중첩함수 응용
'''
inner 함수 종류
getter() : 함수 안의 data를 외부 획득자
setter() : 함수 안의 data를 지정자
'''

def outer_func(data):  # 역할 : 데이터 저장, inner 포함
    dataset = data

    # inner : 데이터 조작
    def tot():
        tot_val = sum(dataset)
        return tot_val

    def avg(tot_val):
        avg_val = tot_val / len(dataset)
        return avg_val

    # getter()
    def get_data():
        return dataset

    # setter
    def set_data(new_data):
        nonlocal dataset
        dataset = new_data

    return tot, avg, get_data, set_data


data = list(range(1, 101))
tot, avg, get_data, set_data = outer_func(data)
tot_val = tot()
avg_val = avg(tot_val)

print(tot_val)
print(avg_val)

new_data = list(range(1, 51))
set_data(new_data)

print(get_data())
print(tot())


# 3. 함수 장식자 : Tensorflow2.0에서 적용
# - 기존 함수의 시작부분과 종료부분에 기능을 추가해서 장식 역할
'''
@함식장식자
def 함수명():
    실행문
'''

# 함수 장식자 작성
def hello_deco(func):  # outer : 함수를 인수로 받음
    def inner(name):       # inner : 함수 장식하는 역할
        print('-' * 20)
        func(name)  # 함수 실행
        print('-' * 20)
    return inner


@hello_deco
def hello(name):
    print(f'My Name is {name}!')

hello('Gnar')

# 구구단 장식하기
'''
**** 2단 ****
 2 * 1 = 2
    :
 2 * 9 = 18
*************
'''

def gugu_deco(func):
    def deco(i):
        print(f'**** {i}단 ****')
        func(i)
        print('*************')
    return deco

@gugu_deco
def gugu(i):
    for j in range(1, 10):
        print(f' {i} * {j} = {i * j}')

dan = int(input('단 입력 : '))

gugu(dan)