from example.user.user_model import UserData
from fastapi import FastAPI

app = FastAPI()

@app.post("/user")
def add_user(user_data: UserData):
    return user_data
