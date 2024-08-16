# SQLAlchemy 설정
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# # PostgreSQL 데이터베이스에 연결하기 위한 엔진 생성
# engine = create_engine("postgresql+psycopg2://sjsuk321:s5764191**@0.0.0.0:5432/test-postgres")
# SessionLocal = sessionmaker(
#     bind=engine,
#     autocommit=False,
#     autoflush=False,
# )

engine = create_engine("mysql+pymysql://admin:1234@0.0.0.0:3306/dev")
SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False,
)


Base = declarative_base()

"""

create_engine 함수는 SQLAlchemy에서 데이터베이스 연결을 생성하는 데 사용됩니다. 제공된 연결 문자열(connection string)은 SQLAlchemy가 데이터베이스와 통신하기 위해 필요한 정보를 포함하고 있습니다. 이를 통해 SQLAlchemy는 데이터베이스와의 세션을 설정하고 SQL 쿼리를 실행할 수 있습니다.

다음은 create_engine("postgresql+psycopg2://admin:1234@0.0.0.0:5432/dev") 연결 문자열의 각 부분에 대한 설명입니다:

postgresql+psycopg2: 이 부분은 데이터베이스 유형과 사용하는 드라이버를 나타냅니다.

postgresql은 데이터베이스 유형이 PostgreSQL임을 나타냅니다.
psycopg2는 PostgreSQL 데이터베이스와 연결하기 위해 사용하는 Python 드라이버입니다.
admin: 데이터베이스에 접속하기 위한 사용자 이름입니다. 이 경우에는 사용자 이름이 admin입니다.

1234: 데이터베이스에 접속하기 위한 비밀번호입니다. 이 경우에는 비밀번호가 1234입니다.

0.0.0.0: 데이터베이스 서버의 호스트 주소입니다. 이 경우에는 0.0.0.0으로 설정되어 있으며, 이는 모든 IP 주소에서 접속을 허용한다는 의미입니다. 실제 환경에서는 특정 IP 주소나 도메인 이름을 사용해야 할 수도 있습니다.

5432: PostgreSQL 서버의 포트 번호입니다. PostgreSQL의 기본 포트 번호는 5432입니다.

/dev: 연결할 데이터베이스의 이름입니다. 이 경우에는 데이터베이스 이름이 dev입니다.

따라서, 전체 연결 문자열 postgresql+psycopg2://admin:1234@0.0.0.0:5432/dev은 다음과 같은 의미를 갖습니다:

PostgreSQL 데이터베이스 서버에 psycopg2 드라이버를 사용하여 연결합니다.
사용자 이름은 admin이고, 비밀번호는 s5764191**입니다.
서버는 0.0.0.0 (모든 IP 주소)에서 접속을 허용합니다.
포트 번호는 5432입니다.
연결할 데이터베이스 이름은 dev입니다.
이 정보를 바탕으로 SQLAlchemy는 지정된 PostgreSQL 데이터베이스에 연결을 설정합니다.
"""