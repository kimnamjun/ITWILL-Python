'''
 문) 동적 멤버 변수 생성으로 다음과 같은 산포도를 구하는 클래스를 정의하시오.
 
class Scattering :         
        
        생성자 
        
        분산 함수(var_func)
        var = sum((x - mu) ** 2) / (n-1)

        표준편차 함수(std_func) 
        std = sqrt(var)
        
   << 출력 결과 >>
 분산 : 7.466666666666666
 표준편차 :  2.7325202042558927
'''

from statistics import mean
from math import sqrt


class Scattering:
    def __init__(self, data):
        self.data = data
        self.var = sum( [(x - mean(data)) ** 2 for x in data] ) / (len(data) - 1)
        self.std = sqrt(self.var)

    def var_func(self):
        return self.var

    def std_func(self):
        return self.std


x = [5, 9, 1, 7, 4, 6]

scatter1 = Scattering(x)
print(scatter1.var_func())
print(scatter1.std_func())

 
        
    
    



