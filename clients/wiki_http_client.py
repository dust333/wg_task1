from typing import Optional

import requests

from clients.http_client import BaseHTTPClient
from config import WIKI_URL


class WikiHTTPClient(BaseHTTPClient):
    _BASE_URL = WIKI_URL

    def __init__(self, headers: Optional[dict[str, str]] = None):
        super().__init__(self._BASE_URL, headers)

    def get_websites_page(
        self, params: Optional[dict] = None, headers: Optional[dict] = None
    ) -> requests.Response:
        route = "/wiki/Programming_languages_used_in_most_popular_websites"

        return self.get(route, params, headers)
