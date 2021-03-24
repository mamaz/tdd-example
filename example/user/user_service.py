from typing import Union
from example.user.user import UserData, User
from example.user.user_repository import UserRepository
class UserService:

    def __init__(self, repo: UserRepository):
        self.user_repo = repo

    def create_user(self, user_data: UserData) -> User:
        existing_user = self.user_repo.get_user_by_email(user_data.email)

        if existing_user is not None:
            raise Exception(f"user with email {existing_user.email} exists")

        return self.user_repo.create_user(user_data)

    def get_user(self, id: str) -> Union[User, None]:
        return self.user_repo.get_user(id)
