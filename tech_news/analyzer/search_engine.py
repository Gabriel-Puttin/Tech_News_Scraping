from tech_news.database import search_news
from datetime import datetime


def convert_to_tuple(content: list[dict]) -> list[tuple]:
    return [(news["title"], news["url"]) for news in content]


def search_by_title(title: str) -> list[tuple]:
    query = {"title": {"$regex": title.lower()}}
    content = search_news(query)

    return convert_to_tuple(content)


def search_by_date(date: str) -> list[tuple]:
    try:
        new_date = datetime.strptime(date, "%Y-%m-%d").strftime("%d/%m/%Y")
        query = {"timestamp": new_date}
        content = search_news(query)

    except (ValueError):
        raise ValueError("Data inválida")

    return convert_to_tuple(content)


def search_by_category(category: str) -> list[tuple]:
    query = {"category":  category.capitalize()}
    content = search_news(query)

    return convert_to_tuple(content)
