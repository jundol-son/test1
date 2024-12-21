import psycopg2
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
