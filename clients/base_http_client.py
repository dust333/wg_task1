from typing import Optional

import requests

from utils.logger import LoggerClass


class BaseHTTPClient:
    def __init__(self, base_url: str, headers: Optional[dict] = None):
        self._session = requests.Session()
        self._logger = LoggerClass(self.__class__.__name__)

        self.base_url = base_url
        self.headers = headers if headers else {}

    @property
    def base_url(self) -> str:  # на всякий случай добавил проперти
        return self.__base_url

    @base_url.setter
    def base_url(self, value) -> None:
        if isinstance(value, str):
            self.__base_url = value
        else:
            raise TypeError

    @property
    def headers(self) -> dict:
        return self.__headers

    @headers.setter
    def headers(self, value):
        if isinstance(value, dict):
            self.__headers = value
            self._session.headers.update(self.headers)
        else:
            raise TypeError

    def _log_request(
        self,
        method: str,
        url: str,
        headers: dict,
        **kwargs,
    ) -> None:
        self._logger.info(f"Request: {method} {url}")
        self._logger.info(f"Headers: {headers if headers else self._session.headers}")

        # тут бы реализовать логгирование остальных частей запроса, или использовать логгирование urllib3

    def _log_response(self, response: requests.Response) -> None:
        self._logger.info(f"Response: {response.status_code} {response.url}")
        self._logger.info(f"Headers: {response.headers}")
        self._logger.info(f"Body: {response.text}")

    def _request(
        self,
        method: str,
        request_url: str,
        headers: Optional[dict] = None,
        **kwargs,
    ) -> requests.Response:
        url = f"{self.base_url}{request_url}"
        self._log_request(method, url, headers, **kwargs)

        try:
            response = self._session.request(
                method=method,
                url=url,
                headers=headers if headers else self.headers,
                **kwargs,
            )
            self._log_response(response)
            return response
        except requests.exceptions.RequestException as e:
            self._logger.error(e)
            raise e

    def get(
        self, endpoint, params: Optional[dict] = None, headers: Optional[dict] = None
    ) -> requests.Response:
        return self._request("GET", endpoint, params=params, headers=headers)

    def post(
        self,
    ) -> requests.Response:  # для экономии времени не стал реализовывать
        return NotImplemented

    def put(
        self,
    ) -> requests.Response:
        return NotImplemented

    def delete(
        self,
    ) -> requests.Response:
        return NotImplemented
