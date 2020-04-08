'''
set 특징
- 순서 없음 (index 사용 불가)
- 중복 허용 불가
형식) 변수 {값1, 값2, ...}
- 집합 개념
'''

s1 = {1, 3, 5, 1, 5}
print(len(s1))
for d in s1:
    print(d)

s2 = {3, 6}

# 집합 관련 함수
print(s1.union(s2))         # 합집합
print(s1.difference(s2))    # 차집합 : s1 - s2
print(s1.intersection(s2))  # 교집합

# list : gender
gender = ['남자', '여자', '남자', '여자']
# list -> set
sgneder = set(gender)
print(sgneder)
# print(sgneder[0]) index 사용 불가
# set -> list
lgender = list(sgneder)
print(lgender[0])

# 원소 추가/삭제
s3 = {1, 3, 5, 7}
print(s3, type(s3))
s3.add(9)
s3.discard(3)