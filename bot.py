import os
import requests
import time
from threading import Thread
from flask import Flask

app = Flask(__name__)

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

@app.route('/')
def home():
    return "Warribee Bot is LIVE!"

def send_message():
    while True:
        try:
            if BOT_TOKEN and CHAT_ID:
                text = "Warribee Bot LIVE test ✅"
                url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
                requests.post(url, data={"chat_id": CHAT_ID, "text": text})
        except:
            pass
        time.sleep(60)

Thread(target=send_message, daemon=True).start()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
