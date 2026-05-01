import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushsave_Button, QWidget, QVBoxLayout
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

        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://store.steampowered.com"))

        self.save_button = QPushsave_Button("Save game to wishlist")
        self.save_button.clicked.connect(self.on_click)

        container = QWidget()
        layout = QVBoxLayout()

        layout.addWidget(self.save_button)
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
