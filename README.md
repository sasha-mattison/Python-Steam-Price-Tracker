# 📉 Python Steam Price Tracker

A Python-based Steam wishlist price tracker that scrapes game data from Steam store pages and can send email alerts when prices drop or discounts appear.

---

## 🚀 Features

- 🔍 Scrapes Steam store pages using `requests` + `BeautifulSoup`
- 🎮 Loads wishlist URLs from '.env'
- 💰 Extracts:
  - Game name
  - Current price
  - Discount percentage
  - Original price
  - Final price (if on sale)
- 📧 Sends email notifications using `smtplib`
- 📦 Stores game data as structured Python dictionaries
- 🧠 Modular design (scraper + email system separated)

---

## 🛠️ Tech Stack

- Python 3
- requests
- BeautifulSoup4
- lxml parser
- smtplib (SMTP email sending)

---

## 📂 Project Structure

Python-Steam-Price-Tracker/<br />
│<br />
├── main.py<br />
├── scraper.py<br />
├── emailer.py<br />
│<br />
├── .env<br />
├── .gitignore<br />
└── README.md<br />



---

## ⚙️ How It Works

1. Steam game URLs are loaded from `wishlist.txt`
2. Each URL is requested using `requests`
3. HTML is parsed with BeautifulSoup
4. Game data is extracted:
   - Name
   - Price / Discount info
5. Data is stored as a list of dictionaries
6. Optional email alerts are sent when conditions are met

---

## 📧 Email Setup (Gmail SMTP)

This project uses Gmail’s SMTP server to send email alerts when a game goes on sale.

---

### 🔐 Step 1: Enable App Passwords

Gmail does NOT allow normal passwords for SMTP login.

You must:

1. Go to your Google Account
2. Navigate to **Security**
3. Enable **2-Step Verification**
4. Go to **App Passwords**
5. Generate a new app password for “Mail”

---

### 🧾 Step 2: Create password file

Run setup.py

this will create a .env file in the git directory where you can fill in the specified fields.
