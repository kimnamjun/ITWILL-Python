'''
 문) login.html 웹 문서를 대상으로 다음 조건에 맞게 내용을 추출하시오. 
    조건1> id="login_wrap" 선택자의  하위 태그  전체 출력 
    조건2> id="login_warp" 선택자  > form > table 태그 내용 출력 
    조건3> find_all('tr') 함수 이용  th 태그 내용 출력  
'''

from bs4 import BeautifulSoup

# 1. html source 가져오기 

# 2. html 파싱

# 3. 선택자 이용 태그 내용 가져오기 

with open('../data/login.html', encoding='UTF-8') as file:
    src = file.read()
    html = BeautifulSoup(src, 'html.parser')

# 1. html source 가져오기
for i in html.select('#login_wrap'):
    print(i, end = '\n' + '-' * 50 + '\n')

# 2. html 파싱
for tab in  html.select('#login_wrap > form > table'):
    print(tab, end = '\n' + '-' * 50 + '\n')

# 3. 선택자 이용 태그 내용 가져오기
for tr in html.find_all('tr'):
    for th in tr.find_all('th'):
        print(th.string)
