from __future__ import annotations
from uuid import uuid4
from typing import Tuple
from pydantic import BaseModel

class UserData(BaseModel):
    fullname: str
    email: str

class User(BaseModel):
    id: str
    email: str
    first_name: str
    middle_name: str
    last_name: str
    initial_name: str

    @classmethod
    def create(cls, user_data: UserData) -> User:
        fullname = user_data.fullname
        (first_name, middle_name, last_name) = split_fullname(fullname)

        user_dict = {
            "id": str(uuid4()),
            "email": user_data.email,
            "first_name": first_name,
            "middle_name": middle_name,
            "last_name": last_name,
            "initial_name": initial_name(fullname)
        }

        return User(**user_dict)

def split_fullname(fullname: str) -> Tuple[str, str, str]:
    return ("", "", "")

def initial_name(fullname) -> str:
    return ""
