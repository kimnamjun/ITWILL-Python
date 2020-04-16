'''
우편번호 검색
135-806	서울	강남구	개포1동 경남아파트		1
135-807	서울	강남구	개포1동 우성3차아파트	(1∼6동)	2
'''
import re

try:
    dong = input('동을 입력하세요 : ')
    with open('../data/zipcode.txt', mode='r', encoding='UTF-8') as file:
        line = file.readline()
        while line:
            addr = line.split('\t')
            if addr[3].startswith(dong):
                print(f'[{addr[0]}] {addr[1]} {addr[2]} {addr[3]} {addr[4]}')
            line = file.readline()

except Exception as e:
    print(f'예외 발생 : {e}')

finally:
    print('~~ 프로그램 종료 ~~')