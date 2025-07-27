import logging
from binance.client import Client

logging.basicConfig(filename='bot.log', level=logging.INFO)

class BasicBot:
    def __init__(self, api_key, api_secret):
        self.client = Client(api_key, api_secret)
        self.client.FUTURES_URL = 'https://testnet.binancefuture.com/fapi'

    def market_order(self, symbol, side, quantity):
        order = self.client.futures_create_order(
            symbol=symbol,
            side=side,
            type='MARKET',
            quantity=quantity
        )
        logging.info(f"Order placed: {order}")
        return order
