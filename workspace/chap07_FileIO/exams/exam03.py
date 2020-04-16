'''
문) emp.csv 파일을 읽어와서 다음 출력 예시와 같이 처리하시오. 
 
       <<출력 예시>>
관측치 길이 :  5
전체 평균 급여 : 370.0
==============================
최저 급여 : 150, 이름 : 홍길동
최고 급여 : 500, 이름 : 강감찬
==============================
'''
from statistics import mean
import pandas as pd

# 1. file read
emp = pd.read_csv('../data/emp.csv', encoding='utf-8')
print(emp)
print(f'관측치 길이 : {len(emp)}')
print(f"전체 평균 급여 : {format(mean(emp.Pay), '.1f')}")

min_pay = emp.Pay.min()
max_pay = emp.Pay.max()

print('==============================')  # emp.Pay[mini] = emp.Pay.min()
for idx, val in enumerate(emp.Pay):
    if val == min_pay:
        print(f'최저 급여 : {val}. 이름 : {emp.Name[idx]}')
    if val == max_pay:
        print(f'최고 급여 : {val}. 이름 : {emp.Name[idx]}')
print('==============================')
