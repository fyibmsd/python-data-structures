"""
    Stack
    LIFO
"""


class Stack:
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
