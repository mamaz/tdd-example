from typing import Union

class DB:
    def get(self, id: str):
        pass

    def get_by_key_value(self, key_value: dict):
        pass

    def insert(self, id: str, obj: dict) -> dict:
        pass

    def delete(self, id) -> bool:
        pass

class FakeDB(DB):
    """
    Fake class for faking database operation, like queries

    Args:
        DB (DB): Base class for database operation
    """
    def __init__(self, options: dict = dict()):
        self.options = options
        self.data = dict()

    def get(self, id: str) -> Union[dict, None]:
        return self.data.get(id, None)

    def get_by_key_value(self, key: str, value: str) -> Union[dict, None]:
        for id, user_dict in self.data.items():
            value_fetched = user_dict.get(key, None)

            if value_fetched == value:
                return user_dict

        return None

    def insert(self, id: str, obj: dict) -> dict:
        self.data[id] = obj
        return obj

    def delete(self, id) -> bool:
        self.data.pop(id)
        return True
