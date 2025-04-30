export OPENAI_API_KEY="your_api_key_here"
import streamlit as st
import openai
import os

st.title("GPT-4.1-mini 챗봇 웹앱")

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    st.error("서버 환경변수에 OPENAI_API_KEY가 설정되어 있지 않습니다.")

question = st.text_input("질문을 입력하세요:")

if st.button("질문하기"):
    if not question:
        st.warning("질문을 입력해주세요.")
    else:
        try:
            openai.api_key = api_key
            response = openai.ChatCompletion.create(
                model="gpt-4.1-mini",
                messages=[{"role": "user", "content": question}]
            )
            answer = response.choices[0].message.content
            st.success("응답:")
            st.write(answer)
        except Exception as e:
            st.error(f"에러 발생: {e}")
