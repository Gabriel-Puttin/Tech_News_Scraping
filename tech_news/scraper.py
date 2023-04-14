import requests
import time
from bs4 import BeautifulSoup
from tech_news.database import create_news


def formated_str(phrase: str) -> str:
    result = ""
    if phrase[-1] == " ":
        result = phrase[:-1]
    else:
        result = phrase
    return result.replace("\xa0", "")


def fetch(url):
    try:
        response = requests.get(
            url, headers={"user-agent": "Fake user-agent"}, timeout=3
        )
        time.sleep(1)
        if response.status_code != 200:
            return None
    except requests.ReadTimeout:
        return None
    return response.text


def scrape_updates(html_content):
    urls = []
    soup = BeautifulSoup(html_content, "html.parser")
    cards = soup.find_all("h2", {"class": "entry-title"})
    for card in cards:
        urls.append(card.a["href"])
    return urls


def scrape_next_page_link(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    next_page_link = soup.find("a", {"class": "next page-numbers"})
    return next_page_link["href"] if next_page_link else None


def scrape_news(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    news_report = dict()
    news_report["url"] = soup.find("div", {"class": "pk-share-buttons-wrap"})[
        "data-share-url"
    ]
    news_report["title"] = formated_str(
        soup.find("h1", {"class": "entry-title"}).string
    )
    news_report["timestamp"] = soup.find("li", {"class": "meta-date"}).string
    news_report["writer"] = soup.find("a", {"class": "url fn n"}).string
    data_ul = soup.find("ul", {"class": "post-meta"})
    data_li = [li.text for li in data_ul.find_all("li")][-1]
    news_report["reading_time"] = [
        int(num) for num in data_li.split() if num.isdigit()
    ][0]
    data_p = soup.find("div", {"class": "entry-content"})
    news_report["summary"] = formated_str(
        [p.text for p in data_p.find_all("p")][0]
    )
    news_report["category"] = soup.find("span", {"class": "label"}).string
    return news_report


def get_tech_news(amount):
    news = []
    blog = "https://blog.betrybe.com/"
    html_blog = fetch(blog)
    news_links = scrape_updates(html_blog)
    next_page = scrape_next_page_link(html_blog)

    while amount > len(news_links):
        html_content_next_page = fetch(next_page)
        news_links_next_page = scrape_updates(html_content_next_page)
        news_links.extend(news_links_next_page)
        next_page = scrape_next_page_link(html_content_next_page)

    for link in news_links[:amount]:
        news.append(scrape_news(fetch(link)))

    create_news(news)
    return news
