import streamlit as st
import openai

st.title("GPT-4.1-mini 챗봇 웹앱")

# API 키 입력란으로 세션 상태에 저장
if "api_key" not in st.session_state:
    st.session_state.api_key = ""

api_key_input = st.text_input("OpenAI API Key를 입력하세요:", type="password", value=st.session_state.api_key)

# 업데이트 세션 상태
if api_key_input != st.session_state.api_key:
    st.session_state.api_key = api_key_input

question = st.text_input("질문을 입력하세요:")

if st.button("질문하기"):
    if not st.session_state.api_key:
        st.warning("API Key를 입력해주세요.")
    elif not question:
        st.warning("질문을 입력해주세요.")
    else:
        try:
            openai.api_key = st.session_state.api_key
            response = openai.ChatCompletion.create(
                model="gpt-4.1-mini",
                messages=[{"role": "user", "content": question}]
            )
            answer = response.choices[0].message.content
            st.success("응답:")
            st.write(answer)
        except Exception as e:
            st.error(f"에러 발생: {e}")
