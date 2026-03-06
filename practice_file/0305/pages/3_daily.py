from bs4 import BeautifulSoup as bs
from requests import get
import pandas as pd
import streamlit as st
import json


st.set_page_config(
  page_title="daily Rank 수집",
  page_icon="💗",
  layout="wide",
)

url = "https://mapi.ticketlink.co.kr/mapi/ranking/genre/daily?categoryId=10&categoryId2=16&categoryId3=0&menu=RANKING"

def getData():
    res = get(url)
    data = res.json()
    try:
        if res.status_code == 200:
            st.text("daily Rank 수집 시작!")
            # json_data = json.load(res.text)
            tab1, tab2 = st.tabs(["JSON 데이터", "DataFrame"])
            with tab1:
                st.text("JSON 출력")
                json_string = json.dumps(data, ensure_ascii=False, indent=2)
                st.json(body=json_string, expanded=True, width="stretch")
                st.html("<hr/>")
                st.text("랭킹 목록 출력")
                st.json(data.get("data",{}).get("rankingList",{}), expanded=False, width="stretch")
            with tab2:
                st.text("DataFrame 출력")
                st.dataframe(pd.DataFrame(data))
    except Exception as e:
        return 0
    return 1 

if st.button(f"수집하기"):
  getData()