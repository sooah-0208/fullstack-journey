from bs4 import BeautifulSoup
import requests

url = 'http://127.0.0.1:5500/practice_file/0303/index.html'
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")
# "html.parser": 어떤 해석기로 분석할 것인가 => 파이썬에 기본 내장되어있음, 속도 보통(lxml같은 거)

lis = soup.find_all("li")
# print(lis)

for li in lis:
    print(li.find("a").text)
# 여기서 find_all이 아니라 find해도 되는 이유는 <li>안에 <a>가 어차피 하나 뿐이기 때문임! 여러개 나오면 find_all


















# for li in lis:
#     print(li.find("a").text)