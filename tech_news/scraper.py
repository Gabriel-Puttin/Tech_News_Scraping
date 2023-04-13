import requests
import time
from bs4 import BeautifulSoup


def fetch(url):
    try:
        response = requests.get(
            url,
            headers={"user-agent": "Fake user-agent"},
            timeout=3
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


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
