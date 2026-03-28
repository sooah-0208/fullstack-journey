from bs4 import BeautifulSoup
import requests

url = "http://finance.naver.com/"
res = requests.get(url)

print(res)

soup = BeautifulSoup(res.text)
print("타이틀: ",soup.title)
# title = head 안의 타이틀. tag랑 같이 나옴
print(soup.title.text)
# text 그 안의 내용만 뽑아줌
print("Tag: ",soup.find("h1"))
# find 가장 첫번째 태그를 찾아줌
print("Tag Text: ",soup.find("h1").text.trim())
# 공백도 같이 출력됨 -> Trim 전처리 필요
# lxml은 빠른 파싱을 원할 때 사용
