import pytest
from example.user.user import User, UserData
from example.user.user_service import UserService
from example.user.user_repository import UserRepository
from example.database.db import FakeDB

def test_it_should_be_able_to_create_user():
    fakedb = FakeDB()
    user_repo = UserRepository(fakedb)
    service = UserService(user_repo)

    new_user = service.create_user(user_data=UserData(
        fullname="Hisma Mulya",
        email="hisma.mulya@gmail.com"
    ))
    assert new_user is not None

def test_it_should_be_able_to_raise_exception_if_theres_existing_user_on_create():
    fakedb = FakeDB()
    user_repo = UserRepository(fakedb)
    service = UserService(user_repo)

    new_user = service.create_user(user_data=UserData(
            fullname="Hisma Mulya",
            email="hisma.mulya@gmail.com"
        ))
    with pytest.raises(Exception) as e:
        service.create_user(user_data=UserData(
            fullname="Mamazo",
            email="hisma.mulya@gmail.com"
        ))

def test_it_should_be_able_to_get_user():
    fakedb = FakeDB()
    user_repo = UserRepository(fakedb)
    service = UserService(user_repo)

    new_user = service.create_user(user_data=UserData(
            fullname="Hisma Mulya",
            email="hisma.mulya@gmail.com"
        ))
    fetched_user = service.get_user(new_user.id)

    assert new_user.dict() == fetched_user.dict()