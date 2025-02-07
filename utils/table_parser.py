from typing import List

from bs4 import BeautifulSoup


class TableParser:
    def __init__(self, html_content: str, caption: str):
        self._soup = BeautifulSoup(html_content, "html.parser")
        self._table = self._find_table_by_caption(caption)

    def _find_table_by_caption(self, caption_text: str):
        tables = self._soup.find_all("table")
        for table in tables:
            caption = table.find("caption")
            if caption and caption.get_text(strip=True) == caption_text:
                return table
        raise ValueError(f"Table with caption '{caption_text}' not found")

    def get_rows(self) -> List[List[str]]:
        rows = self._table.find_all("tr")[1:]  # пропускаем шапку таблицы
        return [self._parse_row(row) for row in rows]

    def _parse_row(self, row) -> List[str]:
        return [self._parse_cell(cell) for cell in row.find_all("td")]

    def _parse_cell(self, cell) -> str:
        for sup in cell.find_all("sup"):
            sup.decompose()  # убираем ненужные ссылки вида [1][2]...

        return cell.text.rstrip("\n")
