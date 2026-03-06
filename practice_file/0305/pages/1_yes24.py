from bs4 import BeautifulSoup as bs
from requests import get
import pandas as pd
import streamlit as st
import json

st.set_page_config(
  page_title="yes24 수집",
  page_icon="💗",
  layout="wide",
)

# Yes24 베스트셀러 URL 예시
yes24 = "https://www.yes24.com/product/category/weekbestseller"
categoryNumber = "001"
pageNumber = 1
pageSize = 40
type = "week"
saleYear = 2026
weekNo = 1149
sex = "A"
viewMode = "thumb"

url = (
  f"{yes24}?"
  f"categoryNumber={categoryNumber}&"
  f"pageNumber={pageNumber}&"
  f"pageSize={pageSize}&"
  f"type={type}&"
  f"saleYear={saleYear}&"
  f"weekNo={weekNo}&"
  f"sex={sex}&"
  f"viewMode={viewMode}"
)

# 데이터 수집
def getData():
  try:
    url = "https://www.yes24.com/product/category/weekbestseller?categoryNumber=001&pageNumber=1&pageSize=24&type=week"
    st.text(f"URL: {url}")
    res = get(url)
    if res.status_code == 200:
      books = [] # { 도서명, 저자, 별점 }
      soup = bs(res.text)
      trs = soup.select("#yesBestList .itemUnit")
      st.text("yes24 국내도서 주별 베스트 수집 시작!")
      for row in trs:
        도서명 = row.find("div", class_="item_info").find("a", class_="gd_name").get_text(strip=True)
        저자 = row.find("span", class_="authPub info_auth").get_text(strip=True)
        별점 = row.find("em", class_="yes_b").get_text(strip=True)
        books.append({
          "도서명": 도서명,
          "저자": 저자,
          "별점": 별점
        })
      # print(books)
      tab1, tab2, tab3 = st.tabs(["HTML 데이터", "JSON 데이터", "DataFrame"])
      with tab1:
        st.html(trs)
      with tab2:
                json_string = json.dumps(books, ensure_ascii=False, indent=2)
                st.download_button(
                label="JSON 다운로드",
                data=json_string,
                file_name="yes24.json",
                mime="application/json"
                )
                st.json(body=json_string, expanded=True, width="stretch")
      with tab3:
        st.dataframe(
                pd.DataFrame(books).drop(columns=['도서명']), 
                width="stretch")
  except Exception as e:
    return 0
  return 1

if st.button(f"수집하기"):
  getData()
  if getData() == 0:
    st.text("수집된 데이터가 없습니다.")