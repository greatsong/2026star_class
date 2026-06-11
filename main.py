import pandas as pd

df = pd.read_csv('stars.csv')
df.columns = ["온도", "광도", "반지름", "절대등급", "유형", "색", "분광형"]

print(df.shape)
print(df["유형"].value_counts().sort_index())

import plotly.express as px
import streamlit as st

유형명 = {0:"갈색왜성", 1:"적색왜성", 2:"백색왜성",
         3:"주계열성", 4:"초거성", 5:"극대거성"}
df["유형명"] = df["유형"].map(유형명)

fig = px.scatter(df, x="온도", y="절대등급", color="유형명",
                 title="온도와 밝기로 펼쳐 본 별들 (2D)",
                 labels={"온도": "표면 온도(K)", "절대등급": "절대등급(작을수록 밝음)"})
st.plotly_chart(fig)


import numpy as np
df["log반지름"] = np.log10(df["반지름"])

fig = px.scatter_3d(df, x="온도", y="절대등급", z="log반지름",
                    color="유형명",
                    title="별 6종을 3D로 펼쳐 보기",
                    labels={"온도": "표면 온도(K)",
                            "절대등급": "절대등급(작을수록 밝음)",
                            "log반지름": "반지름(log10)"})
fig.update_traces(marker=dict(size=2))
st.plotly_chart(fig)
