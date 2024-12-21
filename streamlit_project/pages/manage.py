import streamlit as st
from utils import fetch_data_by_operator, fetch_all_data, add_data_to_db, update_data_in_db, delete_data_from_db

# 데이터 관리 페이지
def show_page():
    st.title("데이터 관리")

    # 처음 페이지 로드 시 데이터 로드
    if 'data' not in st.session_state:
        data = fetch_all_data(limit=100)  # LIMIT 100
        if not data.empty:
            st.session_state.data = data  # 세션에 데이터 저장
        else:
            st.warning("전체 데이터가 없습니다.")

    # 전체 데이터 표시
    st.write("### 전체 데이터")
    if 'data' in st.session_state:
        st.dataframe(st.session_state.data)  # 테이블 출력

    # 새로고침 버튼
    if st.button("전체 데이터 새로고침"):
        data = fetch_all_data(limit=100)  # LIMIT 100
        if not data.empty:
            st.session_state.data = data  # 새로 로드된 데이터 세션에 저장
        else:
            st.warning("전체 데이터가 없습니다.")

    # 데이터 관리 기능 (세로 탭을 가로로 변경)
    tab = st.radio("데이터 관리 기능을 선택하세요:", ['데이터 추가', '데이터 수정', '데이터 삭제'], horizontal=True)

    # 데이터 관리 작업을 라디오 버튼에 따라 처리
    if tab == '데이터 추가':
        st.write("### 새로운 데이터 추가")
        tickers = st.text_input("티커 입력:")
        operator_name = st.text_input("운용사명 입력:")
        price = st.number_input("가격 입력:", min_value=0.0, step=0.01)

        if st.button("데이터 추가"):
            if tickers and operator_name and price:
                success, message = add_data_to_db(tickers, operator_name, price)
                if success:
                    st.success(message)
                    # 데이터 추가 후 세션에 새로운 데이터 갱신
                    data = fetch_all_data(limit=100)
                    st.session_state.data = data
                else:
                    st.error(message)
            else:
                st.warning("모든 필드를 입력해주세요.")

    # 데이터 수정 탭
    elif tab == '데이터 수정':
        st.write("### 데이터 수정")
        operator_name_to_edit = st.text_input("수정할 운용사명 입력:", key="edit_operator_name")
        new_price = st.number_input("새 가격 입력:", min_value=0.0, step=0.01)

        if st.button("수정하기"):
            if operator_name_to_edit and new_price:
                success, message = update_data_in_db(operator_name_to_edit, new_price)
                if success:
                    st.success(message)
                    # 수정 후 세션에 새로운 데이터 갱신
                    data = fetch_all_data(limit=100)
                    st.session_state.data = data
                else:
                    st.error(message)
            else:
                st.warning("운용사명과 새 가격을 입력해주세요.")

    # 데이터 삭제 탭
    elif tab == '데이터 삭제':
        st.write("### 데이터 삭제")
        operator_name_to_delete = st.text_input("삭제할 운용사명 입력:", key="delete_operator_name")

        if st.button("삭제하기"):
            if operator_name_to_delete:
                success, message = delete_data_from_db(operator_name_to_delete)
                if success:
                    st.success(message)
                    # 삭제 후 세션에 새로운 데이터 갱신
                    data = fetch_all_data(limit=100)
                    st.session_state.data = data
                else:
                    st.error(message)
            else:
                st.warning("삭제할 운용사명을 입력해주세요.")

# 페이지 실행
show_page()
