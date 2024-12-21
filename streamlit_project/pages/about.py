import streamlit as st

def show_page():
    st.title("About Us")
    st.write("이곳은 About 페이지입니다.")
    st.image("https://via.placeholder.com/300", caption="About 이미지")

show_page()