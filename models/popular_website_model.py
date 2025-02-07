from dataclasses import dataclass, field
from typing import List

from utils.logger import LoggerClass

logger = LoggerClass("models")


@dataclass
class StringParser:
    as_string: str
    as_list: List[str] = field(init=False)

    def __post_init__(self):
        self.as_list = self.as_string.replace(" ", "").split(",")


@dataclass
class Frontend(StringParser):
    pass


@dataclass
class Backend(StringParser):
    pass


@dataclass
class Database(StringParser):
    pass


@dataclass
class Popularity:
    as_string: str
    as_int: int = field(init=False)

    def __int__(self) -> int:
        return self.as_int

    def __post_init__(self):
        self.as_int = self._parse_popularity()

    def _parse_popularity(self) -> int:
        number_with_dots_or_commas = self.as_string.split(" ")[0]
        popularity = number_with_dots_or_commas.replace(",", "").replace(".", "")
        try:
            return int(popularity)
        except ValueError as e:
            logger.error("Can't parse int from popularity string")
            raise e


@dataclass
class PopularWebsite:
    name: str
    popularity: Popularity
    frontend: Frontend
    backend: Backend
    database: Database
    notes: str = field(default="")  # не везде есть значения в notes

    def __int__(self) -> int:
        return int(self.popularity)

    def __str__(self) -> str:
        return self.name
