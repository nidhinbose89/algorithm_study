#!/usr/bin/env python

"""
Max sub array -- Kadane's Algo
Author:nidhinbose89
"""


def max_sub_sum(arr):
    """max_sub_sum."""
    max_sum = out_max_sum = arr[0]
    index = 1
    while index < len(arr):
        max_sum = max(arr[index], max_sum + arr[index])
        if max_sum > out_max_sum:
            out_max_sum = max_sum
        index += 1
    return out_max_sum


if __name__ == "__main__":
    arr = [1, -3, 2, -1, 1, -1, 3]
    print(max_sub_sum(arr))  # 4
