from fastapi import FastAPI
from app.routers import test_db
from app.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="FastAPI with PostgreSQL and Streamlit")

app.include_router(test_db.router)