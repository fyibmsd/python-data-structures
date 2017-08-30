"""
    Queue
    FIFO
"""


class Queue:
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
