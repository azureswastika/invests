from typing import Any

from pydantic import BaseModel
from pymongo import MongoClient
from pymongo.collection import Collection


class Mongo:
    def __init__(
        self, host: str = None, port: int = None, *, database: str = "main"
    ) -> None:
        self.client = MongoClient() if host and port else MongoClient(host, port)
        self.database = self.client[database]

    def get_collection(self, name: str, model: BaseModel):
        return MongoCollection(self.database[name], model)


class MongoCollection:
    def __init__(self, obj: Collection, model: BaseModel) -> None:
        self.obj = obj
        self.model = model

    def create(self, data: dict[str, Any]):
        return self.get(self.obj.insert_one(data).inserted_id)

    def get(self, ffilter: dict) -> BaseModel:
        return self.model(**self.obj.find_one(ffilter))

    def select(self, ffilter=dict()) -> list[BaseModel]:
        return [self.model(**obj) for obj in self.obj.find(ffilter)]

    def update(self, ffilter: dict, update: dict) -> BaseModel:
        return self.model(**self.obj.update_one(ffilter, update))
