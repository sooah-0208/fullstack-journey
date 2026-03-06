from bs4 import BeautifulSoup as bs
from requests import get
import pandas as pd
import streamlit as st
import json

st.set_page_config(
  page_title="interpark 수집",
  page_icon="💗",
  layout="wide",
)

# 인터파크 장르별 URL

urls = [
"https://tickets.interpark.com/contents/ranking?genre=MUSICAL",
"https://tickets.interpark.com/contents/ranking?genre=CONCERT",
"https://tickets.interpark.com/contents/ranking?genre=SPORTS",
"https://tickets.interpark.com/contents/ranking?genre=EXHIBIT"
"https://tickets.interpark.com/contents/ranking?genre=CLASSIC",
"https://tickets.interpark.com/contents/ranking?genre=KIDS",
"https://tickets.interpark.com/contents/ranking?genre=DRAMA",
"https://tickets.interpark.com/contents/ranking?genre=LEISURE"
]


# 데이터 수집
def getData():
  try:
    url = "https://tickets.interpark.com/contents/ranking?genre=MUSICAL"
    st.text(f"URL: {url}")
    res = get(url)
    if res.status_code == 200:
      st.text("인터파크 티켓 수집 시작!")
      soup = bs(res.text, "html.parser")
      tickets = [] # { 장르, 티켓이름, 장소, 시작날짜, 종료날짜, 예매율 }
      items = soup.select("div.responsive-ranking-list_rankingItem__PuQPJ")
      genre = "MUSICAL"
      for item in items:
        tName = item.select_one("li.responsive-ranking-list_goodsName__aHHGY").get_text(strip=True)
        pName = item.select_one("li.responsive-ranking-list_placeName__9HN2O").get_text(strip=True)
        tDate = item.select_one("div.responsive-ranking-list_dateWrap__jBu5n").get_text(strip=True)
        tPercent = item.select_one("li.responsive-ranking-list_bookingPercent__7ppKT").get_text(strip=True)
        tickets.append({ "genre": genre, "tName": tName, "pName": pName, "tDate": tDate, "tPercent": tPercent })
      tab1, tab2, tab3 = st.tabs(["HTML 데이터", "JSON 데이터", "DataFrame"])
      with tab1:
        st.text("html 출력")
        st.text(items)
      with tab2:
        st.text("JSON 출력")
        json_string = json.dumps(tickets, ensure_ascii=False, indent=2)
        st.json(body=json_string, expanded=True, width="stretch")
      with tab3:
        st.text("DataFrame 출력")
        st.dataframe(
          pd.DataFrame(tickets).drop(columns=['tName']), 
          width="stretch")
  except Exception as e:
    return 0
  return 1

if st.button(f"수집하기"):
  getData()
