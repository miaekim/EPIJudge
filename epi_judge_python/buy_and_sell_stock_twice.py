from typing import List

from test_framework import generic_test


def buy_and_sell_stock_twice(prices: List[float]) -> float:
    buy_price = prev_price = prices[0]
    profit = 0
    for price in prices[1:]:
        if price > prev_price:
            prev_price = price
            profit = max(profit, price - buy_price)
        elif price < buy_price:
            buy_price = prev_price = price
    return profit


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock_twice.py',
                                       'buy_and_sell_stock_twice.tsv',
                                       buy_and_sell_stock_twice))
