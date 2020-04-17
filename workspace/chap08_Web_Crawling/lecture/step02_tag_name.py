'''
tag명으로 찾기
형식) html.find('tag') : 최초로 발견된 tag 수집
html.find_all('tag')   : 해당 tag 전체 수집
'''
from bs4 import BeautifulSoup

# 1. local file 불러오기
with open('../data/html01.html', encoding='UTF-8') as file:
    src = file.read()
    print(src)

# 2. src -> html parsing
html = BeautifulSoup(src, 'html.parser')
print(html)

# 3. tag 찾기 -> 내용 추출

# 1) tag
h1 = html.html.body.h1
print(h1)  # element : <h1> 시멘틱 태그 ?</h1>
print(h1.string)  # 내용 :  시멘틱 태그 ?

# 2) find
h2 = html.find('h2')
print(h2)
print(h2.string)

# 3) find_all('tag') : list
li = html.find_all('li')
# print(li)

for l in li:
    print(l.string)

li_cont = [l.string for l in li]
print(li_cont)
