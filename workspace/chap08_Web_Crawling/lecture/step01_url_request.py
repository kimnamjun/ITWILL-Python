'''
원격 서버의 웹 수집
'''
from bs4 import BeautifulSoup     # source -> html
import urllib.request as req  # 원격 서버 파일 요청

url = 'https://www.naver.com'

# 1. 원격 서버 url 요청
request = req.urlopen(url)  # 요청 -> 응답
print(request)  # object info
data = request.read()
print(data) # !<doctype html> -> source


# 2. source(문자열) -> html 형식 : html parsing
src = data.decode('UTF-8')
html = BeautifulSoup(src, 'html.parser')  # source -> html
print(html)


# 3. Tag 내용 가져오기
link = html.find('a')
print(link)
'''
element : <시작태그 속성명='값'> 내용 </종료태그>
'''
print(link.string)

link_all = html.find_all('a')
print(link_all)