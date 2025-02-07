from typing import Callable

import pytest

from clients.wiki.wiki_http_client import WikiHTTPClient
from models.wiki.popular_website_model import (Backend, Database, Frontend,
                                               Popularity, PopularWebsite)
from utils.table_parser import TableParser


@pytest.fixture(scope="session")
def wiki_http_client_factory() -> Callable[[str], WikiHTTPClient]:
    """Реализовал такой подход для возможности использования фикстуры в других со скоупом
    session, при этом что бы была возможность использовать в тестах(когда понадобится) со скоуком
    аналогичному function, что бы не таскать из теста в тест заголовки, куки и пр.
    Ранее так не делал
    """
    clients = {}

    def _create_client(scope: str = "function") -> WikiHTTPClient:
        if scope == "session":
            if "session_client" not in clients:
                clients["session_client"] = WikiHTTPClient()
            return clients["session_client"]
        elif scope == "function":
            return WikiHTTPClient()

    return _create_client


@pytest.fixture(scope="session")
def websites_table(
    wiki_http_client_factory: Callable[[str], WikiHTTPClient],
) -> list[PopularWebsite]:
    target_header = "Programming languages used in most popular websites*"
    response = wiki_http_client_factory("session").get_websites_page()

    table = TableParser(html_content=response.text, caption=target_header)
    rows = table.get_rows()

    table_data = [
        PopularWebsite(
            name=row[0],
            popularity=Popularity(row[1]),
            frontend=Frontend(row[2]),
            backend=Backend(row[3]),
            database=Database(row[4]),
            notes=row[5],
        )
        for row in rows
    ]

    yield table_data
