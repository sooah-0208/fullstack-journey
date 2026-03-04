# import streamlit as st
# import ollama

# st.set_page_config(
#     page_title="5. 로컬 AI",
#     page_icon="💗",
#     layout="wide",
# )

# if "history" not in st.session_state:
#     st.session_state["history"] = []

# st.title("[5] 로컬 AI")

# if prompt := st.chat_input("메세지를 입력하세요"):
#     st.write(prompt)
#     st.session_state["history"].append({"role":"user", "content": prompt})
#     res = ollama.chat(model="gemma3:4b", messages=st.session_state["history"])
#     st.write(res.message.content)

import streamlit as st
import ollama

st.set_page_config(
	page_title="[5] 로컬 AI",
	page_icon="💻",
	layout="wide",
)

st.title("5. 로컬 AI")

if 'history' not in st.session_state:
	st.session_state["history"] = []

# 대화 내역 로그 보여주는 코드(없으면 input 보낼때마다 날아감)
for message in st.session_state["history"]:
     with st.chat_message(message["role"]):
          st.write(message["content"])

# 아이콘 변경하는 방법3: 내 컴퓨터에 있는 사진이나 이미지 URL로 바꾸기
# with st.chat_message("assistant", avatar="https://내사이트.com/my_icon.png"):
if prompt:=st.chat_input("채팅창"):
    # 아이콘 변경하는 방법 1: badge변경 후 뱃지랑 글자 같은 줄에 출력하기
    # col1, col2 = st.columns([0.1, 0.9])
    # with col1:
    #     st.badge(label="나", icon="🐰")
    # with col2:
    #     st.write(prompt)
    with st.chat_message("user", avatar="🐰"):
        st.write(prompt)
    st.session_state["history"].append({'role': 'user', 'content': prompt})
    # 아이콘 변경하는 방법 2: st에서 제공하는 기본 요소(assistant는 답변AI, user는 사용자 이모티콘+배경색)에서 avatar설정해주기
    with st.chat_message("assistant", avatar="👾"):
        message_placeholder = st.empty()
        full_response = ""
        res = ollama.chat(
            model='gemma3:4b',
            messages=st.session_state['history'],
            stream=True
        )
        for chunk in res:
             content = chunk["message"]["content"]
             full_response += content
             message_placeholder.markdown(full_response +"▌")
        message_placeholder.markdown(full_response)
        st.session_state["history"].append({'role': 'user', 'content': full_response})