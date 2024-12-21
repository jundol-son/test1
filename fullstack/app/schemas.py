from pydantic import BaseModel

class TestDBBase(BaseModel):
    tickers : str
    운용사명 : str
    가격 : float

    class Config:
        orm_mode = True

class TestDBCreate(TestDBBase):
    """데이터 생성 시 필요한 스키마"""
    pass

class TestDBResponse(TestDBBase):
    """응답 시 반환할 스키마"""
    pass