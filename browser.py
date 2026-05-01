import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QVBoxLayout
from PyQt6.QtCore import QUrl
from PyQt6.QtWebEngineWidgets import QWebEngineView
from dotenv import set_key, load_dotenv
import os
import json


load_dotenv()

raw = os.getenv("STEAM_WISHLIST")

if raw and raw.strip():
    try:
        wishlist = json.loads(raw)
    except json.JSONDecodeError:
        wishlist = []
else:
    wishlist = []

class Browser(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Steam")

        # Browser
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://store.steampowered.com"))

        # Button
        self.button = QPushButton("Save game to wishlist")
        self.button.clicked.connect(self.on_click)

        # Layout
        container = QWidget()
        layout = QVBoxLayout()

        layout.addWidget(self.button)
        layout.addWidget(self.browser)

        container.setLayout(layout)
        self.setCentralWidget(container)

    def on_click(self):
        current_url = self.browser.url().toString()
        add_to_wishlist(current_url)


def add_to_wishlist(content):
    wishlist.append(content)

    temp = " ".join(wishlist)
    set_key(".env", "STEAM_WISHLIST", json.dumps(wishlist), quote_mode="never")


# App
app = QApplication(sys.argv)
window = Browser()
window.show()
app.exec()
