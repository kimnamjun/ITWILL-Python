'''
문제2) 서울 지역을 대상으로 '동' 이름만 추출하여 다음과 같이 출력하시오.
  단계1 : 'ooo동' 문자열 추출 : 예) '개포1동 경남아파트' -> '개포1동'
  단계2 : 중복되지 않은 전체 '동' 개수 출력 : list -> set -> list
  
  <출력 예시>  
서울시 전체 동 개수 =  797
'''
import re

try :
    with open("../data/zipcode.txt", mode='r', encoding='utf-8') as file:
        dong = set()
        zip_code = file.readlines()
        for i in zip_code:
            s = re.sub(r' \d+ $', '', re.sub(r'\s', ' ', i)).split()
            if s[1] == '서울':
                dong.add(s[3])

except Exception as e :
    print('예외발생 :', e)

finally:
    print('프로그램 종료')

dong_list = sorted(list(dong))
print(f'서울 시 전체 동의 개수 = {len(dong)}\n')
for idx, val in enumerate(dong_list):
    if idx % 10 == 9 or idx == len(dong_list) - 1:
        print(f'[{val}]')
    else:
        print(f'[{val}], ', end='')
