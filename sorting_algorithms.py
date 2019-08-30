#!/usr/bin/env python

"""
Sorting Algorithm Implementation.

Author:nidhinbose89
"""
import random


def selection_sort(unsorted_array):
    """Selection Sort.

    This is in ascending order. For desceding, increase j counter
    by removing -1 and make the if check to >
    It is inplace and stable.
    """
    print "In selection sort - ascending..."
    for i in range(len(unsorted_array) - 2):
        imin = i
        for j in range(i + 1, len(unsorted_array) - 1):
            if unsorted_array[j] < unsorted_array[imin]:
                imin = j
        unsorted_array[i], unsorted_array[
            imin] = unsorted_array[imin], unsorted_array[i]

    return unsorted_array


def bubble_sort(unsorted_array):
    """Bubble Sort.

    This is in ascending order. It is inplace and stable.
    """
    print "In bubble sort - ascending..."
    for k in range(len(unsorted_array)):
        flag = 0
        for i in range(len(unsorted_array) - k - 1):
            if unsorted_array[i] > unsorted_array[i + 1]:
                unsorted_array[i], unsorted_array[
                    i + 1] = unsorted_array[i + 1], unsorted_array[i]
                flag = 1
            # if the list is already sorted, there wont be any swaps
            # then it is safe to assume that the list is already sorted.
        if not flag:
            break
    return unsorted_array


def insertion_sort(unsorted_array):
    """Insertion Sort.

    This is in ascending order. It is inplace and stable.
    """
    print "In insertion sort - ascending..."
    for k in range(1, len(unsorted_array) - 1):
        value = unsorted_array[k]
        hole = k
        while hole > 0 and unsorted_array[hole - 1] > value:
            unsorted_array[hole] = unsorted_array[hole - 1]
            hole = hole - 1
        unsorted_array[hole] = value
    return unsorted_array


def merge_sort(unsorted_array):
    """Merge Sort.

    This is in ascending order. It is *NOT* inplace and stable.
    """
    def _merge(left, right):
        array = []
        if not len(left) or not len(right):
            return left or right
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                array.append(left[i])
                i += 1
            else:
                array.append(right[j])
                j += 1
        if i < len(left):
            array.extend(left[i:])
        if j < len(right):
            array.extend(right[j:])
        return array

    if len(unsorted_array) < 2:
        return unsorted_array
    mid = len(unsorted_array) / 2
    left = merge_sort(unsorted_array[:mid])
    right = merge_sort(unsorted_array[mid:])
    return _merge(left, right)


def quick_sort(unsorted_array):
    """Quick Sort.

    This is in ascending order. It is inplace and stable.
    O(nlog n) - in best
    O(n^2) - in worst, avoided with good pivot
    """
    def _quick_sort(array, start, end):

        def _partition_and_order(array, start, end):
            # push all the elements lesser than pivot to
            # the left of `partition_index`
            pivot = array[end]  # better logic for picking pivot??
            partition_index = start
            for idx in range(start, end):
                if array[idx] < pivot:
                    array[idx], array[partition_index] = array[
                        partition_index], array[idx]
                    partition_index += 1
            # swap the partition_index element with pivot
            array[end], array[partition_index] = array[
                partition_index], array[end]
            return partition_index
        if start < end:
            partition_index = _partition_and_order(unsorted_array, start, end)
            # The element at the partition_index is sorted
            _quick_sort(unsorted_array, start, partition_index - 1)
            _quick_sort(unsorted_array, partition_index + 1, end)
        return array

    return _quick_sort(unsorted_array, 0, len(unsorted_array) - 1)


def pick_smallest(unsorted_array, th_smallest=None):
    """Quick Sort.

    This is in ascending order. It is inplace and stable.
    O(nlog n) - in best
    O(n^2) - in worst, avoided with good pivot
    """
    def find_smallest_by_sort(array, start, end):

        def _get_partition(array, start, end):
            # push all the elements lesser than pivot to
            # the left of `partition_index`
            pivot = array[end]  # better logic for picking pivot??
            partition_index = start
            for idx in range(start, end):
                if array[idx] < pivot:
                    array[idx], array[partition_index] = array[
                        partition_index], array[idx]
                    partition_index += 1
            # swap the partition_index element with pivot
            array[end], array[partition_index] = array[
                partition_index], array[end]
            return partition_index
        if start < end:
            partition_index = _get_partition(array, start, end)
            # The element at the partition_index is sorted
            if partition_index == th_smallest:
                return array[partition_index]
            elif partition_index > th_smallest:
                return find_smallest_by_sort(array, start, partition_index - 1)
            else:
                return find_smallest_by_sort(array, partition_index + 1, end)

    return find_smallest_by_sort(unsorted_array, 0, len(unsorted_array) - 1)


def pick_largest(unsorted_array, th_largest=None):
    """Quick Sort.

    This is in descending order. It is inplace and stable.
    O(nlog n) - in best
    O(n^2) - in worst, avoided with good pivot
    """
    def find_largest_by_sort(array, start, end):

        def get_partition(array, start, end):
            # push all the elements lesser than pivot to
            # the left of `partition_index`
            pivot = array[end]  # better logic for picking pivot??
            partition_index = start
            for idx in range(start, end):
                if array[idx] > pivot:
                    array[idx], array[partition_index] = array[
                        partition_index], array[idx]
                    partition_index += 1
            # swap the partition_index element with pivot
            array[end], array[partition_index] = array[
                partition_index], array[end]
            return partition_index
        if start < end:
            partition_index = get_partition(array, start, end)
            # The element at the partition_index is sorted
            if partition_index == th_largest:
                return array[partition_index]
            elif partition_index < th_largest:
                return find_largest_by_sort(array, partition_index + 1, end)
            else:
                return find_largest_by_sort(array, start, partition_index - 1)

    return find_largest_by_sort(unsorted_array, 0, len(unsorted_array) - 1)


def some_sort(unsorted_array):
    """<> Sort.

    This is in ascending order. It is inplace and stable.
    """
    print "In <> sort - ascending..."
    for k in xrange(1, len(unsorted_array) - 1):
        pass
    return unsorted_array


if __name__ == "__main__":
    print "*********O(n^2) in worst case*********"
    an_array = random.sample(xrange(1, 100), 30)
    print "Going to sort {}".format(an_array)
    print selection_sort(an_array)
    print "\n"
    an_array = random.sample(xrange(1, 100), 30)
    print "Going to sort {}".format(an_array)
    print bubble_sort(an_array)
    an_array = random.sample(xrange(1, 100), 30)
    print "\n"
    print "Going to sort {}".format(an_array)
    print insertion_sort(an_array)
    an_array = random.sample(xrange(1, 100), 30)
    print "\n"
    print "*********O(nlogn) in worst case*********"
    print "In merge sort - ascending..."
    print "Going to sort {}".format(an_array)
    print merge_sort(an_array)
    print "\n"
    print "In quick sort - ascending..."
    print "Going to sort {}".format(an_array)
    an_array = random.sample(xrange(1, 100), 30)
    print quick_sort(an_array)
    print "\n"
    print "Application of Quick Sort..."
    an_array = random.sample(xrange(1, 100), 30)
    th_smallest = random.choice(xrange(30))
    print "Find {k}th smallest element in {arr}".format(k=th_smallest, arr=an_array)
    print pick_smallest(an_array, th_smallest)
    print "**verify***"
    print "Expected: ", sorted(an_array)[th_smallest]
    print "\n"
    an_array = random.sample(xrange(1, 100), 30)
    th_largest = random.choice(xrange(30))
    print "Find {k}th largest element in {arr}".format(k=th_largest, arr=an_array)
    print pick_largest(an_array, th_largest)
    print "**verify***"
    print "Expected: ", sorted(an_array, reverse=True)[th_largest]
