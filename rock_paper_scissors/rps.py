#!/usr/bin/python

import sys


def rock_paper_scissors(n):
    """
    -Start with list [[]]
    -In a loop with a range of n, create a new list
    -For every element in the original list, append it three times into a new list,
     with 'rock', 'paper', 'scissors' appended onto the element respectively
    -IE, going from [[]], new list should be [['rock'], ['paper'], ['scissors']]
    """
    rps = [[]]

    if n == 0:
        return rps

    for i in range(n):
        new_rps = []
        for j in rps:
            new_rps.append(j + ['rock'])
            new_rps.append(j + ['paper'])
            new_rps.append(j + ['scissors'])
        rps = new_rps

    return rps


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
