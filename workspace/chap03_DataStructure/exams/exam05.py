'''
step04, 05 문제 

 문1) 중복 되지 않은 직위 출력 하시오.
 문2) 각 직위별 빈도수를 출력하시오.
 
 <<출력 결과 >>
 중복되지 않은 직위 : ['사장', '과장', '대리', '부장'] : list -> set -> list
 각 직위별 빈도수 : {'과장': 2, '부장': 1, '대리': 2, '사장': 1} -> dict  
'''

position = ['과장', '부장', '대리', '사장', '대리', '과장']

position_set = set(position)
position_list = list(position_set)
print(f'중복되지 않은 직위 : {position_list}')

position_count = dict()
for i in position:
    position_count[i] = position_count.get(i, 0) + 1
print(f'각 직위별 빈도수 : {position_count}')
