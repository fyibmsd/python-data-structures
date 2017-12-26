"""
    Queue
    FIFO
"""

from .double_linked_list import DoubleLinkedList


class QueueUsingArray:
    def __init__(self):
        self._queue = []

    def enqueue(self, value):
        self._queue.append(value)

    def dequeue(self):
        return self._queue.pop(0)

    def is_empty(self):
        return not len(self._queue)

    def size(self):
        return len(self._queue)


class QueueUsingLinkedList:
    def __init__(self):
        self._queue = DoubleLinkedList()

    def enqueue(self, value):
        self._queue.lpush(value)

    def dequeue(self):
        return self._queue.rpop()

    def is_empty(self):
        return self._queue.is_empty()

    def size(self):
        return self._queue.size
