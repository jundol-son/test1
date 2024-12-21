import streamlit as st
import requests
import pandas as pd

API_URL = "http://localhost:8000/test_db"

st.title("운용사명 기반 데이터 검색")

# 운용사명 입력
st.header("Search by 운용사명")
운용사명 = st.text_input("운용사명")

if st.button("Search"):
    response = requests.get(f"{API_URL}/{운용사명}")
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data)
        st.dataframe(df)  # 테이블 형태로 데이터 표시
    else:
        st.error("No matching entries found.")
