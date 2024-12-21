# new.py
import streamlit as st
from utils import get_db_connection
from psycopg2 import sql

# 데이터 추가 함수
def add_data_to_db(tickers, operator_name, price):
    try:
        # DB 연결
        conn = get_db_connection()
        cur = conn.cursor()

        # 데이터 추가 SQL 쿼리
        insert_query = sql.SQL("""
            INSERT INTO test_db (tickers, 운용사명, 가격)
            VALUES (%s, %s, %s)
        """)

        # 데이터 삽입
        cur.execute(insert_query, (tickers, operator_name, price))

        # 커밋 후 연결 종료
        conn.commit()
        cur.close()
        conn.close()

        return True, "데이터가 성공적으로 추가되었습니다."
    except Exception as e:
        return False, f"데이터 추가 실패: {e}"

# Streamlit UI
def show_page():
    st.title("새로운 데이터 추가")
    st.write("이곳은 새로운 데이터를 데이터베이스에 추가하는 페이지입니다.")

    # 사용자 입력 받기
    tickers = st.text_input("Tickers", placeholder="예: AAPL")
    operator_name = st.text_input("운용사명", placeholder="운용사명 입력")
    price = st.number_input("가격", min_value=0.0, format="%.2f")

    # 데이터 추가 버튼
    if st.button("데이터 추가"):
        if tickers and operator_name and price > 0:
            # 데이터 추가 함수 호출
            success, message = add_data_to_db(tickers, operator_name, price)
            if success:
                st.success(message)
            else:
                st.error(message)
        else:
            st.warning("모든 필드를 입력해주세요.")

# 페이지 실행
show_page()
