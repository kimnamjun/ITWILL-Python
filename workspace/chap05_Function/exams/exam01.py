'''
문1) Start counter 문제  

height : 3 <- 키보드 입력 
*
**
***
start 개수 : 6 
'''

# 함수 정의
def StarCount(height):

    s_cnt = height * (height + 1) / 2 # 별 개수 카운트
    
    return s_cnt


# 키보드 입력 
height = int(input('height : ')) # 층 수 입력

# 함수 호출 및 start 개수 출력
print('start 개수 : %d'%StarCount(height))
