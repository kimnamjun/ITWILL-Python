'''
list 특징
- 1차원 배열 구조
- 다양한 자료형 저장 가능
- index 사용, 순서 존재
- 값 수정(추가, 삽입, 수정, 삭제)
'''

# 1. 단일 리스트
lst = [1, 2, 3, 4, 5]
print(lst, type(lst), len(lst))

for i in lst:
    print(lst[i - 1:])

for i in lst:
    print(lst[:i])

'''
처음/마지막 데이터 추출
'''

x = list(range(1, 101))
print(x)
print(x[:5])

'''
index 형식
변수[start,stop:step]
'''
print(x[:])     # 전체
print(x[::2])   # 홀수 인덱스
print(x[1::2])  # 짝수 인덱스


# 2. 중첩 list : [[], []]
a = ['a','b','c']
b = [10, 20, 5, a, True, 'hong']
print(b)
print(b[3])
print(b[3][2])
print(b[3][1:])

print(type(a), type(b))
print(id(a), id(b))

# 3. 값 수정(추가, 삽입, 수정, 삭제)
num = ['one', 'two', 'three', 'four']
print(num)  # ['one', 'two', 'three', 'four']
num.append('five')
print(num)  # ['one', 'two', 'three', 'four', 'five']
num.remove('five')
print(num)  # ['one', 'two', 'three', 'four']
num.insert(0, 'zero')
print(num)  # ['zero', 'one', 'two', 'three', 'four']
num[0] = 0
print(num)  # [0, 'one', 'two', 'three', 'four']

# 4. list 연산 (+, *)

# 1) list 연산
x = [1, 2, 3, 4]
y = [1.5, 2.5]
z = x + y
print(z)

# 2) list 확장
x.extend(y)
print(x)

# 3) list 추가
x.append(y)
print(x)

# 4) list 곱셈
lst = [1, 2, 3, 4]
result = lst * 2
print(result)

# 5. list 정렬
result.sort()
print(result)
result.sort(reverse=True)
print(result)

# 6. scalar vs vector
'''
scala 변수 : 한 개의 상수(값)을 갖는 변수(크기)
vector 변수 : 다수의 값을 갖는 변수(크기, 방향)
'''
dataset = list()
size = int(input('vector size : '))
for i in range(size):
    dataset.append(i+1)
print(dataset)

# 7. list에서 원소 찾기
'''
if 값 in list:
    참 실행문
else:
    거짓 실행문
'''
if 5 in dataset:
    print('있음')
else:
    print('없음')