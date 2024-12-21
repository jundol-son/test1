from sqlalchemy import Column, Float, Text
from app.database import Base

class TestDB(Base):
    __tablename__ = "test_db"
    tickers = Column(Text, index=True)
    운용사명 = Column(Text, primary_key=True, index=True)
    가격 = Column(Float, index=True)