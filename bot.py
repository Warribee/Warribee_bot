import os
import requests
import time
from threading import Thread
from flask import Flask

TELEGRAM_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

app = Flask(__name__)

@app.route('/')
def home():
    return "Warribee Bot Live 100%"

def send_loop():
    while True:
        try:
            if TELEGRAM_TOKEN and CHAT_ID:
                msg = "GBPJPY-OTC Test signal - Bot is LIVE ✅"
                url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage?chat_id={CHAT_ID}&text={msg}"
                requests.get(url)
        except Exception as e:
            print(e)
        time.sleep(60)

Thread(target=send_loop, daemon=True).start()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
