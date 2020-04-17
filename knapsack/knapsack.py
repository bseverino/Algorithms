#!/usr/bin/python

import sys
from collections import namedtuple

Item = namedtuple('Item', ['index', 'size', 'value'])


def knapsack_solver(items, capacity):
    """
    Create a dictionary:
    -The key is the index of the item
    -The value is the ratio between the item's weight and value
    -Sort by smallest ratio
    """
    item_ratios = dict(sorted({i.index: float(i.size) / float(i.value)
                               for i in items}.items(), key=lambda x: x[1]))

    knapsack = []
    total_weight = 0
    total_value = 0
    for key in item_ratios:
        if total_weight < capacity:
            position = key - 1
            ratio = item_ratios[key]
            weight = items[position][1]
            value = items[position][2]
            added_weight = total_weight + weight
            if added_weight > capacity:
                pass
            else:
                knapsack.append(items[position][0])
                total_weight = added_weight
                total_value += value

    knapsack.sort()
    return {'Value': total_value, 'Chosen': knapsack}


if __name__ == '__main__':
    if len(sys.argv) > 1:
        capacity = int(sys.argv[2])
        file_location = sys.argv[1].strip()
        file_contents = open(file_location, 'r')
        items = []

        for line in file_contents.readlines():
            data = line.rstrip().split()
            items.append(Item(int(data[0]), int(data[1]), int(data[2])))

        file_contents.close()
        print(knapsack_solver(items, capacity))
    else:
        print('Usage: knapsack.py [filename] [capacity]')
