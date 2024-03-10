import time
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin


# Crawls data from a website and prints it.

class Card:
    def __init__(self: "Card", title: str, image: str, emoji: str, text: str) -> None:
        self.__title = title
        self.__image = image
        self.__emoji = emoji
        self.__text = text

    def __str__(self) -> str:
        return """
        title=\"{title}\",
        image=\"{image}\",
        emoji=\"{emoji}\",
        text=\"{text}\"""".format(title=self.__title, image=self.__image, emoji=self.__emoji, text=self.__text)


def crawl_cards(website, url) -> list[Card]:
    cards: list[Card] = []

    for card in website.select(".card-block"):
        title = card.select(".card-title span")[1].text
        image = urljoin(url, card.select_one("img").attrs["src"])
        emoji = card.select_one(".emoji").text
        text = card.select_one(".card-text").text

        cards.append(Card(title, image, emoji, text))

    return cards


def crawl_all(website_strs: list[str], base_url: str, joined_url: str, site_count: int) -> list[str]:

    # Not sending too many requests.
    time.sleep(1)
    print(joined_url)

    website: BeautifulSoup = BeautifulSoup(requests.get(joined_url).text, "html.parser")
    card_str: str = '\n'.join([str(card) for card in crawl_cards(website, base_url)])

    partition: str = "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
    site_count_str = str(site_count)
    website_strs.append(site_count_str + partition + site_count_str + '\n' + card_str)

    if website.find('a', {"class": "btn btn-primary"}) is not None:
        site_count += 1
        crawl_all(website_strs, base_url, urljoin(base_url, website.select_one(".btn-primary")["href"]), site_count)

    return website_strs


print('\n'.join([website for website in crawl_all([],
                                                  "...",
                                                  "...",
                                                  1)]))
