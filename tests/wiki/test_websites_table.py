import allure
import pytest
from assertpy import assert_that, soft_assertions

from models.popular_website_model import PopularWebsite


class TestWebsitesTable:
    @pytest.mark.parametrize(
        "min_popularity",
        (
            10**7,
            int(1.5 * (10**7)),
            5 * (10**7),
            10**8,
            5 * (10**8),
            10**9,
            int(1.5 * (10**9)),
        ),
    )
    @allure.title("Минимальная популярность не ниже {min_popularity}")
    @pytest.mark.websites
    def test_check_min_popularity(
        self,
        websites_table: list[PopularWebsite],
        min_popularity: int,
    ) -> None:
        with soft_assertions():
            for website in websites_table:
                with allure.step(f"Проверка {website}"):
                    description = (
                        f"{website.name} (Frontend:{website.frontend.as_string}|Backend:{website.backend.as_string}) "
                        f"has {website.popularity.as_int} unique visitors per month."
                        f"(Expected more than {min_popularity})"
                    )
                    assert_that(
                        int(website),
                        description=description,
                    ).is_greater_than_or_equal_to(min_popularity)
