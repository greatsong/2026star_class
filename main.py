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
# --- 온도(가로) vs 밝기(세로) 산점도 ---
st.subheader("온도와 밝기의 관계")
st.scatter_chart(
    df,
    x="Temperature (K)",
    y="Luminosity(L/Lo)",
    color="Star type"      # 별 종류마다 다른 색
)
# --- 색 표기 통일: 소문자 + 공백/하이픈 정리 ---
df["Star color"] = (
    df["Star color"]
    .str.strip()              # 앞뒤 공백 제거
    .str.lower()              # 전부 소문자로
    .str.replace("-", " ")   # 하이픈을 공백으로
)
st.write("정리 후:", df["Star color"].unique())
from sklearn.preprocessing import LabelEncoder

# --- 글자 색·스펙트럼을 숫자로 변환 ---
color_enc = LabelEncoder()
spec_enc  = LabelEncoder()

df["color_num"] = color_enc.fit_transform(df["Star color"])
df["spec_num"]  = spec_enc.fit_transform(df["Spectral Class"])
