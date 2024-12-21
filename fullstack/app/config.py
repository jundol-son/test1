from pydantic import BaseSettings

class Settings(BaseSettings):
    db_host: str = "localhost"
    db_port: int = 5432
    db_name: str = "test1"
    db_user: str = "postgres"
    db_password: str = "s5764191**"

    class Config:
        env_file = ".env"  # .env 파일에서 환경 변수 로드

# 전역 설정 객체 생성
settings = Settings()
