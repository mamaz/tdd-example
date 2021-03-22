from typing import Union
from example.user.user import User, UserData
from example.database.db import DB

class UserRepository:
    def __init__(self, db: DB):
        self.db = db

    def get_user(self, id: str) -> Union[User, None]:
        usr_dict = self.db.get(id)

        return User(**usr_dict) if usr_dict is not None else None

    def get_user_by_email(self, email: str) -> Union[User, None]:
        user_dict = self.db.get_by_key_value({"email": email})

        return User(**user_dict) if user_dict is not None else None

    def create_user(self, user_data: UserData) -> User:
        """
        obj is saved as dict of User
        """
        user = User.create(user_data)
        self.db.insert(id=user.id, obj=user.dict())

        return user

    def delete_user(self, id: str) -> bool:
        self.db.delete(id)

        return True
