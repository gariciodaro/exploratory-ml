"""
Module to find cost of wishes below given condition.

@author: Gari Ciodaro
@date: 2022-06-20
"""

import numpy as np


def compute_gift_cost(gift_costs_path):
    """Read file in gift_costs_path. Compute total cost of accepted wishes"""
    with open(gift_costs_path, encoding='utf-8') as file_path:
        gift_costs_list = np.arrary(file_path.read().split('\n')).astype(int)
    total_cost = gift_costs_list[gift_costs_list < 25] * 1.08
    return total_cost


if __name__ == '__main__':
    TOTAL_COST = compute_gift_cost('../data/gift_costs.text')
    print(f'Total cost would be: {TOTAL_COST}')
