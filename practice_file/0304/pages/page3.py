import streamlit as st
import numpy as np
import pandas as pd

st.set_page_config(
	page_title="[2] 암환자수 통계",
	page_icon="🤒",
	layout="wide",
)

if 'slider_value' not in st.session_state:
	st.session_state.slider_value = (2017,2022)
# if 'data_view' not in st.session_state:
# 	st.session_state.data_view = False

url = "https://www.index.go.kr/unity/potal/eNara/sub/showStblGams3.do?stts_cd=277002&idx_cd=2770&freq=Y&period=N"

st.title("2. 암환자수 통계")
col1, col2, col3 = st.tabs(["1. 원본", "2. [Unnamed: 1] 삭제", "3. [Unnamed: 0] 변경"])
df = pd.read_html(url)[0].drop(0)
data1 = df.drop("Unnamed: 1", axis = 1)
data2 = data1.iloc[::2,:].set_index(keys="Unnamed: 0")
with col1:
	st.dataframe(df)
with col2:
	st.dataframe(data1)
with col3:
	st.dataframe(data2)

def makeCol(data1):
	point = []
	target = st.session_state.slider_value
	for i in range(target[0], target[1]+1):
		point.append(str(i))
	if len(point) == 0:
		point = list(data1.columns)
	return point

sl = st.slider(
	label="년도 범위를 변경하세요",
	min_value=1989,
	max_value=2023,
	value=st.session_state.slider_value,
	step=1
	# step은 정수 이동하게 해줌(1이면 1단위, 5면 5단위 // 지금은 년도라 1년, 5년으로 이동되게 해줌)
)

# slider 움직일 때 마다 로딩되지 않도록 버튼 생성

if st.button("선택한 범위"):
	st.session_state.slider_value = sl
	data3 = data2.filter(items=makeCol(data2)).transpose()
	#.transpose(): pivot시키는 함수(행 열 뒤집기)
	tab3, tab4 = st.tabs(["데이터", "차트"])
	with tab3:
		st.dataframe(data3, use_container_width = True)
	with tab4:
		st.line_chart(data3)