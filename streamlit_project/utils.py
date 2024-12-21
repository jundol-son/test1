import psycopg2
from psycopg2 import sql
import pandas as pd

def get_db_connection():
    """PostgreSQL 데이터베이스에 연결"""
    conn = psycopg2.connect(
        host="127.0.0.1",          # PostgreSQL 서버 주소
        database="test1",  # 데이터베이스 이름
        user="postgres",      # 사용자 이름
        password="s5764191**",  # 비밀번호
        port=5432                  # 포트 (기본값 5432)
    )
    return conn

def fetch_data_by_operator(operator_name):
    """운용사명을 기반으로 데이터를 조회"""
    conn = get_db_connection()
    query = f"""
    SELECT * FROM test_db
    WHERE 운용사명 LIKE %s
    """
    df = pd.read_sql(query, conn, params=(f"%{operator_name}%",))
    conn.close()
    return df

def fetch_all_data(limit=100):
    """전체 데이터를 조회 (LIMIT 적용)"""
    conn = get_db_connection()
    query = f"""
    SELECT * FROM test_db
    LIMIT %s
    """
    df = pd.read_sql(query, conn, params=(limit,))
    conn.close()
    return df

# 새로운 데이터 추가
def add_data_to_db(tickers, operator_name, price):
    try:
        conn = get_db_connection()
        cur = conn.cursor()

        insert_query = sql.SQL("INSERT INTO test_db (tickers, 운용사명, 가격) VALUES (%s, %s, %s)")
        cur.execute(insert_query, (tickers, operator_name, price))
        conn.commit()
        cur.close()
        conn.close()
        return True, "데이터가 성공적으로 추가되었습니다."
    except Exception as e:
        return False, f"데이터 추가 중 오류가 발생했습니다: {e}"

# 데이터 수정
def update_data_in_db(operator_name, new_price):
    try:
        conn = get_db_connection()
        cur = conn.cursor()

        update_query = sql.SQL("UPDATE test_db SET 가격 = %s WHERE 운용사명 = %s")
        cur.execute(update_query, (new_price, operator_name))
        conn.commit()

        if cur.rowcount > 0:
            cur.close()
            conn.close()
            return True, "데이터가 성공적으로 수정되었습니다."
        else:
            cur.close()
            conn.close()
            return False, "운용사명을 찾을 수 없습니다."
    except Exception as e:
        return False, f"데이터 수정 중 오류가 발생했습니다: {e}"

# 데이터 삭제
def delete_data_from_db(operator_name):
    try:
        conn = get_db_connection()
        cur = conn.cursor()

        delete_query = sql.SQL("DELETE FROM test_db WHERE 운용사명 = %s")
        cur.execute(delete_query, (operator_name,))
        conn.commit()

        if cur.rowcount > 0:
            cur.close()
            conn.close()
            return True, "데이터가 성공적으로 삭제되었습니다."
        else:
            cur.close()
            conn.close()
            return False, "운용사명을 찾을 수 없습니다."
    except Exception as e:
        return False, f"데이터 삭제 중 오류가 발생했습니다: {e}"