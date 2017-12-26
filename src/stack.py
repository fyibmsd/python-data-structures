"""
    Stack
    LIFO
"""

from .double_linked_list import DoubleLinkedList


class StackUsingArray:
    def __init__(self):
        self._stack = []

    def add(self, value):
        self._stack.append(value)

    def remove(self):
        return self._stack.pop()

    def is_empty(self):
        return not len(self._stack)

    def size(self):
        return len(self._stack)


class StackUsingLinkedList:
    def __init__(self):
        self._stack = DoubleLinkedList()

    def add(self, value):
        self._stack.lpush(value)

    def remove(self):
        return self._stack.lpop()

    def is_empty(self):
        return self._stack.is_empty()

    def size(self):
        return self._stack.size
