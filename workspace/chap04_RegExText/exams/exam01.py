'''
문1) 다음 emp '입사년도이름급여'순으로 사원의 정보가 기록된 데이터 있다.
      이 벡터 데이터를 이용하여 사원의 이름만 추출하시오. 

# <출력 결과>
 names = ['홍길동', '이순신', '유관순']
'''

from re import findall

# <Vector data>
emp = ["2014홍길동220", "2002이순신300", "2010유관순260"]

names1 = list()
for s in emp:
    names1.extend(findall('[가-힣]+', s))
print(names1)

names2 = [findall('[가-힣]+', s)[0] for s in emp]
print(names2)