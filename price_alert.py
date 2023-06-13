from win10toast import ToastNotifier
import winsound
import time
from datetime import datetime
import numpy as np
import warnings
import pandas as pd
import ccxt
import schedule
pd.set_option('display.max_rows', None)

warnings.filterwarnings('ignore')

toaster = ToastNotifier()

symbol = 'BTC/USDT'
exchange = ccxt.binance({'api_key': '',
                        'secret': ''})


def run_bot():
    price = exchange.fetch_ticker(symbol)['last']
    if x > price or y < price:
        toaster.show_toast("Alert BTC price", f"{price}", duration=2)
        winsound.PlaySound("cena.wav", winsound.SND_FILENAME)
    else:
        print(f'current BTC price is {price}')


x = float(input('Enter your floor price:'))
y = float(input('Enter your ceil price:'))

schedule.every(5).seconds.do(run_bot)

while True:
    schedule.run_pending()
    time.sleep(1)
