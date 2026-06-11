# === 무엇을 하는 코드? — 별 데이터를 표로 보여준다 ===
import streamlit as st       # 웹 앱 도구
import pandas as pd          # 표 데이터 도구

# --- 왜? 제목이 있어야 무슨 앱인지 알 수 있다 ---
st.title("⭐ 별빛 분류기")
st.write("별의 정보로 종류를 맞히는 머신러닝 앱")

# --- CSV 파일을 읽어서 df라는 표에 담는다 ---
df = pd.read_csv("stars.csv")

# --- 표 전체를 화면에 보여준다 ---
st.subheader("데이터 미리보기")
st.dataframe(df)
