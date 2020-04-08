'''
step05 문제

문) price에는 과일 가게에 진열된 과일과 가격이 저장되어 있고, 
      buy에는 고객이 구매한 장바구니이다.
      
      list + for 형식1)을 적용하여 구매 상품 총 금액(tot_bill)을 계산하시오.      
'''

# 과일가게 진열 상품
price = {'사과': 2000, '복숭아': 3000, '딸기': 2500}

# 구매 상품
buy = {'사과': 3, '딸기': 5}

# 구매 상품 총 금액 
tot_bill = sum([price[i] * buy[i] for i in buy])
print(tot_bill)
