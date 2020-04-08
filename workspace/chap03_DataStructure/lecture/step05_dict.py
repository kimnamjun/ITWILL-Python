'''
dict 특징
- set 구조와 유사함
형식) 변수 = {key:value, ...}
- R의 list와 유사함
- key와 value 한 쌍으로 원소 구성
- key -> value 참조
- key 중복 불가, value 중복 가능
'''

# 1. dict 생성
dic1 = dict(key1=100, key2=200, key3=300)
print(dic1['key1'])

dic2 = {'name':'홍길동','age':35, 'addr':'서울시'}

# 2. 수정, 추가, 삭제, 검색 : key 이용
dic2['age'] = 45
dic2['pay'] = 350
del(dic2['addr'])
print('age' in dic2)

# 3. for 이용
for k in dic2.keys(): # dic2.key() -> dic2
    print(k, dic2[k], sep=' -> ')

for v in dic2.values():
    print(v)

for k, v in dic2.items():
    print(k, v)

# 4. key -> value
print(dic2['name'])
print(dic2.get('name'))

# 5. {key, [value]}
emp = {'hong': [250, 50], 'lee': [350, 80], 'yoo': [200, 40]}
print(emp)

for k, v in emp.items():
    print(k, v)

# 급여 250 이상인 경우 사원명, 수당 합계 출력
su = 0
for key, val in emp.items():
    if val[0] > 250:
        su += val[1]
        print(key)
print(f'수당 합계 : {su}')


# 6. 문자 빈도수 구하기
charset = ['love','test','love','hello','test','love']

# 방법1
wc = {}
for word in charset:
    if word in wc:
        wc[word] += 1
    else:
        wc[word] = 1
print(max(wc, key=wc.get))

# 방법2
wc2 = {}
for word in charset:
    wc2[word] = wc2.get(word, 0) + 1
print(wc2)

word_list = [[i] for i in wc]
print(word_list)