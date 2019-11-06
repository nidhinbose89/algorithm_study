#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Implement Linked List."""


class Node(object):
    """Node Implementation."""

    def __init__(self, data, next_node=None):
        """Initialize."""
        self.data = data
        self.next = next_node

    def __repr__(self):
        """Representation."""
        return "Node: {}".format(self.data)


class LinkedList(object):
    """Linked List Implementation."""

    def __init__(self, data=None):
        """Initialize."""
        self.head = Node(data)

    def append(self, data):
        """Append."""
        if not self.head.data:
            self.head = Node(data)
            return True
        current = self.head
        while current.next:
            current = current.next
        current.next = Node(data)
        return True

    def prepend(self, data):
        """Prepend."""
        new_head = Node(data)
        new_head.next = self.head
        self.head = new_head

    def delete_with_value(self, data):
        """Delete with value."""
        if not self.head.data:
            return True
        if self.head.data == data:
            self.head = self.head.next
        current = self.head
        while current.next:
            if current.next.data == data:
                # delete
                if current.next.next:
                    current.next = current.next.next
                else:
                    current.next = None
                    break
            current = current.next
        return

    def find_with_value(self, data):
        """Find with value."""
        current = self.head
        found = False
        while current:
            if current.data == data:
                found = True
                break
            current = current.next
        return found

    def print_linked_list(self):
        """Print linked list."""
        current = self.head
        print current
        while current.next:
            print current.next
            current = current.next

ll_5 = LinkedList(5)
ll_5.append(2)
ll_5.append(3)
ll_5.append(4)
ll_5.append(7)
ll_5.append(1)
ll_5.prepend(10)
ll_5.delete_with_value(1)
ll_5.delete_with_value(4)
ll_5.delete_with_value(7)

ll_5.print_linked_list()

print ll_5.find_with_value(44)
