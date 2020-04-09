'''
정규 표현식

[주요 메타문자]
. : 임의의 한 문자
.x : 임의의 한 문자 뒤에 x가 오는 문자열(ex : abc, mbc -> .bc)
^x : x로 시작하는 문자열(접두어 추출)
x$ : x로 끝나는 문자열(접미어 추출)
x. : x 다음에 임의의 한 문자가 오는 문자열(ex : t1, t2, ta -> t.)
x* : x가 0번 이상 반복
x+ : x가 1개 이상 반복
x? : x가 0 또는 1개 존재
x{m, n} : x가 m~n 사이 연속
x{m, } : x가 m 이상 연속
x{,n} : x가 n 이하 연속
[x] : x문자 한 개 일치
'''

import re                           # 방법1) 정규표현식 모듈
from re import findall, match, sub  # 방법2) from 모듈 import 함수

'''
re.findall()  # 방법1)
findall()     # 방법2)
'''

# 1. findall
# findall(pattern='메타문자 패턴', string='문자열')

str1 = '1234 abc홍길동 ABC_555_6 이사도시'

print(re.findall(pattern='1234', string=str1))
print(findall(pattern='[0-9]{3}', string=str1))
print(findall(pattern='[0-9]{3,}', string=str1))
print(findall(pattern=r'\d{3,}', string=str1))  # r'\d' = '\\d'

# 1-1. 문자열 처리
print(findall('[가-힣]{3,}', str1))
print(findall('[a-z|A-Z]{3,}', str1))

str_list = str1.split(sep=' ')
print(str_list)

names = list()
for s in str_list:
    temp = findall('[가-힣]{3,}', s)
    print(temp)

    if temp:
        names.append(temp[0])
print(names)

# 1-2. 접두어/접미어 문자열 찾기
str2 = 'test1abcABC 123mbc 45test'
print(findall('^test', str2))
print(findall('st$', str2))

# 1-3. 종료 문자 찾기
print(findall('.bc', str2))
print(findall('t.', str2))

# 1-4. 단어 찾기(\\w) : 한글, 영문자, 숫자
str3 = 'test^홍길동 abc 대한*민국 123$tbc'
words = findall(r'\w{3,}', str3)
print(words)

# 1-5. 특정 문자열 제외
print(findall('[^t]+', str3))
print(findall(r'[^^*$]+', str3))
# 패턴 맨 앞의 ^는 시작 문자열
# 대괄호 맨 앞에 나오는 ^는 제외 기호
# 그 외에는 문자 ^

# 2. match
# match(pattern='패턴', string='문자열')
# - 패턴 일치 여부 반환(object 반환)

jumin = '123456-1234567'
result = match('[0-9]{6}-[1-4][0-9]{6}', jumin)
if result:
    print('정상 주민번호')
else:
    print('비정상 주민번호')

# 3. sub
# sub('pattern','rep','string')
result = sub(r'[\^*$]', '', str3)
print(result)
