import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os

load_dotenv()


import json

def load_wishlist():
    raw = os.getenv("STEAM_WISHLIST", "[]")

    try:
        urls = json.loads(raw)
    except json.JSONDecodeError:
        print("Invalid STEAM_WISHLIST format in .env")
        return []

    return urls if isinstance(urls, list) else []



def get_html_docs(urls):
    html_documents = []

    for i, url in enumerate(urls):
        try:
            response = requests.get(url, timeout=5)

            if response.status_code == 200:
                html_documents.append(response.text)
            else:
                print(f"[{i}] Error: status {response.status_code} for {url}")

        except Exception as e:
            print(f"[{i}] Request failed for {url}: {e}")

    return html_documents


def scrape_documents(html_documents):
    return [
        BeautifulSoup(doc, "lxml")
        for doc in html_documents
    ]


def get_game_data(soups):
    game_data = []

    for soup in soups:
        game = {}

        app_name = soup.find("div", class_="apphub_AppName")
        if app_name:
            game["name"] = app_name.get_text(strip=True)

        price_tag = soup.find("div", class_="game_purchase_price")
        if price_tag:
            game["price"] = price_tag.get_text(strip=True)

        discount_pct_tag = soup.find("div", class_="discount_pct")
        if discount_pct_tag:
            game["discount_pct"] = discount_pct_tag.get_text(strip=True)

        discount_og_price_tag = soup.find("div", class_="discount_original_price")
        if discount_og_price_tag:
            game["original_price"] = discount_og_price_tag.get_text(strip=True)

        discount_final_price_tag = soup.find("div", class_="discount_final_price")
        if discount_final_price_tag:
            game["final_price"] = discount_final_price_tag.get_text(strip=True)

        if game:  # only add non-empty entries
            game_data.append(game)

    return game_data


def get_wishlist_attributes():
    urls = load_wishlist()

    html_documents = get_html_docs(urls)
    soups = scrape_documents(html_documents)
    game_data = get_game_data(soups)

    return game_data
