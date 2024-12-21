from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from app.config import settings

DATABASE_URL = (
    f"postgresql+asyncpg://{settings.db_user}:{settings.db_password}@"
    f"{settings.db_host}:{settings.db_port}/{settings.db_name}"
)

engine = create_async_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, class_=AsyncSession)

# Dependency
async def get_db():
    async with SessionLocal() as session:
        yield session
