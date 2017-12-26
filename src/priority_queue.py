# -*-coding:utf-8-*-
#
# author: fyibmsd
# desc: priority queue

from .binary_heap import MaxBinaryHeap


class PriorityQueue:
    def __init__(self):
        self._queue = {}
        self._heap = MaxBinaryHeap()

    def size(self):
        return len(self._queue)

    def is_empty(self):
        return self.size() is 0

    def insert(self, value, priority):
        self._queue[priority] = value
        self._heap.insert(priority)

    def dequeue(self):
        if self.is_empty():
            return None

        priority = self._heap.remove_max()

        return self._queue.pop(priority), priority
