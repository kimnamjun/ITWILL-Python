'''
tag 속성과 내용 가져오기
- element : tag + 속성 + 내용
ex) <a href="www.naver.com">네이버</a>
a : tag
href : 속성(attribute)
네이버 : 내용(content)
'''
from bs4 import BeautifulSoup

# 1. local file 가져오기
with open('../data/html02.html', encoding='UTF-8') as file:
    src = file.read()

# 2. html 파싱
html = BeautifulSoup(src, 'html.parser')
print(html)

# 3. a 태그 엘리먼트 가져오기
links = html.find_all('a')
print(links)

# 4. a 태그 -> 속성(href(5), target(1))
urls = list()
for link in links:
    print(link.attrs)
    print(link.string)
    urls.append(link.attrs['href'])
    if link.attrs.get('target'):
        print(link.attrs.get('target'))
print(urls)

# 문) urls -> 정상 url -> new_urls
import re  # findall, match, sub

new_urls = [i for i in urls if re.match('^http[s]?://', i)]
print(new_urls)
