from bs4 import BeautifulSoup
import requests

url = 'https://news.naver.com/'
response = requests.get(url)
# print(response)
soup = BeautifulSoup(response.text, 'lxml')

# print(soup)
# 모든 뉴스 제목 가져오기
titles = soup.select('a[href*="025"]')
# `*=:` 포함하는 모든 것 (=Like)
# 내가 원하는 정보 찾아오기 위해 사이트(F12)통해 class나 태그명으로 찾아옴

# print(titles)

for t in titles[7:10]:
    print(t.get_text(strip=True))