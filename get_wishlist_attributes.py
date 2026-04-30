import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os

load_dotenv()

html_documents = []
soups = []
game_data = []

urls = []

def load_wishlist():
    contents = os.getenv("STEAM_WISHLIST")
    urls.extend(contents.split())

def get_html_docs():
    for i, url in enumerate(urls):
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                html_documents.append(response.text)
            else:
                print(f"Error accessing URL at index: {i}\nStatus code: {response.status_code}")
        except Exception as e:
            print(f"Request failed: {e}")

def scrape_documents():
    for doc in html_documents:
        soup = BeautifulSoup(doc, 'lxml')
        soups.append(soup)

def get_game_data():
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
        if discount_final_price_tag and discount_pct_tag:
            game["final_price"] = discount_final_price_tag.get_text(strip=True)

        game_data.append(game)

def get_wishlist_attributes():
    load_wishlist()
    get_html_docs()
    scrape_documents()
    get_game_data()

    return game_data