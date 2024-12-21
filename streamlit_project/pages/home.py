import streamlit as st
from utils import fetch_data_by_operator, fetch_all_data

# 검색 실행 함수
def search_operator():
    operator_name = st.session_state.operator_name  # 입력된 운용사명 가져오기
    
    if operator_name.strip():  # 검색어가 있는 경우
        try:
            # 운용사명에 맞는 데이터 조회
            data = fetch_data_by_operator(operator_name)
            if not data.empty:
                st.session_state.search_results = data  # 세션에 저장
            else:
                st.session_state.search_results = None
        except Exception as e:
            st.session_state.search_results = None
            st.error(f"데이터를 조회하는 중 오류가 발생했습니다: {e}")
    else:  # 검색어가 비어 있는 경우
        st.warning("운용사명을 입력하세요.")
        try:
            # 전체 데이터 조회
            data = fetch_all_data(limit=100)  # LIMIT 100
            if not data.empty:
                st.session_state.search_results = data  # 전체 데이터 세션에 저장
            else:
                st.session_state.search_results = None
        except Exception as e:
            st.error(f"전체 데이터를 조회하는 중 오류가 발생했습니다: {e}")

def show_page():
    st.title("운용사명 검색")
    st.write("이곳은 운용사명 검색 페이지입니다.")

    # 검색창과 버튼을 세로로 배치
    st.write("### 운용사명 검색")

    # 검색창
    operator_name = st.text_input("운용사명을 입력하세요:", placeholder="운용사명을 입력", key="operator_name", on_change=search_operator)

    # 검색 버튼
    search_button = st.button("검색", on_click=search_operator)

    # 검색 결과를 화면 맨 아래로 배치
    if 'search_results' in st.session_state:
        # 검색 결과가 없으면 '검색 결과가 없습니다'를 맨 아래에 출력
        if st.session_state.search_results is None:
            st.write("검색 결과가 없습니다.")
        else:
            # 검색 결과가 있으면 데이터 출력
            st.write("검색 결과:")
            st.dataframe(st.session_state.search_results)  # 검색된 데이터 맨 아래에 배치

show_page()
