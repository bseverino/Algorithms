#!/usr/bin/python

import argparse


def find_max_profit(prices):
    """
    -Loop through the array except for the final price
    -If price is lower than current min price, store it
    -Subtract current lowest price from every price that comes after it
    -If profit is larger than max profit so far, store it
    """
    current_min_price_so_far = prices[0]
    max_profit_so_far = prices[1] - prices[0]

    for x in range(len(prices) - 1):
        if prices[x] <= current_min_price_so_far:
            current_min_price_so_far = prices[x]
        for y in range(x + 1, len(prices) - 1):
            profit = prices[y] - prices[x]
            if profit > max_profit_so_far:
                max_profit_so_far = profit

    return max_profit_so_far


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
