from pymongo import MongoClient


class Mongo:
    def __init__(self, host=None, port=None, *, database="main") -> None:
        self.client = MongoClient() if host and port else MongoClient(host, port)
        self.database = self.client[database]


class MongoCollection:
    def __init__(self, obj, model) -> None:
        self.obj = obj
        self.model = model

    def create(self, data):
        return self.model(**self.obj.insert_one(data))

    def select(self, ffilter={}):
        return [self.model(**obj) for obj in self.obj.find(ffilter)]

    def get(self, ffilter: dict):
        return self.model(**self.obj.find_one(ffilter))

    def update(self, ffilter: dict, update: dict):
        return self.model(**self.obj.update_one(ffilter, update))


if __name__ == "__main__":
    mongo = Mongo()
    main = MongoCollection(mongo.database["main"])
