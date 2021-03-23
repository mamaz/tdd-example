from example.user.user import UserData
from example.user.user_service import UserService
from example.user.user_repository import UserRepository
from example.database.db import FakeDB
from fastapi import FastAPI, HTTPException

app = FastAPI()

db = FakeDB()
user_repo = UserRepository(db)
user_service = UserService(user_repo)

@app.post("/user", status_code=201)
def add_user(user_data: UserData):
    try:
        created_user = user_service.create_user(user_data)

        return {
            "status": "ok",
            "data": created_user
        }

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/user/{user_id}", status_code=200)
def get_user(user_id: str):
    try:
        created_user = user_service.get_user(user_id)

        return {
            "status": "ok",
            "data": created_user
        }

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
