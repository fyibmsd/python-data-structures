# -*-coding:utf-8-*-
#
# author: fyibmsd
# desc: double ended queue

from collections import deque
from .double_linked_list import DoubleLinkedList


class Deque(deque):
    def __init__(self):
        super(Deque, self).__init__()
        self._queue = DoubleLinkedList()

    def append(self, *args, **kwargs):
        """ Add an element to the right side of the deque. """
        for arg in args:
            self._queue.rpush(arg)

    def appendleft(self, *args, **kwargs):
        """ Add an element to the left side of the deque. """
        for arg in args:
            self._queue.lpush(arg)

    def clear(self, *args, **kwargs):
        """ Remove all elements from the deque. """
        while self._queue.is_empty() is False:
            self._queue.lpop()

    def count(self, value):
        """ D.count(value) -> integer -- return number of occurrences of value """
        return self._queue.size

    def pop(self, *args, **kwargs):
        """ Remove and return the rightmost element. """
        return self._queue.rpop()

    def popleft(self, *args, **kwargs):
        """ Remove and return the leftmost element. """
        return self._queue.lpop()

    def remove(self, value):
        """ D.remove(value) -- remove first occurrence of value. """
        return self._queue.remove(value)
