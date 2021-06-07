from typing import List

from test_framework import generic_test

def buy_and_sell_stock_twice(prices: List[float]) -> float:

    buy_price = float('inf')
    profit = 0
    profits = []
    for price in prices:
        buy_price = min(buy_price, price)
        profit = max(profit, price - buy_price)
        profits.append(profit)

    backward_profits = []
    sell_price = 0
    profit = 0
    for price in reversed(prices):
        sell_price = max(sell_price, price)
        profit = max(profit, sell_price - price)
        backward_profits.append(profit)

    total_profit = 0
    for p1, p2 in zip(profits, reversed(backward_profits)):
        total_profit = max(total_profit, p1 + p2)
    return total_profit



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock_twice.py',
                                       'buy_and_sell_stock_twice.tsv',
                                       buy_and_sell_stock_twice))
