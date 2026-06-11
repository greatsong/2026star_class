import plotly.express as px
import streamlit as st

유형명 = {0:"갈색왜성", 1:"적색왜성", 2:"백색왜성",
         3:"주계열성", 4:"초거성", 5:"극대거성"}
df["유형명"] = df["유형"].map(유형명)

fig = px.scatter(df, x="온도", y="절대등급", color="유형명",
                 title="온도와 밝기로 펼쳐 본 별들 (2D)",
                 labels={"온도": "표면 온도(K)", "절대등급": "절대등급(작을수록 밝음)"})
st.plotly_chart(fig)
