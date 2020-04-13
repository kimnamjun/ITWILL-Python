'''
 <급여 계산 문제>
문) Employee 클래스를 상속하여 Permanent와 Temporary 클래스를 구현하시오.
    <조건> pay_pro 함수 재정의     
'''

# 부모클래스 
class Employee : 
    name = None
    pay = 0
    
    def __init__(self,name):
        self.name = name
    
    # 원형 함수 : 급여 계산 함수     
    def pay_pro(self):
        pass

# 자식클래스 - 정규직 
class Permanent(Employee):
    
    # 함수 재정의 : 인수+내용 추가      
    def pay_pro(self):
        pass
   
# 자식클래스 - 임시직 
class Temporary(Employee):
    
    # 함수 재정의 : 인수+내용 추가      
    def pay_pro(self):
        pass
    
    
    
    
    
    
