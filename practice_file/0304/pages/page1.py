import streamlit as st
import time
from bs4 import BeautifulSoup as bs
from requests import get
import json
import pandas as pd
from db import saveMany


if 'link_index' not in st.session_state:
	st.session_state.link_index = 0
# 함수끼리 정보를 주고받기 위한 설정
# session_state로 전역변수 처리
# .link_index가 변수

st.markdown("<h1 style='text-align: center;'>수집 목록</h1>", unsafe_allow_html=True)
# `st.title`로는 stlye을 줄 수 없어서 커스텀용으로 markdown사용

links = [
  "https://www.melon.com/genre/song_list.htm?gnrCode=GN0100&orderBy=POP",
  "https://www.melon.com/genre/song_list.htm?gnrCode=GN0200&orderBy=POP",
  "https://www.melon.com/genre/song_list.htm?gnrCode=GN0300&orderBy=POP",
  "https://www.melon.com/genre/song_list.htm?gnrCode=GN0400&orderBy=POP",
  "https://www.melon.com/genre/song_list.htm?gnrCode=GN0500&orderBy=POP",
  "https://www.melon.com/genre/song_list.htm?gnrCode=GN0600&orderBy=POP",
  "https://www.melon.com/genre/song_list.htm?gnrCode=GN0700&orderBy=POP",
  "https://www.melon.com/genre/song_list.htm?gnrCode=GN0800&orderBy=POP",
]
options = ("발라드","댄스","랩/힙합","R&B/Soul","인디음악","록/메탈","트로트","포크/블루스")
# html select태그에 option이 필수임. 얘네가 옵션 value

def getData(data):
  arr = []
  trs = data.select("#frm tbody > tr")
  if trs:
    for i in range(len(trs)):
      id = int(trs[i].select("td")[0].select_one("input[type='checkbox']").get("value"))
      img = cleanData(trs[i].select("td")[2].select_one("img")["src"])
      title = cleanData(trs[i].select("td")[4].select_one("div[class='ellipsis rank01']").text).replace("'",'"')
      album = cleanData(trs[i].select("td")[5].select_one("div[class='ellipsis rank03']").text).replace("'",'"')
      arr.append( {"id": id, "img": img, "title": title, "album": album, "cnt": 0} )
  return arr

def cleanData(txt):
  list = ["\n", "\xa0", "\r", "\t", "총건수"]
  for target in list:
    txt = txt.replace(target, "")
  return txt.strip()

# 좋아요 수 집계용(비동기라 한번에 안 읽어짐) url 함수
def getLikes(list, head=None):
  ids = ""
  for i in range(len(list)):
    if i == 0:
      ids += f"{list[i]["id"]}"
    else:
      ids += f",{list[i]["id"]}"
  if ids:
    url = f"https://www.melon.com/commonlike/getSongLike.json?contsIds={ids}"
    res = get(url, headers=head)
    if res.status_code == 200:
      data = json.loads(res.text)
      for row in data["contsLike"]:
        for i in range(len(list)):
          if list[i]["id"] == row["CONTSID"]:
            list[i]["cnt"] = row["SUMMCNT"]
            break
  return list

def main():
  try:
    st.text("데이터 수집을 시작 합니다.")
    head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'}
    url = links[st.session_state.link_index]
    st.text(url)
    res = get(url, headers=head)
    if res.status_code == 200:
    #    st.text(res.text.replace("\n","").replace("\t","").strip())
        # st.html(res.text) - 데이터 확인용 html그대로 가져와줌
        data = bs(res.text)
        arr = getData(data)
        arr = getLikes(arr, head)
        # arr에 cnt(좋아요 수) 채워주는 작업 전처리
        df = pd.DataFrame(arr)
        # pandas역할 DataFrame 자체가 데이터 가공해서 표형태의 객체로 변환해줌
        st.dataframe(df.head(10))
        # 받은 데이터 스트림릿(보여주기)
        genre = url.replace("https://www.melon.com/genre/song_list.htm?gnrCode=","").replace("&orderBy=POP","")
        print(genre)
        sql2 = f"""
          INSERT INTO edu.`melon` 
          (`id`, `img`, `title`, `album`, `cnt`, `genre`)
          VALUE
          (%s, %s, %s, %s, %s, %s)
          ON DUPLICATE KEY UPDATE
            id=VALUES(id),
            img=VALUES(img),
            title=VALUES(title),
            album=VALUES(album),
            cnt=VALUES(cnt),
            genre=VALUES(genre)
            """
        values = [(row["id"], row["img"], row["title"], row["album"], row["cnt"], genre) for row in arr]
        # print("값:", values[0])
        saveMany(sql2, values)

    st.text("데이터 수집이 완료 되었습니다.")
  except Exception as e:
    return 0
  return 1

selected = st.selectbox(
  label="음원 장르를 선택하세요",
  options=options,
  index=None,
  # 이거 없으면 1번 옵션이 미리 선택되어져 보임, placeholder 필요 없음
  placeholder="수집 대상을 선택하세요."
)
# selected에 st.selectbox가 보내준 return값들이 들어있음 => value + index
# 이 인덱스 값으로 T/F처리하는 if문
if selected:
  st.write("선택한 장르 :", selected)
  st.session_state.link_index = options.index(selected)
  if st.button(f"'{options[st.session_state.link_index]}' 수집"):
  # 이 if문은 button이 눌리면 True, 아님 False
    if main() == 0:
      st.text("수집된 데이터가 없습니다.")