'''
선택자(selector)
- 웹 문서 디자인(css)에서 사용
- 선택자 : id(#), class(.)
- html.select('선택자') : 여러 개 element 수집
- html.select_one('선택자') : 한 개 element 수집
'''

from bs4 import BeautifulSoup

with open('../data/html03.html', encoding='UTF-8') as file:
    src = file.read()
    html = BeautifulSoup(src, 'html.parser')

# 태그 & 선택자 -> element 수집

# 1) id 선택자
# attr=id를 찾으면 find_all을 쓰겠지만, 그 값이 tab인 것을 찾을 때는 이거
table = html.select('#tab')  # id='tab'
print(table)  # <table> ~ </table>

# <table> <tr> [<th> or <td>]

# 계층적 접근
ths = html.select('#tab > tr > th')
print(ths)

for th in ths:
    print(th.string)

# 2) class 선택 : .
trs = html.select('#tab > .odd')
print(trs)

for tr in trs:
    tds = tr.find_all('td')
    for td in tds:
        print(td.string)

# 3) tag[속성='값'] 찾기
trs = html.select("tr[class='odd']")
# trs = html.select('#tab > .odd')  : 2)와 결과가 같음
