from tech_news.database import search_news


def search_by_title(title: str):
    query = {
        "title": {"$regex": title.lower()}
    }
    content = search_news(query)

    return [(news["title"], news["url"]) for news in content]


# Requisito 8
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
