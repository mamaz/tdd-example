from pydantic import BaseModel

class UserData(BaseModel):
    fullname: str
    email: str
