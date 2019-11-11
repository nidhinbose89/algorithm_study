#!/usr/bin/env python
"""Heap Implementation."""
from copy import copy


class MaxHeap(object):
    """Max Heap Implementation."""

    def __init__(self, items):
        """Initializer."""
        for idx in range(len(items) - 1, -1, -1):
            self.heapify(the_input, idx)
        self.items = items

    def heapify(self, array, index):
        """Heapify."""
        left_el = 2 * index + 1
        right_el = 2 * index + 2

        largest_idx = index
        if left_el < len(array):
            if array[left_el] > array[largest_idx]:
                largest_idx = left_el
        if right_el < len(array):
            if array[right_el] > array[largest_idx]:
                largest_idx = right_el
        if largest_idx != index:
            # swap and hepify
            array[largest_idx], array[index] = array[index], array[largest_idx]
            self.heapify(array, largest_idx)

    def insert(self, element):
        """Insert an element and heapify."""
        self.items.append(element)
        new_elem_idx = len(self.items) - 1
        parent = (new_elem_idx - 1) // 2
        while parent >= 0:
            if element > self.items[parent]:
                # swap
                self.items[parent], self.items[new_elem_idx] = \
                    self.items[new_elem_idx], self.items[parent]
                new_elem_idx = parent

            parent = (parent - 1) // 2
        return new_elem_idx

    def get_top_and_heapify(self):
        """Get Top Item and heapify."""
        top_ele = None
        if self.items:
            # put last as first
            self.items[0], self.items[-1] = self.items[-1], self.items[0]
            top_ele = self.items.pop()  # now that it is swapped, get the last
            self.heapify(self.items, 0)

        return top_ele

    def sorted(self):
        """Sort via heapify -- Heap Sort."""
        initial_heap = copy(self.items)
        ret = []
        for idx in range(len(self.items)):
            ret.append(self.get_top_and_heapify())
        self.items = initial_heap
        return ret

if __name__ == '__main__':
    the_input = [64, 89, 197, 151, 101, 43, 142, 25, 189, 59]
    heap_obj = MaxHeap(the_input)
    print heap_obj.items
    print "The largest: ", heap_obj.get_top_and_heapify()
    print heap_obj.items, "items..still hepified"
    print heap_obj.sorted(), "get sorted.."
    print heap_obj.insert(120), "inserted.. return the index"
    print heap_obj.items, 'items.. heap after an insert'
    print heap_obj.sorted(), 'sorted'
