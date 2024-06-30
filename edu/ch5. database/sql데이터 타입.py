"""
DDL(Create,Alter,Drop)
DML(Insert,Select,Update,Delete) -> 데이터 조작 명령 : CRUD
- 테이블 생성 명령(쿼리)
# CREATE TABLE 테이블명(컬럼명1 데이터타입, 컬럼명2 데이터타입)
제약조건
1. primary key(구분짓는 값)
# CREATE TABLE 테이블명(컬럼명1 데이터타입 primary key, 컬럼명2 데이터타입)
2. not null
# CREATE TABLE 테이블명(컬럼명1 데이터타입 not null, 컬럼명2 데이터타입)
3. default : 기본값으로 대체
# CREATE TABLE 테이블명(컬럼명1 데이터타입 default'기본값', 컬럼명2 데이터타입)
4. unique : 중복될 시 오류 발생
   autoincrement 자동증가
# CREATE TABLE 테이블명(컬럼명1 데이터타입 autoincrement, 컬럼명2 데이터타입 unique)

-> 테이블 삭제
DROP TABLE 테이블명

->테이블 변경
ALTER TABLE


-> 테이블 조회
SELECT 컬럼명1,컬럼명2 FROM 테이블명;
-> 조건 조회
SELECT 컬럼명1,컬럼명2 FROM 테이블명 WHERE 조건;
-> 정렬
SELECT 컬럼명1,컬럼명2 FROM 테이블명 ORDER BY 컬럼명 [ASC|DESC];
-> 데이터 수정 명령
UPDATE 테이블명 SET 컬럼명1 = 값1,컬럼명2 = 값2,... WHERE 조건식;
-> 데이터 삭제
DELETE FROM 테이블명 WHERE 조건식;

-> 행추가
INSERT INTO 테이블 (컬럼1, 컬럼2, 컬럼3) VALUES ('값1','값2','값3)
GROUP BY, JOIN
SELECT count(*) FROM 테이블명 GROUP BY 컬럼명;
JOIN 두 테이블 묶어서 조회
SELECT*FROM 테이블명1 INNER JOIN 테이블명2 WHERE 조건

파이썬에서 DB사용
1. DB파일 열기
2. 커서(Cursor)생성
3. SQL 명령 실행
4. 커밋(승인) 또는 롤백(취소)
5. DB 닫기

정규화 : 여러테이블에 중복되지 않도록 다른 테이블에서 데이터를 불러옴

"""

#모듈 추가
import psycopg2
import pandas as pd
DB_Name = 'test1'
User_Name = 'postgres'
Password = 's5764191**'
Table_Name = '시가평가액'
Host_IP = '127.0.0.1'
Port_num = '5432'
db = psycopg2.connect(host=Host_IP,dbname=DB_Name,user=User_Name,password=Password,port=Port_num)
cur = db.cursor()
SELECT_SQL = "SELECT * FROM test_db"
cur.execute(SELECT_SQL)
rows = cur.fetchall()
# print(rows)
# for row in rows:
#     print(row)
df = pd.DataFrame(rows)
print(df)