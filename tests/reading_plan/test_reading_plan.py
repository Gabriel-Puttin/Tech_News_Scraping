import pytest
from unittest.mock import MagicMock
from tech_news.analyzer.reading_plan import ReadingPlanService


@pytest.fixture
def mock_news():
    return [
        {
            "url": "https://blog.betrybe.com/novidades/noticia-bacana",
            "title": "Notícia bacana",
            "timestamp": "04/04/2021",
            "writer": "Eu",
            "reading_time": 4,
            "summary": "Algo muito bacana aconteceu",
            "category": "Ferramentas",
        },
        {
            "url": "https://blog.betrybe.com/novidades/noticia-bacana",
            "title": "Notícia bacana 2",
            "timestamp": "04/04/2021",
            "writer": "Eu",
            "reading_time": 14,
            "summary": "Algo muito bacana aconteceu 2",
            "category": "Ferramentas",
        },
    ]


@pytest.fixture
def return_value():
    return {
        "readable": [
            {"chosen_news": [("Notícia bacana", 4)], "unfilled_time": 6}
        ],
        "unreadable": [("Notícia bacana 2", 14)],
    }


def test_reading_plan_group_news(mock_news, return_value):
    "It should 'group_news_for_available_time' method return a correct value"
    ReadingPlanService._db_news_proxy = MagicMock(return_value=mock_news)
    with pytest.raises(
        ValueError, match="Valor 'available_time' deve ser maior que zero"
    ):
        ReadingPlanService.group_news_for_available_time(-1)

    group_news = ReadingPlanService.group_news_for_available_time(10)
    assert group_news == return_value
