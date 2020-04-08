'''
tuple 특징
- index 사용, 순서 존재
- 1차원 배열 구조
- 수정 불가, 처리 속도 빠름
- 제공 함수 없음
'''

tp = 10     # scalar
tp1 = (10)  # scalar
tp2 = (10,)  # tuple : 원소가 하나 일 경우 ,를 붙여야 튜플로 인식

# index
tp3 = (10, 58, 4, 96, 55, 2)
print(tp3[:4])

# 수정 불가
# tp3[0] = 100   TypeError: 'tuple' object does not support item assignment

# max/min
vmax = vmin = tp3[0]
for t in tp3:
    if t > vmax:
        vamx = t
    if t < vmin:
        vmin = t
print(f'최대값 : {vmax}')
print(f'최대값 : {vmin}')

# list -> tuplle
lst = list(range(10000))
print(len(lst))

tlst = tuple(lst)
print(type(tlst))