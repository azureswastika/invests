from typing import Any

from pydantic import BaseModel


class Ticker(BaseModel):
    _id: Any
    name: str
    # api: str


class TickerBundle(BaseModel):
    tickers: list[Ticker]
