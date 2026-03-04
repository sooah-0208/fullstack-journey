import streamlit as st
import time
from requests import get
from bs4 import BeautifulSoup as bs
import pandas as pd
import json

st.set_page_config(
	page_title="[3] 위키백과 수집",
	page_icon="📘",
	layout="wide",
)


if 'episode_index' not in st.session_state:
	st.session_state.episode_index = 0
# episode_links = [
# 	"https://en.wikipedia.org/wiki/Demon_Slayer:_Kimetsu_no_Yaiba_season_1",
# 	"https://en.wikipedia.org/wiki/Demon_Slayer:_Kimetsu_no_Yaiba_season_2",
# 	"https://en.wikipedia.org/wiki/Demon_Slayer:_Kimetsu_no_Yaiba_season_3",
# 	"https://en.wikipedia.org/wiki/Demon_Slayer:_Kimetsu_no_Yaiba_season_4",  
# ]
episode_links = [
	"https://en.wikipedia.org/wiki/Crayon_Shin-chan_the_Movie:_Our_Dinosaur_Diary",
	"https://en.wikipedia.org/wiki/Crayon_Shin-chan_the_Movie:_Super_Hot!_The_Spicy_Kasukabe_Dancers",
	"https://en.wikipedia.org/wiki/Crayon_Shin-chan_the_Movie:_Super_Hot!_The_Spicy_Kasukabe_Dancers",
	"https://en.wikipedia.org/wiki/Crayon_Shin-chan_the_Movie:_Super_Strange!_My_Y%C5%8Dkai_Monster_Vacation",  
]

options = ["Season1","Season2","Season3","Season4"]
options = ["2023","2024","2025","2026"]

def main():
    try:
        st.text("데이터 수집을 시작합니다.")
        url = episode_links[st.session_state.episode_index]
        head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
        res = get(url, headers=head)
        if res.status_code == 200:
            episodes = []
            soup = bs(res.text)
            # table = soup.select_one("table.wikitable.plainrowheaders.wikiepisodetable")
            # rows = table.select("tr.vevent.module-episode-list-row")
            table = soup.select_one("table.infobox.vevent")
            rows = table.select("th", class_="infobox-label")
            # print(rows)
            for i, row in enumerate(rows, start=1):
                # enumerate(): start를 시작 index로 잡고 index를 붙여서 value 같이 꺼내는 함수
                synopsis = None
                # synopsis_row = row.find_next_sibling("tr", class_="expand-child")
                synopsis_row = row.find_next_sibling("td", class_="infobox-data")
                # find_next_sibling: 자식 말고 바로 아래오는 형제 찾기
                print(synopsis_row)
                if synopsis_row:
                    # synopsis_cell = synopsis_row.select_one("td.description div.shortSummaryText")
                    # synopsis_cell = synopsis_row.select_one("td.infobox-data")
                    synopsis = synopsis_row.get_text(strip=True) if synopsis_row else None
                episodes.append({
                    "season": options[st.session_state.episode_index],
                    "episode_in_season": i,
                    "synopsis": synopsis
                })
            tab1, tab2, tab3 = st.tabs(["HTML 데이터", "JSON 데이터", "DataFrame"])
            with tab1:
                st.html(table)
            with tab2:
                json_string = json.dumps(episodes, ensure_ascii=False, indent=2)
                st.download_button(
                label="JSON 다운로드",
                data=json_string,
                file_name=f"귀멸의칼날_{options[st.session_state.episode_index]}.json",
                mime="application/json"
                )
                st.json(body=json_string, expanded=True, width="stretch")
            with tab3:
                st.dataframe(
                pd.DataFrame(episodes).drop(columns=['season']), 
                width="stretch")
            st.text("데이터 수집이 완료 되었습니다.")
    except Exception as e:
        return 0
    return 1     

selected = st.selectbox(
  label="짱구는 못!말!려!💦",
  options=options,
  index=None,
  placeholder="수집 대상을 선택하세요."
)

if selected:
    st.session_state.episode_index = options.index(selected)
    if st.button(f"짱구 극장판 데이터'{options[st.session_state.episode_index]}' 수집"):
        if main() == 0:
             st.text("수집된 데이터가 없습니다.")
