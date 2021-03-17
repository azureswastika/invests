from typing import Any, Union

from pydantic import BaseModel
from pymongo.collection import Collection


class Mongo:
    def __init__(self, host: str = None, port: int = None, *, database: str) -> None: ...


class MongoCollection:
    obj: Collection
    model: BaseModel

    def __init__(self, obj: Collection, model: BaseModel) -> None: ...

    def create(self, data: Union[dict[str, Any], list[dict]]) -> BaseModel: ...

    def select(self, ffilter: dict) -> list[BaseModel]: ...

    def get(self, ffilter: dict) -> BaseModel: ...

    def update(self, ffilter: dict, update: dict) -> BaseModel: ...
