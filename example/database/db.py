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
    def __init__(self, options):
        self.options = options
        self.data = dict()

    def get(self, id: str) -> Union[dict, None]:
        return self.data.get(id, None)

    def get_by_key_value(self, key_value: dict) -> Union[dict, None]:
        for key in key_value.keys():
            value = self.data.get(key, None)

            if value is not None:
                return value

        return None

    def insert(self, id: str, obj: dict) -> dict:
        self.data[id] = obj
        return obj

    def delete(self, id) -> bool:
        self.data.pop(id)
        return True
