'''
사용자 정의 함수 응용
'''

# 1. 텍스트 전처리 용도 함수
def clean_text(texts):
    from re import sub
    return ' '.join(sub(r'[\d.,;:?!@#$%^&*()]+', '', texts).lower().split())


texts = [' 우리나라    대한민국, 우리나라%$ 만세', '비아그&라 500GRAM 정력 최고!', '나는 대한민국 사람', '보험료 15000원에 평생 보장 마감 임박', '나는 홍길동']

print('텍스트 전처리 전')
print(texts)
print(len(texts))

result = [clean_text(text) for text in texts]

print('텍스트 전처리 후')
print(result)
print(len(result))

# 2. 표본의 분산과 표준편차
from statistics import mean, variance, stdev # 통계 함수
from math import sqrt # 수학 함수
dataset = [2, 4, 5, 6, 1, 8]

print(mean(dataset))
print(variance(dataset))
print(stdev(dataset))

'''
분산 = sum( (x 변량 - 평균) **2 ) / (n-1)
표준편차 = sqrt(분산)
'''

avg = mean(dataset)
def var_std(dataset):
    avg = mean(dataset)
    diff = [(x - avg) ** 2 for x in dataset]
    diff_sum = sum(diff)
    var = diff_sum / (len(dataset) - 1)
    std = sqrt(var)
    return var, std

# 함수 호출
var, std = var_std(dataset)
print(f'    분산 = {var}\n표준편차 = {std}')

a, b = 15, 15
print(id(a), id(b))
a = a ^ b
b = a ^ b
a = a ^ b
print(a)
print(b)