from __future__ import annotations
from uuid import uuid4
from typing import Tuple
from pydantic import BaseModel
from re import sub
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
            "initial_name": create_initial_name(fullname)
        }

        return User(**user_dict)

def split_fullname(fullname: str) -> Tuple[str, str, str]:
    names = fullname.split(" ")
    middle_name = " ".join(names[1:len(names)-1]) if len(names) >= 3 else ""
    first_name = names[0]
    last_name = names[len(names)-1] if len(names) > 1 else ""

    return (first_name, middle_name, last_name)

def create_initial_name(fullname) -> str:
    trimmed_fullname = sub(r"[^\w\s]", "", fullname) # replace punctuation with empty string
    print(trimmed_fullname)
    names = trimmed_fullname.split(" ")
    initials = [n.capitalize()[0] for n in names if len(n) > 0]

    return "".join(initials)
