# app.py
import streamlit as st
import openai

st.title("GPT-4.1-mini 챗봇 웹앱")

# 1. OpenAI API Key 입력받기 (비밀번호 형태)
api_key = st.text_input("OpenAI API Key를 입력하세요:", type="password")

# 2. 질문 입력 받기
question = st.text_input("질문을 입력하세요:")

# 3. 버튼 클릭 시 응답 출력
if st.button("질문하기"):
if not api_key:
st.warning("API Key를 입력해주세요.")
elif not question:
st.warning("질문을 입력해주세요.")
else:
try:
openai.api_key = api_key

response = openai.ChatCompletion.create(
model="gpt-4.1-mini", 
messages=[
{"role": "user", "content": question}
]
)

answer = response.choices[0].message.content
st.success("응답:")
st.write(answer)

except Exception as e:
st.error(f"에러 발생: {e}")
