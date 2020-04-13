class Account:
    def __init__(self, balance=0, name='', no=''):
        self.balance = balance
        self.accName = name
        self.accNo = no

    def get_balance(self):
        return self.accNo, self.accName,  self.balance

    def deposit(self, money):
        self.balance += money

    def withdraw(self, money):
        if self.balance >= money:
            self.balance -= money
        else:
            print('잔액이 부족합니다.')


acc = Account(1000)
print(f'잔액 : {acc.get_balance()[2]}')
acc.deposit(20000)
print(f'잔액 : {acc.get_balance()[2]}')
acc.withdraw(5000)
print(f'잔액 : {acc.get_balance()[2]}')

'''
1. 예금주(accName), 계좌번호(accNo) 동적 멤버 변수 추가하기
    -> 예금주 : 홍길동, 계좌번호 : 012-125-41520
2. getBalance() 메소드를 이용하여 잔액, 예금주, 계좌번호 출력하기
'''

acc2 = Account(1000, '홍길동', '012-125-41520')
print(f'{acc2.get_balance()[1]} 님의 잔액은 {acc2.get_balance()[2]}원 입니다.')