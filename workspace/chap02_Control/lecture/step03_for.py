# 반복문 for

# 열거형 객체 (iterable) : string, list, tuple, set, dict
# 제너레이터 식 : 변수 in 열거형 객체 (원소 순회 -> 변수 넘김)


# 1. string 열거형 객체
string = "나는 빡빡이 입니다."

for s in string:
    print(s, end=' ')
print()

for s in string.split():
    print(s)

# 2. list 열거형 객체 이용
lst = [1,2,3,4,5]
print(lst)
print(type(lst))

lst2 = list()
for i in lst:
    print(i, end=' ')
    lst2.append(i ** 2)
print(lst2)

# 1~100 원소를 갖는 list 객체 생성
lst3 = list(range(1, 101, 1))
print(lst3)

# 3. range 열거형 객체 이용
'''
range(n) : 0 ~ n-1 정수
range(start, stop) : start ~ stop-1 정수
range(start, stop, step) : start ~ stop-1, step 정수
'''

num1 = range(10)
num2 = range(1, 10)
num3 = range(1, 10, 2)
print(num1)
print(num2)
print(num3)

for i in num1:
    print(i, end=' ')
print()
for i in num2:
    print(i, end=' ')
print()
for i in num3:
    print(i, end=' ')

# 4. list + range 열거형 객체 이용
idx = list(range(5))
print(idx)

# 문) lst1에 1~100 100개의 원소를 갖는 vector를 생성하고,
#     lst2에 3의 배수만 append
lst1 = list(range(1,101))
lst2 = list()
for i in lst1:
    if i % 3 == 0:
        lst2.append(i)

# index 이용 : 분류 정확도
y_true = [1,0,2,1,0] # 관측치 : 범주형 (0,1,2)
y_pred = [1,0,2,0,0] # 예측치

size = len(y_true)
acc = 0

for i in range(size):
    fit = int(y_true[i] == y_pred[i])
    acc += fit * 20
print(f'분류정확도 = {acc}')

# 5. 이중 for문
# 1) 구구단
for i in range(2, 10):
    print(f'*** {i}단 ***')
    for j in range(1, 10):
        print(f'{i} * {j} = {i * j}')
    print()

# 2) 문자열 처리
para = """나는 빡빡이 입니다.
주소는 서창동입니다.
나이는 26세입니다."""

sents = list()
words = list()
for sent in para.split('\n'):
    sents.append(sent)
    for word in sent.split():
        words.append(word)

print(sents)
print(f'문장 길이 : {len(sents)}')
print(f'단어 길이 : {len(words)}')

# 제너레이터 식 : 변수 in 열거형 객체
'''
for 변수 in 열거형 객체:
    -> 객체의 원소 수 만큼 반복
if 값 in 열거형 객체:
    -> 객체의 원소 중에서 값이 있으면 True, 없으면 False
'''
search = input('검색 단어 입력 : ')
if search in words:
    print('해당 단어 있음')
else:
    print('해당 단어 없음')
