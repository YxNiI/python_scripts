import csv
import time
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin


# Crawls data from a website and saves it in a csv-file.

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

    def get_as_tuple(self) -> tuple[str, str, str, str]:
        return self.__title, self.__image, self.__emoji, self.__text


def crawl_cards(website: BeautifulSoup, url: str) -> list[Card]:
    local_cards: list[Card] = []

    for local_card in website.select(".card-block"):
        title = local_card.select(".card-title span")[1].text
        image = urljoin(url, local_card.select_one("img").attrs["src"])
        emoji = local_card.select_one(".emoji").text
        text = local_card.select_one(".card-text").text

        local_cards.append(Card(title, image, emoji, text))

    return local_cards


def crawl_all(base_url: str, joined_url: str, param_cards: list[Card]) -> list[Card]:
    # Not sending too many requests.
    time.sleep(1)
    print(joined_url)

    website: BeautifulSoup = BeautifulSoup(requests.get(joined_url).text, "html.parser")
    param_cards += crawl_cards(website, joined_url)

    if website.find('a', {"class": "btn btn-primary"}) is not None:
        crawl_all(base_url, urljoin(base_url, website.select_one(".btn-primary")["href"]), param_cards)

    return param_cards


cards: list[Card] = crawl_all("...",
                              "...",
                              [])
card_tuples: list[tuple[str, str, str, str]] = [crawled_card.get_as_tuple() for crawled_card in cards]

with open("./data.csv", 'w', newline='') as file:
    writer = csv.writer(file, delimiter=';', quotechar='"')

    for card_tuple in card_tuples:
        writer.writerow(card_tuple)
