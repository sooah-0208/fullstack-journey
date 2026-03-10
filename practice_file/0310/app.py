import streamlit as st
import mariadb
import pandas as pd
import numpy as np

# --- DATABASE CONNECTION ---
# st.secrets를 사용하여 데이터베이스 자격 증명을 안전하게 관리하는 것을 권장합니다.
# 하지만 여기서는 사용자가 직접 입력하도록 플레이스홀더를 사용합니다.
# 아래 정보를 실제 데이터베이스 정보로 채워주세요.

conn_params = {
  "user": "root",
  "password": "1234",
  "host": "192.168.0.201",
  "database" : "db_air",
  "port" : int(3306)
}

@st.cache_data
def get_data():
    """데이터베이스에서 공항 데이터를 가져옵니다."""
    try:
        conn = mariadb.connect(**conn_params)
        cursor = conn.cursor()
        
        # ddl.sql 파일의 쿼리
        query = """
        SELECT distinct a.항공사코드, a.출발공항코드 AS 공항, air.위도, air.경도
        from db_air2.`비행` as a
        join db_air2.`항공사` as air
        ON (a.`출발공항코드` = air.항공사코드)
        ORDER BY a.항공사코드, a.`출발공항코드`;
        """
        
        cursor.execute(query)
        data = cursor.fetchall()
        
        # 데이터프레임으로 변환
        df = pd.DataFrame(data, columns=['항공사코드', '공항', '위도', '경도'])
        
        cursor.close()
        conn.close()
        
        # 위도, 경도 데이터 타입 변환 및 유효성 검사
        df['위도'] = pd.to_numeric(df['위도'], errors='coerce')
        df['경도'] = pd.to_numeric(df['경도'], errors='coerce')
        df.dropna(subset=['위도', '경도'], inplace=True)
        
        return df

    except mariadb.Error as e:
        st.error(f"데이터베이스 연결 오류: {e}")
        st.info("왼쪽 사이드바의 'DB 연결 정보'를 올바르게 입력했는지 확인하세요.")
        return pd.DataFrame() # 빈 데이터프레임 반환

# --- STREAMLIT APP ---

st.set_page_config(layout="wide")

st.title("항공사별 공항 위치 및 분포")
st.markdown("""
이 앱은 MariaDB에 저장된 비행 데이터를 사용하여 항공사별 공항의 위치를 지도에 표시하고, 관련 분포도 차트를 보여줍니다.
**DB 연결 정보를 입력해야 데이터를 볼 수 있습니다.**
""")


# 데이터 로드
df = get_data()

if not df.empty:
    st.success("데이터베이스 연결 및 데이터 로드 성공!")

    # --- 데이터 필터링 ---
    st.sidebar.header("데이터 필터")
    selected_airlines = st.sidebar.multiselect(
        "항공사 선택",
        options=df['항공사코드'].unique(),
        default=df['항공사코드'].unique()[:5] # 기본으로 5개 항공사 선택
    )

    if not selected_airlines:
        st.warning("항공사를 하나 이상 선택해주세요.")
        st.stop()
        
    filtered_df = df[df['항공사코드'].isin(selected_airlines)]

    # --- 메인 화면 ---
    
    col1, col2 = st.columns((2, 1))

    with col1:
        # 1. 지도 시각화
        st.header("공항 위치 지도")
        st.markdown(f"**{', '.join(selected_airlines)}** 항공사의 공항 위치입니다.")
        
        # 지도에 표시할 데이터프레임 (위도, 경도 이름 변경)
        map_df = filtered_df[['위도', '경도']].copy()
        map_df.rename(columns={'위도': 'lat', '경도': 'lon'}, inplace=True)
        
        st.map(map_df, zoom=1)

    with col2:
        # 2. 분포도 차트 (항공사별 취항 공항 수)
        st.header("항공사별 취항 공항 수")
        airline_counts = filtered_df['항공사코드'].value_counts().sort_index()
        st.bar_chart(airline_counts)
        st.markdown("선택된 항공사들이 각각 몇 개의 공항에 취항하는지 보여줍니다.")

    # 3. 데이터 테이블
    st.header("상세 데이터")
    st.dataframe(filtered_df)
    
else:
    st.warning("데이터를 불러오지 못했습니다. DB 연결 정보를 확인하고 다시 시도해주세요.")

st.sidebar.markdown("---")
st.sidebar.info("Made with Streamlit and Gemini")
