from example.database.db import FakeDB
from example.user.user_repository import UserRepository
from example.user.user import UserData, User

def test_repo_can_create_user():
    fakeDB = FakeDB()
    repo = UserRepository(fakeDB)

    user = repo.create_user(UserData(**{
        "fullname": "Hisma Mulya Sudradjat",
        "email": "mamaz@kata.ai"
    }))

    assert user is not None

def test_repo_can_get_user_by_id():
    fakeDB = FakeDB()
    repo = UserRepository(fakeDB)

    user = repo.create_user(UserData(**{
        "fullname": "Hisma Mulya Sudradjat",
        "email": "mamaz@kata.ai"
    }))
    fetched_user = repo.get_user(user.id)

    assert fetched_user.dict() == user.dict()

def test_repo_can_get_user_by_email():
    fakeDB = FakeDB()
    repo = UserRepository(fakeDB)

    user = repo.create_user(UserData(**{
        "fullname": "Hisma Mulya Sudradjat",
        "email": "mamaz@kata.ai"
    }))
    fetched_user = repo.get_user_by_email(user.email)

    assert fetched_user.dict() == user.dict()


def test_repo_can_delete_user_by_id():
    fakeDB = FakeDB()
    repo = UserRepository(fakeDB)

    user = repo.create_user(UserData(**{
        "fullname": "Hisma Mulya Sudradjat",
        "email": "mamaz@kata.ai"
    }))
    repo.delete_user(user.id)

    fetched_user = repo.get_user(user.id)

    assert fetched_user is None

