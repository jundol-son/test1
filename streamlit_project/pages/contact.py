import streamlit as st

def show_page():
    st.title("Contact Us")
    st.write("이곳은 Contact 페이지입니다.")
    email = st.text_input("Your Email", placeholder="Enter your email")
    message = st.text_area("Message", placeholder="Write your message")
    if st.button("Send"):
        st.success("Your message has been sent!")

show_page()