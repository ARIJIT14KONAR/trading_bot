# trading_bot
Automated Binance Futures trading bot that places market orders using Python and the Binance API. Developed as part of a trading bot project submission.
/
/
# Binance Futures Trading Bot 🚀

This is a simple yet functional trading bot for Binance Futures. It connects to the Binance Futures API and executes a market buy order using credentials stored securely in a `.env` file. The bot is written in Python and is intended for educational and demonstration purposes.

---

## 📌 Features

- Connects securely to Binance Futures using API key and secret
- Executes a market **Buy** order for BTC/USDT
- Clean and modular code structure
- Environment variables for API credentials (never hardcoded)
- Error handling and status logging
- Meets the standard submission requirements for a bot project

---

## 🧠 How It Works

1. Load API credentials from `.env`
2. Connect to Binance Futures Testnet (or mainnet if configured)
3. Place a market order to buy 0.001 BTC using USDT
4. Print the order status in the terminal

---

## 🛠️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/binance-futures-bot.git
cd binance-futures-bot
