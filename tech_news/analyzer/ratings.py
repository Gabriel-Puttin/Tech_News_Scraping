from collections import Counter
from tech_news.database import find_news


def top_5_categories():
    content = find_news()
    categories = [news["category"] for news in content]
    c = Counter(categories)
    sort_by_category = sorted(c.most_common(5), key=lambda item: item[0])
    sort_by_common = sorted(
        sort_by_category, key=lambda item: item[1], reverse=True
    )
    most_common_categories = [category for category, _num in sort_by_common]
    return most_common_categories
