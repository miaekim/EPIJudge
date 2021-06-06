from typing import List

from test_framework import generic_test


def buy_and_sell_stock_once(prices: List[float]) -> float:

    buy_price = prev_price = prices[0]
    sell_price = None
    profit = 0
    for price in prices[1:]:
        if price > prev_price:
            sell_price = prev_price = price
            profit = max(profit, sell_price - buy_price)
        elif price < buy_price:
            buy_price = prev_price = price
            sell_price = None
    return profit


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock.py',
                                       'buy_and_sell_stock.tsv',
                                       buy_and_sell_stock_once))
