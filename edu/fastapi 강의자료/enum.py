# from enum import Enum
import uvicorn
from fastapi import FastAPI

app = FastAPI()

class UserLevel(str):
    a = "a"
    b = "b"
    c = "c"


@app.get("/users")
def get_users(grade: UserLevel):
    return {"grade": grade}

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)