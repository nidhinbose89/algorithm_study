#!/usr/bin/env python

"""
Puzzles!!

Author:nidhinbose89
"""
import random


def find_second_largest_in(array):
    """Find second largest in an array with O(n). # No sorting.

    Second biggest is assigned when:
    1. On comparison with each element if it is smaller than
        the current first_largest and greater than current second_biggest
    2. On finding a new largest element (duh!!)
    """
    first_largest = max(array[0], array[1])
    second_biggest = min(array[0], array[1])
    for idx in range(2, len(array)):
        if array[idx] >= first_largest:
            second_biggest = first_largest
            first_largest = array[idx]
        else:
            if array[idx] > second_biggest:
                second_biggest = array[idx]

    return second_biggest

#!/usr/bin/env python

"""
Puzzles!!

Author:nidhinbose89
"""
import random


def find_second_largest_in(array):
    """Find second largest in an array with O(n). # No sorting.

    Second biggest is assigned when:
    1. On comparison with each element if it is smaller than
        the current first_largest and greater than current second_biggest
    2. On finding a new largest element (duh!!)
    """
    first_largest = max(array[0], array[1])
    second_biggest = min(array[0], array[1])
    for idx in range(2, len(array)):
        if array[idx] > first_largest:
            second_biggest = first_largest
            first_largest = array[idx]
        else:
            if second_biggest > array[idx] and array[idx] < first_largest:
                second_biggest = array[idx]

    return second_biggest


if __name__ == "__main__":
    array = random.sample(xrange(-100, 100), 10)
    array = [1, 1, 1, -1, 1]
    array = [2, 3, 6, 6, 5]
    print "Second Largest Match --> {}=={} is {}".format(find_second_largest_in(array),
                                                         sorted(
                                                             list(set(array)))[-2],
                                                         find_second_largest_in(array) == sorted(
                                                             list(set(array)))[-2]
                                                         )

if __name__ == "__main__":
    array = random.sample(xrange(1, 1000), 45)
    print "Second Largest Match -- ", find_second_largest_in(array) == sorted(array)[-2]
