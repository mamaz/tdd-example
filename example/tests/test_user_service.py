from example.user.user import UserData
from example.user.user_repository import UserRepository

class UserService:
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    def create_user(self, user_data: UserData):
        existing_user = self.user_repo.get_user({"email": user_data.email})

        if existing_user is not None:
            raise Exception(f"there's an existing user with email {user_data.email}, please create user with another email")

        return self.user_repo.create_user(user_data)
