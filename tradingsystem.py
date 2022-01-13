import alpaca_trade_api as tradeapi
import threading
import requests
from datetime import datetime
from abc import ABC, abstractmethod
#import constants as const
import logging
import numpy as np
import time

SEC_KEY = 'cWUIGDGGhGsqjSauMhgcviFr6dlGkQbTtNwXIoJO'  # Enter Your Secret Key Here
PUB_KEY = 'PKW31LNZNE7P9QCCI6MF'  # Enter Your Public Key Here
# This is the base URL for paper trading
BASE_URL = 'https://paper-api.alpaca.markets'

Log_Format = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename = "logs/logfile.log", filemode = "w", format = Log_Format,level = logging.DEBUG)
logger = logging.getLogger()

# class AlpacaPaperSocket(REST):
#     def __init__(self):
#         super().__init__(
#             key_id='YOUR_KEY_HERE',
#             secret_key='YOUR_SECRET_KEY_HERE',
#             base_url='https://paper-api.alpaca.markets'
#         )

class TradingSystem(ABC):

    def __init__(self, api, symbol, time_frame, system_id, system_label):
        # Connect to api
        # Connect to BrokenPipeError
        # Save fields to class
        self.api = api
        self.symbol = symbol
        self.time_frame = time_frame
        self.system_id = system_id
        self.system_label = system_label
        api = tradeapi.REST(key_id=PUB_KEY, secret_key=SEC_KEY, base_url=BASE_URL)
        thread = threading.Thread(target=self.system_loop)
        thread.start()

    @abstractmethod
    def place_buy_order(self):
        pass

    @abstractmethod
    def place_sell_order(self):
        pass

    @abstractmethod
    def system_loop(self):
        pass