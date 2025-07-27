from basic_bot import BasicBot
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("BINANCE_API_KEY")
api_secret = os.getenv("BINANCE_API_SECRET")

bot = BasicBot(api_key, api_secret)

try:
    result = bot.market_order("BTCUSDT", "BUY", 0.001)
    print("✅ Order executed:", result)
except Exception as e:
    print("❌ Failed:", e)
