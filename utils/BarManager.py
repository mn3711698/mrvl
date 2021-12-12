# -*- coding: utf-8 -*-
##############################################################################
# Author：QQ173782910
##############################################################################
import numpy as np
import talib


class BarManager(object):

    def __init__(self, symbols_dict, size: int = 100):

        self.size: int = size
        self.symbols_dict = symbols_dict
        self.count_dict = {}
        self.inited_dict = {}
        self.open_array_dict = {}
        self.high_array_dict = {}
        self.low_array_dict = {}
        self.close_array_dict = {}
        self.volume_array_dict = {}

        for symbol in self.symbols_dict:
            self.count_dict[symbol] = 0
            self.inited_dict[symbol] = False
            self.open_array_dict[symbol] = [0.0] * size
            self.high_array_dict[symbol] = [0.0] * size
            self.low_array_dict[symbol] = [0.0] * size
            self.close_array_dict[symbol] = [0.0] * size
            self.volume_array_dict[symbol] = [0.0] * size

    def update_bar(self, symbol, bar):

        self.count_dict[symbol] = self.count_dict.get(symbol, 0) + 1
        if not self.inited_dict.get(symbol, False) and self.count_dict.get(symbol, 0) >= self.size:
            self.inited_dict[symbol] = True

        self.open_array_dict[symbol][:-1] = self.open_array_dict[symbol][1:]
        self.high_array_dict[symbol][:-1] = self.high_array_dict[symbol][1:]
        self.low_array_dict[symbol][:-1] = self.low_array_dict[symbol][1:]
        self.close_array_dict[symbol][:-1] = self.close_array_dict[symbol][1:]
        self.volume_array_dict[symbol][:-1] = self.volume_array_dict[symbol][1:]

        self.open_array_dict[symbol][-1] = bar["open_price"]
        self.high_array_dict[symbol][-1] = bar["high_price"]
        self.low_array_dict[symbol][-1] = bar["low_price"]
        self.close_array_dict[symbol][-1] = bar["close_price"]
        self.volume_array_dict[symbol][-1] = bar["volume"]

    def donchian(self, symbol, n, array=False):

        up = talib.MAX(np.array(self.high_array_dict[symbol]), n)
        down = talib.MIN(np.array(self.low_array_dict[symbol]), n)

        if array:
            return up, down
        return up[-1], down[-1]
