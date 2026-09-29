from iqoptionapi.stable_api import IQ_Option
import time, requests, threading, os
from flask import Flask

IQ_EMAIL = "warriboelijah6@gmail.com"
IQ_PASSWORD = "Raju@1990"
TELEGRAM_TOKEN = "8862479772:AAFhQNwgi0hnYxAz6OzdT-pjnVUZE4ZBvxk"
CHAT_ID = "8609943735"
PAIRS = ["GBPJPY-OTC", "EURUSD-OTC", "EURJPY-OTC", "GBPUSD-OTC"]

app = Flask(__name__)
@app.route('/')
def home():
    return "Warribee Bot Running 24/7!"

def send_telegram(msg):
    try:
        requests.post(f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage", data={"chat_id": CHAT_ID, "text": msg}, timeout=10)
    except:
        pass

def get_sma(candles, p=7):
    return sum([c['close'] for c in candles[-p:]]) / p

def run_bot():
    Iq = IQ_Option(IQ_EMAIL, IQ_PASSWORD)
    Iq.connect()
    send_telegram("✅ Warribee 24/7 BOT don start for Render!")
    while True:
        for PAIR in PAIRS:
            try:
                candles = Iq.get_candles(PAIR, 60, 10, time.time())
                sma = get_sma(candles)
                price = candles[-1]['close']
                if abs(price - sma) < 0.08:
                    continue
                signal = "CALL 🟢 BUY" if price > sma else "PUT 🔴 SELL"
                send_telegram(f"📊 {PAIR}\n{signal}\n⏰ 1 MIN - Quotex NOW!")
                time.sleep(2)
            except:
                pass
        time.sleep(45)

threading.Thread(target=run_bot, daemon=True).start()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
